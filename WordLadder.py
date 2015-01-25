__author__ = 'Cristal Ngo'

from MyQueue import MyQueue
from MyStack import MyStack

dictionary = []

def readFromDictionary(fileName):
    global dictionary

    f = open(fileName, "r")
    for line in f:
        line = line.replace("\n", "", )
        line = line.lower()
        dictionary.append(line)
    dictionary = list(set(dictionary))
    dictionary.sort()
    f.close()

def findWords(firstWord, lastWord):
    global dictionary

    #---------------Enter your source code here----------------#
    #Print a shortest word ladder for the firstWord and lastWord and return 1 if such a ladder can be found
    #Return -1 if there exists no word ladder for the firstWord and lastWord

    usedWords = []
    usedWords.append(firstWord)
    #step 1
    count = 0
    breakFirstWordIntoChars = list(firstWord)
    myQueue = MyQueue()

    for i in range(len(dictionary)):

        if len(dictionary[i]) == len(breakFirstWordIntoChars):
            breakDicObjectIntoChars = list(dictionary[i])
            for j in range(len(breakFirstWordIntoChars)):

                if breakFirstWordIntoChars[j] != breakDicObjectIntoChars[j]:
                    count += 1

            if count == 1 and dictionary[i] not in usedWords:
                myStack = MyStack()
                myStack.push(firstWord)
                myStack.push(dictionary[i])
                usedWords.append(dictionary[i])
                myQueue.enqueue(myStack)


        count = 0


    #step 2
    #print myQueue.size()

    if myQueue.size() > 0:
        count = 0

        while(True):

            if myQueue.isEmpty() is not True:
                firstStack = myQueue.dequeue()
                firstStackWord = firstStack.peek()

                print firstStack.toString()
                if firstStackWord == lastWord:
                    #return firstStack.toString()
                    break
                else:

                    firstStackWordIntoChars = list(firstStackWord)

                    for m in range(len(dictionary)):
                        if len(dictionary[m]) == len(firstStackWordIntoChars):
                            breakDicObjectIntoChars = list(dictionary[m])

                            for n in range(len(firstStackWordIntoChars)):
                                if firstStackWordIntoChars[n] != breakDicObjectIntoChars[n]:
                                    count += 1

                            if count == 1 and dictionary[m] not in usedWords:
                                myStack2 = MyStack()
                                myStack2.copyFrom(firstStack)
                                myStack2.push(dictionary[m])
                                myQueue.enqueue(myStack2)
                                usedWords.append(dictionary[m])

                        count = 0
            else:

                return -1
                break
    else:
        myStack2 = MyStack()
        myStack2.push(firstWord)
        return myStack2.toString()








def returnAllLadders(firstWord, lastWord, length):
    global dictionary

    #---------------Enter your source code here----------------#
    #Print a shortest word ladder for the firstWord and lastWord and return 1 if such a ladder can be found
    #Return -1 if there exists no word ladder for the firstWord and lastWord

    usedWords = []
    usedWords.append(firstWord)
    #step 1
    count = 0
    breakFirstWordIntoChars = list(firstWord)
    myQueue = MyQueue()

    for i in range(len(dictionary)):

        if len(dictionary[i]) == len(breakFirstWordIntoChars):
            breakDicObjectIntoChars = list(dictionary[i])
            for j in range(len(breakFirstWordIntoChars)):

                if breakFirstWordIntoChars[j] != breakDicObjectIntoChars[j]:
                    count += 1

            if count == 1 and dictionary[i] not in usedWords:
                myStack = MyStack()
                myStack.push(firstWord)
                myStack.push(dictionary[i])
                usedWords.append(dictionary[i])
                myQueue.enqueue(myStack)


        count = 0


    #step 2
    #print myQueue.size()


    myQueue2 = MyQueue()
    if myQueue.size() > 0:
        count = 0

        while(True):

            if myQueue.isEmpty() is not True:
                firstStack = myQueue.dequeue()
                firstStackWord = firstStack.peek()
                print myQueue.size()

                print "Dequeue"+str(firstStack.toString())

                if firstStackWord == lastWord and firstStack.size() == length:
                    #print firstStack.toString()
                    myStack3 = MyStack()
                    myStack3.copyFrom(firstStack)
                    myQueue2.enqueue(myStack3)
                else:

                    firstStackWordIntoChars = list(firstStackWord)

                    for m in range(len(dictionary)):
                        if len(dictionary[m]) == len(firstStackWordIntoChars):
                            breakDicObjectIntoChars = list(dictionary[m])

                            for n in range(len(firstStackWordIntoChars)):
                                if firstStackWordIntoChars[n] != breakDicObjectIntoChars[n]:
                                    count += 1

                            if count == 1 and dictionary[m] not in usedWords:
                                myStack2 = MyStack()
                                myStack2.copyFrom(firstStack)
                                myStack2.push(dictionary[m])
                                myQueue.enqueue(myStack2)
                                usedWords.append(dictionary[m])

                        count = 0

                #if firstStack.size() < length:
                #    myQueue.enqueue(firstStack)
            else:
                return myQueue2
                break






def test(firstWord, lastWord):
    result = findWords(firstWord, lastWord)
    if result == -1: print("No Ladder for ", firstWord, "->", lastWord)
    else: print result

def ladderLength(firstWord, lastWord , length):
    result = returnAllLadders(firstWord, lastWord, length)
    while(True):
        if result.isEmpty() is not True:
            returnAllStacks = result.dequeue()
            #print returnAllStacks.toString()
        else:
            break


readFromDictionary('dictionary.txt')
test('stone','money')
test('babies','sleepy')
test('devil','angel')
test('monk','perl')
test('blue','pink')
test('heart','heart')
test('slow', 'fast')
test('atlas','zebra')
test('babes','child')
test('train','bikes')
test('brewing','whiskey')
test('men','can')
#More challenging test cases
test('money','smart')
test('mumbo','ghost')
#No solution test cases
test('snow', 'stop')

#ladderLength('sail', 'ruin', 4)



