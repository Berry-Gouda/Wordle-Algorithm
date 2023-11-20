from WordleBot import WordleBot
#from models import Word
import csv



def AddAllWords():
    """"Pulls all of the words out of the historical data, formats to lowercase, and adds to a list"""

    counter = 0

    while counter < len(historicalData):


        solvedData[counter][2] = historicalData[counter][:-1].lower()
        botSolvers.append(WordleBot(False, historicalData[counter][:-1].lower()))
        counter +=1


def AddGameNumbers():
    """Adds the game number to solved words dataset"""

    global solvedData

    counter = 0

    while counter < len(historicalData):

        tempString = ''
        tempList = [None]*11
        stringSliceCounter = 0

        #loop through the historical data set to get just the game number
        for c in historicalData[counter]:

            if c == ',':
                break

            tempString += c

            stringSliceCounter += 1
            

        tempList[0] = tempString

        solvedData.append(tempList)

        historicalData[counter] = historicalData[counter][stringSliceCounter+1:]

        counter += 1

def AddGameDates():
    """Adds the game date to solved words dataset"""

    global solvedData
    counter = 0


    while counter < len(historicalData):



        solvedData[counter][1] = historicalData[counter][:10]
        historicalData[counter] = historicalData[counter][11:]
        counter += 1


def AddHistoricalDataToSolvedDataSet():
    """Adds the historical data to the final data output"""
    global currentDataSetIndex

    #Get the game number
    AddGameNumbers()

    #Get the date
    AddGameDates()

    #Get the Solution Words
    AddAllWords()
    

def AddSolvedData(data:list, index:int):
    """Adds Solved Data to the data set"""

    global solvedData
    global sumGuessNumbers

    for i in range(len(data)):
        solvedData[index][i+3] = data[i]

    if data[0] == False:
        print(data)
        wordsNotSolved.append(solvedData[index][2])

    sumGuessNumbers += int(data[1])



def SolveWordles():
    """Solves the Wordle And calls the output data format functions"""

    for i in range(len(botSolvers)):
        botSolvers[i].SetDebug(False)
        botSolvers[i].SolveWord()

        AddSolvedData(botSolvers[i].ReturnAllData(), i)

def WriteSolvedData():
    """Writes the output form solving the wordle"""
    file = open('SolvedWordles.csv', 'w', newline='')
    writer = csv.DictWriter(file, fieldnames=['Game Number', 'Date', 'Solution Word', 'Solved', 'Number Of Guesses', 'Guess 1', 'Guess 2', 'Guess 3', 'Guess 4', 'Guess 5', 'Guess 6'])
    writer.writeheader()
    for data in solvedData:
        writer.writerow({'Game Number':data[0], 'Date':data[1], 'Solution Word':data[2], 'Solved':data[3], 'Number Of Guesses': data[4], 'Guess 1':data[5], 'Guess 2':data[6], 'Guess 3':data[7], 'Guess 4':data[8], 'Guess 5': data[9], 'Guess 6':data[10]})
    file.close()



def WriteFalseData():
    file = open('FailedWords', 'w', newline='')
    writer = csv.DictWriter(file, fieldnames=['Word'])
    writer.writeheader()
    for data in wordsNotSolved:
        writer.writerow({'Word':data})
    file.close()

def AppendSolvedData():

    with open('SolvedWordles.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(solvedData[0])
        file.close()

#def InsertDataIntoDB():

 #   for data in solvedData:
  #      Word.objects.create([Word(date=data[1], word=data[2], numberOfGuesses=data[4], guess1=data[5], guess2=data[6], guess3=data[7], guess4=data[8], guess5=data[9], guess6=data[10])])
        


def SolveLatestWordle():

    global solvedData

    file = open('WordHistoricalData.csv', 'r')
    gameInfo = file.readlines()[-1]
    file.close()

    tempList = [None]*11

    tempString = ''

    for i in range(len(gameInfo)):

        if gameInfo[i] == ',':
            break

        tempString += gameInfo[i]
    
    gameInfo = gameInfo[i+1:]
    tempList[0] = tempString

    tempList[1] = gameInfo[:10]
    gameInfo = gameInfo[11:-1]
    
    tempList[2] = gameInfo.lower()

    solvedData.append(tempList)

    bot = WordleBot(True, tempList[2])

    bot.SolveWord()

    tempList = bot.ReturnAllData()

    AddSolvedData(tempList, 0)

    print(solvedData)

    AppendSolvedData()


    
#list to hold the data related to solving the wordles
solvedData = []

solveAll = True
sumGuessNumbers = 0
averageGuesses = 0
wordsNotSolved = []

if solveAll:



    #Get the raw historical data from file
    f1 = open('WordHistoricalData.csv', 'r')
    historicalData = f1.readlines()
    f1.close()

    historicalData.pop(0)

    #set the index to 0
    currentDataSetIndex = 0


    #create the WordleBots to solve for solutions.
    botSolvers = []




    AddHistoricalDataToSolvedDataSet()

    SolveWordles()

    WriteSolvedData()
    WriteFalseData()

    #InsertDataIntoDB()

else:
    SolveLatestWordle()
    #InsertDataIntoDB()

print(sumGuessNumbers/len(solvedData))
print(str(len(wordsNotSolved)) + "/" + str(len(solvedData)) + '=' + str(len(wordsNotSolved)/len(solvedData))  + ' Fail Percent')
