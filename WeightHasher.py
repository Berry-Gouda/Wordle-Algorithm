#This is the algo to make the hash map of weights for which letter is most probable based on the
#letters that we know.
#
#Format <letter known><letter known position><position before:after 0:1><surrounding letter>
#




import FileWriter
import BotData


def add_element(dic, key):
    if key not in dic:
        dic[key] = 1
    else:
        dic[key] += 1


LetterWeights = {}
aWeights = {}
bWeights = {}
cWeights = {}
dWeights = {}
eWeights = {}
fWeights = {}
gWeights = {}
hWeights = {}
iWeights = {}
jWeights = {}
kWeights = {}
lWeights = {}
mWeights = {}
nWeights = {}
oWeights = {}
pWeights = {}
qWeights = {}
rWeights = {}
sWeights = {}
tWeights = {}
uWeights = {}
vWeights = {}
wWeights = {}
xWeights = {}
yWeights = {}
zWeights = {}

for i in range(len(BotData.TotalDictionary)):

    
    currentWord = BotData.TotalDictionary[i]

    for j in range(len(currentWord)):

        keyString = ''

        if j - 1 >= 0:
            keyString = currentWord[j] + str(j)
            keyString = keyString + '0' + currentWord[j-1]
            add_element(LetterWeights, keyString)


        if j + 1 < len(currentWord):
            keyString = currentWord[j] + str(j)
            keyString = keyString + '1' + currentWord[j+1]
            add_element(LetterWeights, keyString)

# for k in LetterWeights:
#    if k[0] == 'a':
#         aWeights[k] = LetterWeights[k]
#     if k[0] == 'b':
#         bWeights[k] = LetterWeights[k]
#     if k[0] == 'c':
#        cWeights[k] = LetterWeights[k]
#     if k[0] == 'd':
#         dWeights[k] = LetterWeights[k]
#     if k[0] == 'e':
#         eWeights[k] = LetterWeights[k]
#     if k[0] == 'f':
#         fWeights[k] = LetterWeights[k]
#     if k[0] == 'g':
#         gWeights[k] = LetterWeights[k]
#     if k[0] == 'h':
#         hWeights[k] = LetterWeights[k]
#     if k[0] == 'i':
#         iWeights[k] = LetterWeights[k]
#     if k[0] == 'j':
#         jWeights[k] = LetterWeights[k]
#     if k[0] == 'k':
#         kWeights[k] = LetterWeights[k]
#     if k[0] == 'l':
#         lWeights[k] = LetterWeights[k]
#     if k[0] == 'm':
#         mWeights[k] = LetterWeights[k]
#     if k[0] == 'n':
#         nWeights[k] = LetterWeights[k]
#     if k[0] == 'o':
#         oWeights[k] = LetterWeights[k]
#     if k[0] == 'p':
#         pWeights[k] = LetterWeights[k]
#     if k[0] == 'q':
#         qWeights[k] = LetterWeights[k]
#     if k[0] == 'r':
#         rWeights[k] = LetterWeights[k]
#     if k[0] == 's':
#         sWeights[k] = LetterWeights[k]
#     if k[0] == 't':
#         tWeights[k] = LetterWeights[k]
#     if k[0] == 'u':
#         uWeights[k] = LetterWeights[k]
#     if k[0] == 'v':
#         vWeights[k] = LetterWeights[k]
#     if k[0] == 'w':
#         wWeights[k] = LetterWeights[k]
#     if k[0] == 'x':
#         xWeights[k] = LetterWeights[k]
#     if k[0] == 'y':
#         yWeights[k] = LetterWeights[k]
#     if k[0] == 'z':
#         zWeights[k] = LetterWeights[k]


# codeToWrite = 'aWeights = {'
# for k in aWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(aWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'bWeights = {'
# for k in bWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(bWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'cWeights = {'
# for k in cWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(cWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'dWeights = {'
# for k in dWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(dWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'eWeights = {'
# for k in eWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(eWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'fWeights = {'
# for k in fWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(fWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'gWeights = {'
# for k in gWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(gWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'hWeights = {'
# for k in hWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(hWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'iWeights = {'
# for k in iWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(iWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'jWeights = {'
# for k in jWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(jWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'kWeights = {'
# for k in kWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(kWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'lWeights = {'
# for k in lWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(lWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'mWeights = {'
# for k in mWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(mWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'nWeights = {'
# for k in nWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(nWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'oWeights = {'
# for k in oWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(oWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'pWeights = {'
# for k in pWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(pWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'qWeights = {'
# for k in qWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(qWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'rWeights = {'
# for k in rWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(rWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'sWeights = {'
# for k in sWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(sWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'tWeights = {'
# for k in tWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(tWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'uWeights = {'
# for k in uWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(uWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'vWeights = {'
# for k in vWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(vWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'wWeights = {'
# for k in wWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(wWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'xWeights = {'
# for k in xWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(xWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'yWeights = {'
# for k in yWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(yWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

# codeToWrite = 'zWeights = {'
# for k in zWeights:
#     codeToWrite += '\'' + k +'\''  + ":" + str(zWeights[k]) + ','
# codeToWrite += '}'
# FileWriter.AppendToFile(codeToWrite, './BotData.py')

codeToWrite = 'TotalWeights = {'
for k in LetterWeights:
    codeToWrite += '\'' + k +'\''  + ":" + str(LetterWeights[k]) + ','
codeToWrite += '}'
FileWriter.AppendToFile(codeToWrite, './BotData.py')
