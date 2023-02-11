import math


DB = [["A","B", "FG", "C", "D"],
      ["B","G","D"],
      ["B","F","G","BA"],
      ["F","AB","C","D"],
      ["A","BC","G","F","DE"]]
numberOfTransactions = len(DB)
min_support = math.floor(0.4 * numberOfTransactions)
myDict = dict()
# change mySet to one string hold each transaction
for transaction in DB:
    mySet = set()
    for element in transaction:
        for event in element:
            mySet.add(event)
    for event in mySet:
        if event not in myDict:
            myDict[event] = 1
        else:
            myDict[event] += 1
deletedKeys = list()
sizeOfDict = len(myDict)
for key in sorted(myDict):
    if myDict[key] < min_support:
        deletedKeys.append(key)
for key in deletedKeys:
    del myDict[key]
levelOne = []
for key in sorted(myDict):
    levelOne.append(key)


def joinItems(element1, element2):
    resultSequence = list()
    resultSequence.append((element1, element1))
    resultSequence.append((element2, element2))
    resultSequence.append((element1, element2))
    resultSequence.append((element2, element1))
    resultSequence.append((element1 + element2))
    return resultSequence

#(A,A)
uniqueJoinedSet = set()
for i in range(0, len(levelOne)):
    for j in range(i + 1, len(levelOne)):
        returnedSequence = joinItems(levelOne[i], levelOne[j])
        for partial in returnedSequence:
            uniqueJoinedSet.add(partial)
dictSizeTwo = dict()
for pr in uniqueJoinedSet:
    dictSizeTwo[pr] = 0
for element in uniqueJoinedSet:
    if isinstance(element, str):
        for transaction in DB:
            for eachList in transaction:
                if element in eachList:
                    dictSizeTwo[element] += 1
    else:
        for transaction in DB:
            savedIdx = -1
            idx = 0
            sizeOfElement = len(element)
            flagCnt = 0
            for item in element:
                if savedIdx == -1:
                    idx = 0
                else:
                    idx = savedIdx
                whileLen = len(transaction)
                while idx < whileLen:
                    if item in transaction[idx]:
                        savedIdx = idx + 1
                        flagCnt += 1
                        break
                    idx += 1
            if flagCnt == sizeOfElement:
                dictSizeTwo[element] += 1

deletedKeys2 = list()
sizeOfDict2 = len(deletedKeys2)

for key in dictSizeTwo:
    if dictSizeTwo[key] < min_support:
        deletedKeys2.append(key)
for key in deletedKeys2:
    del dictSizeTwo[key]

def joinItems2(element1, element2):
    resultSequence = list()
    resultTuple = ()
    if isinstance(element1, tuple) and isinstance(element2, tuple):
        if element1[-1] == element2[0]:
            resultTuple = element1 + tuple(element2[-1])
    elif isinstance(element1, str) and isinstance(element2, str):
        if element1[-1] == element2[0]:
            resultTuple = element1 + element2[-1]
    elif isinstance(element1, tuple) and isinstance(element2, str):
        if element1[-1] == element2[0]:
            convertedList = list(element1)
            convertedList.pop(len(convertedList) - 1)
            convertedList.append(element2)
            resultTuple = tuple(convertedList)
    elif isinstance(element1, str) and isinstance(element2, tuple):
        if element1[-1] == element2[0]:
            convertedList = [element1, element2[-1]]
            resultTuple = tuple(convertedList)
    return resultTuple
dictSizeThree = dict()

for myTuple in dictSizeTwo:
    for myTuple2 in dictSizeTwo:
        if myTuple == myTuple2 : continue
        returnedTuple = joinItems2(myTuple, myTuple2)
        dictSizeThree[returnedTuple] = 0
del dictSizeThree[()]
# for record in dictSizeThree:
#     print(record, len(dictSizeThree))
for record in dictSizeThree:
    for transaction in DB:
        savedIdx = -1
        idx = 0
        sizeOfElement = len(record)
        flagCnt = 0
        for item in record:
            if savedIdx == -1:
                idx = 0
            else:
                idx = savedIdx
            whileLen = len(transaction)
            while idx < whileLen:
                if item in transaction[idx]:
                    savedIdx = idx + 1
                    flagCnt += 1
                    break
                idx += 1
        if flagCnt == sizeOfElement:
            dictSizeThree[record] += 1

deletedKeys3 = list()
sizeOfDict3 = len(deletedKeys3)

for key in dictSizeThree:
    if dictSizeThree[key] < min_support:
        deletedKeys3.append(key)
for key in deletedKeys3:
    del dictSizeThree[key]
def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str

def joinItems3(element1, element2):
    returnedTuple = ()
    tmpElement1 = convertTuple(element1)
    tmpElement2 = convertTuple(element2)
    firstCondition = tmpElement1[len(tmpElement1) - 2] + tmpElement1[len(tmpElement1) - 1]
    secCondition = tmpElement2[0] + tmpElement2[1]
    if firstCondition == secCondition:
        changedToList = list(element1)
        changedToList.append(element2[-1])
        returnedTuple = tuple(changedToList)
    return returnedTuple
dictSizeFour = dict()
for myTuple in dictSizeThree:
    for myTuple2 in dictSizeThree:
        if myTuple == myTuple2 : continue
        returnedTuple = joinItems3(myTuple, myTuple2)
        dictSizeFour[returnedTuple] = 0
for record in dictSizeFour:
    for transaction in DB:
        savedIdx = -1
        idx = 0
        sizeOfElement = len(record)
        flagCnt = 0
        for item in record:
            if savedIdx == -1:
                idx = 0
            else:
                idx = savedIdx
            whileLen = len(transaction)
            while idx < whileLen:
                if item in transaction[idx]:
                    savedIdx = idx + 1
                    flagCnt += 1
                    break
                idx += 1
        if flagCnt == sizeOfElement:
            dictSizeFour[record] += 1
del dictSizeFour[()]
for record in myDict:
    print(record, myDict[record])
print("-----------------------------------")
for record in dictSizeTwo:
    print(record, dictSizeTwo[record])
print("-----------------------------------")
for record in dictSizeThree:
    print(record, dictSizeThree[record])
print("-----------------------------------")
deletedKeys4 = list()
sizeOfDict4 = len(deletedKeys4)

for key in dictSizeFour:
    if dictSizeFour[key] < min_support:
        deletedKeys4.append(key)
for key in deletedKeys4:
    del dictSizeFour[key]

for record in dictSizeFour:
    print(record, dictSizeFour[record])


