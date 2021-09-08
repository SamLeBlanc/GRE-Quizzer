import math
import random
import time

def format1(r1,r2):
  if (r2>0):
    return (str(r1) + 'x + ' + str(r2))
  if (r2<0):
    return (str(r1) + 'x - ' + str(abs(r2)))

def printLine():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def printScore(score):
    print()
    printLine()
    print('Current score is ' + str(score[0]) + '/' + str(score[1]) + ', or ' + str(round(100*(score[0]/score[1]),1)) + '%.' )
    printLine()

def formatQuantities(a, b, newLine):
    quants = [str(a),str(b)]
    if newLine:
        return 'Quantity A:\n' + quants[0] + '\n\nQuantity B:\n' + quants[1]
    else:
        return 'Quantity A: ' + quants[0] + '\nQuantity B: ' + quants[1]

def quantityAnswers():
    return ['Quantity A is greater', 'Quantity B is greater', 'The two quantities are equal', 'The relationship cannot be determined']

def printQuestionNumber(qNum):
    print('Question ' + str(qNum) + ':')

def newScore():
    return [0,0]

def printQuestion(q,a,r,showAnswer):
  print()
  print(q)
  print()
  for i in range (0,len(a)):
    print(chr(ord('A') + i) + ': ' + str(a[i]))

  print()
  if showAnswer:
      print('Answer: ' + getAnswerLetter(r))

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
