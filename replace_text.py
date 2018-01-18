def replacer(theString, wordsToRepalce =[], wordsThatWillReplace=[]):
    __inputDataValidator(theString, wordsToRepalce, wordsThatWillReplace)
    __checkForDplicatedValuesInList(wordsToRepalce)
    stringList= __convertStringToList(theString)
    booleanFlag = __checkIfListsAreEqual(wordsToRepalce, wordsThatWillReplace)
    mappedValues = __mapWordsToBeReplaced(wordsToRepalce, wordsThatWillReplace)
    listChangedWords=[]
    for x in stringList[:]:
        if x in mappedValues:
            listChangedWords.append(x)
            placeInList = stringList.index(x)
            stringList[placeInList] = mappedValues[x]
    if booleanFlag == False:
        return __zipAnswer(theString, booleanFlag, "List lengths do not match")
    else:
        return __zipAnswer(__convertTheListToString(stringList), booleanFlag, __messageBuilder(listChangedWords, wordsToRepalce))

def __checkForDplicatedValuesInList(theList= []):
    setList = __removeDuplicates(theList)
    if len(setList) != len(theList):
        raise ValueError('List words to change contains duplicate values, this is not logical')

def __inputDataValidator(theString, wordsToRepalce =[], wordsThatWillReplace=[]):
    if ((isinstance(theString, str) == False) or theString==""):
        raise ValueError('Wrong Input Data')
    for arg in wordsToRepalce:
        if ((isinstance(arg, str) == False) or arg==""):
            raise ValueError('Wrong Input Data')
    for arg in wordsThatWillReplace:
        if (isinstance(arg, str) == False):
            raise ValueError('Wrong Input Data')

def __convertStringToList(theString):
    return theString.split(",")

def __mapWordsToBeReplaced(wordsToRepalce=[], wordsThatWillReplace=[]):
    return dict(zip(wordsToRepalce, wordsThatWillReplace))

def __convertTheListToString(theList=[]):
    joiner = ','
    return joiner.join(theList)

def __checkIfListsAreEqual(wordsToRepalce =[], wordsThatWillReplace=[]):
    if len(wordsToRepalce) == len(wordsThatWillReplace):
        return True
    else:
        return False

def __zipAnswer(*args):
    answer =[]
    for arg in args:
        answer.append(arg)
    return answer

def __removeDuplicates(imputList):
    return list(sorted(set(imputList),key=imputList.index))

def __messageBuilder(listChangedWords=[], listAllWords=[]):
    singleChangedWords= __removeDuplicates(listChangedWords)
    messages = []
    message=""
    for word in singleChangedWords:
        occurance = 0
        for i in range(0,len(listChangedWords),1):
            if listChangedWords[i] == word:
                occurance = occurance + 1
        if occurance >1:
            messages.append(word +": replaced "+ str(occurance)+" times")
        elif occurance == 1:
            messages.append(word +": replaced "+ str(occurance)+" time")
    for word in listAllWords:
        if singleChangedWords.__contains__(word)==False:
            messages.append(word +": replaced "+"0"+" times")
    return message.join(messages)
