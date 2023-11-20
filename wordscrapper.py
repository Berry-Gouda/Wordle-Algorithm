from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
from datetime import datetime, date

class WordGatherer:

    def __init__(self, currentWord : bool):
        self.website = 'https://www.stadafa.com/2021/09/every-worlde-word-so-far-updated-daily.html'
        self.latestWord = currentWord



listOfMonths = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
finalDataSet = [[]]

scrapper = WordGatherer(True)

html = urlopen(scrapper.website)
bs = BeautifulSoup(html.read(), 'html.parser')

if scrapper.latestWord:
    
    yesterdayData = []
    todayData = []

    f1 = open('WordHistoricalData.csv', "r")
    yesterdayData = f1.readlines()[-1]
    f1.close()

    strGameNum =''
    for i in range(len(yesterdayData)):



        if yesterdayData[i] == ',':
            break

        strGameNum += yesterdayData[i]

    gameNum = int(strGameNum)

    todayData.append(gameNum+1)

    today = date.today()
    todayData.append(today.strftime("%Y-%m-%d"))
    todayWord = bs.find('div', {'class':'spoiler'}).find('div').get_text()
    todayData.append(todayWord)


    with open('WordHistoricalData.csv', 'a') as file:
        writerObj = csv.writer(file)
        writerObj.writerow(todayData)
        file.close()

else:
    listOfWords = bs.find_all('p')

    cleanedUpWords = []

    for word in listOfWords:
        currentWord = word.get_text()
        if len(currentWord) < 23 or len(currentWord) > 150:
            continue
        if not currentWord[0].isnumeric():
            continue
        if not any(month in currentWord for month in listOfMonths):
            continue
        
        counter = 0
        finalWord = ''

        for tchar in currentWord:
            if tchar == '-':
                counter = counter + 1
                if counter == 2:
                    break
            else:
                finalWord = finalWord + tchar

        cleanedUpWords.append(finalWord)

    for word in cleanedUpWords:
        
        singleDataSetEntry = []

        for i in range(len(word)-1):
            if word[i] == '.':
                decimalLoc = i
                singleDataSetEntry.append(word[:i])
                singleDataSetEntry.append(word[i+2:i+7])
                singleDataSetEntry.append(word[i+9:])

        if len(singleDataSetEntry) > 1:
            singleDataSetEntry[2] = singleDataSetEntry[2].replace('  ', ' ')
            singleDataSetEntry[2] = singleDataSetEntry[2].replace(' ', '-') 
            singleDataSetEntry[2] = singleDataSetEntry[2].replace('January','01')
            singleDataSetEntry[2] = singleDataSetEntry[2].replace('February','02')
            singleDataSetEntry[2] = singleDataSetEntry[2].replace('March','03')
            singleDataSetEntry[2] = singleDataSetEntry[2].replace('April','04')
            singleDataSetEntry[2] = singleDataSetEntry[2].replace('May','05')
            singleDataSetEntry[2] = singleDataSetEntry[2].replace('June','06')
            singleDataSetEntry[2] = singleDataSetEntry[2].replace('July','07')
            singleDataSetEntry[2] = singleDataSetEntry[2].replace('August','08')
            singleDataSetEntry[2] = singleDataSetEntry[2].replace('September','09')
            singleDataSetEntry[2] = singleDataSetEntry[2].replace('October','10')
            singleDataSetEntry[2] = singleDataSetEntry[2].replace('November','11')
            singleDataSetEntry[2] = singleDataSetEntry[2].replace('December','12')

            if '-' == singleDataSetEntry[2][len(singleDataSetEntry[2])-1]:
                singleDataSetEntry[2] = singleDataSetEntry[2][:len(singleDataSetEntry[2])-1]

            dateObj = datetime.strptime(singleDataSetEntry[2], '%d-%m-%Y').date()

            singleDataSetEntry[2] = dateObj

            finalDataSet.append(singleDataSetEntry)

    finalDataSet.reverse()

    file = open('WordHistoricalData.csv', 'w', newline='')
    writer = csv.DictWriter(file, fieldnames=['Game Number', 'Date', 'Word'])
    writer.writeheader()
    for data in finalDataSet:
        if len(data) > 1:
            writer.writerow({'Game Number':data[0], 'Date':data[2], 'Word':data[1]})

    file.close()





    