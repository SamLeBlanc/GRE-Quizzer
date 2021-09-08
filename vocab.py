import csv
import numpy as np
from numpy import genfromtxt
import datetime
today = datetime.date.today()

from formating import *

import random

def printInfo(data, row, word, part, deff):
    string = ''
    if word:
        string = data[row][0] + '\n'
    if part:
        string = string + data[row][1] + '\n'
    if deff:
        string = string + data[row][2] + '\n'
    print(string)

def printArray(arr):
    for row in range(0,len(arr)):
        print(arr[row])

def updateScores(mark, num, careerScores, sessionScores):
    if int(mark) == 1:
        careerScores[num][1] += 1
        sessionScores[1] += 1
    if int(mark) == 2:
        careerScores[num][0] += 0.5
        careerScores[num][1] += 1
    if int(mark) == 3:
        careerScores[num][0] += 1
        careerScores[num][1] += 1
        sessionScores[0] += 1
        sessionScores[1] += 1
    return careerScores, sessionScores

def multChoice(data, num, pickFrom, qNum):
    print('Question ' + str(qNum) + ':')
    print()
    if pickFrom == 0:
        print('Match the following -word- to its corresponding definition:')
        print('--' + data[num][pickFrom] + '--')
        printLine()
    if pickFrom == 1:
        print('Match the following -definition- to its corresponding word:')
        print('--' + data[num][pickFrom] + '--')
        printLine()

    choices = random.sample(range(30,60),6)
    if num in choices:
        choices.remove(num)
    else:
        choices.remove(choices[5])

    replace = random.randint(0, 4)
    choices[replace] = num

    for i in range(0,5):
        print(chr(ord('A') + i) + ': ' + data[choices[i]][abs(pickFrom-1)])

    return replace

def getAnswerLetter(num):
  if num==0:
    return 'A'
  if num==1:
    return 'B'
  if num==2:
    return 'C'
  if num==3:
    return 'D'
  if num==4:
    return 'E'
  if num==5:
    return 'F'

def printIntro():
    printLine()
    print('Hello and Welcome to Sam\'s GRE Verbal Reasoning Study Center')
    printLine()
    print()
    game = input('What would you like to do?\n\n0: Learn\n1: Guess definition from words\n2: Guess word from definitions\n\nYour choice: ')
    print()
    return game

def printScores(num, careerScores, sessionScores):
    printLine()
    print('Today\'s score: ' + str(sessionScores[0]) + '/' + str(sessionScores[1]) + ' or ' + str(round(100*sessionScores[0]/sessionScores[1],1)) + '%')
    print('Career score for -' + str(data[num][0]) + '-: ' + str(careerScores[num][0]) + '/' + str(careerScores[num][1])+ ' or ' + str(round(100*careerScores[num][0]/careerScores[num][1],1)) + '%')

def chooseRandomWord(data):
    return random.randint(0,len(data)-1)

def acceptGuess():
    return input('\nYour guess: ')

def getMark(guess, answer):
    if guess.upper() == getAnswerLetter(answer):
        print('Correct!')
        return 3
    else:
        print('Wrong! The answer was ' + str(getAnswerLetter(answer)) + '.')
        return 1

def learnWords(wordIndex):
    print('--' + data[wordIndex][0].upper() + '--')
    input()
    print(data[wordIndex][1])
    print()
    return input('1: No idea...\n2: Kinda?\n3: Knew it!\n\n')

with open('words.csv', newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)

careerScores = genfromtxt('scores.csv', delimiter=',')

game = printIntro()
game = int(game)-1
sessionScores = [0,0]
continuous = True
qNum = 1
wordOrder = random.sample(range(30,60),30)
while continuous:
    wordIndex = wordOrder[qNum-1]
    printLine()
    if game == -1:
        mark = learnWords(wordIndex)
    else:
        answer = multChoice(data, wordIndex, game, qNum)
        guess = acceptGuess()
        print()

        if guess.lower() == 'end':
            continuous = False
        else:
            mark = getMark(guess, answer)
    [careerScores, sessionScores] = updateScores(mark, wordIndex, careerScores, sessionScores)

    print()
    time.sleep(1)
    printScores(wordIndex, careerScores, sessionScores)
    qNum += 1

    np.round(careerScores,1)
    np.savetxt('scores.csv', careerScores, delimiter=',')
    np.savetxt('scores' + today.strftime('%b%d%Y') + '.csv', careerScores, delimiter=',')

### FIX: when program ends, it marks last answer as correct


    #printArray(scores)
