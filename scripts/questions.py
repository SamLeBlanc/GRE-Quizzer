import math
import random
from decimal import Decimal

def format1(r1,r2):
  if (r2>0):
    return (str(r1) + 'x + ' + str(r2))
  if (r2<0):
    return (str(r1) + 'x - ' + str(abs(r2)))

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

def printQuestion(q,a,r):
  print()
  print(q)
  print()
  for i in range (0,len(a)):
    print(chr(ord('A') + i) + ': ' + str(a[i]))
    
  print('Answer: ' + getAnswerLetter(r))
  
def receiveAnswer(r):
  guess = input("Your Guess: ")
  print()
  if (guess==getAnswerLetter(r)):
    print('Right!')
    return True
  elif(guess=='skip'):
    print('Too bad! The answer was ' + getAnswerLetter(r))
    return True
  else:
    print('Wrong. Try again? (or \'skip\')')
    return False

def style0():
  #Solve for x; one variable
  #Example: If 5x - 22 = 12x - 57, what is the value of x?

  value = random.randint(-15, 15) #Assign value of each side of the eqaulity

  x = random.randint(1, 15) #Assign value of x

  r0 = random.randint(3, 10) #Assign random x coefficeint 
  r1 = value - r0*x #Calculate differnce to ensure sides of equaltion equals value

  r2 = random.randint(2, 10) + random.randint(2, 10) #repeat for other side of equation
  r3 = value - r2*x

  while (r1==r3): #Reassign if coefficeints are equal
    r2 = random.randint(2, 10) + random.randint(2, 10)
    r3 = value - r2*x

  #Format question
  question = 'If ' + format1(r0,r1) + ' = ' + format1(r2,r3) +', what is the value of x?'

  #Create and format wrong answers
  ans = [x+3,2*x, x-1, x/2, x^2, x -2.5]
  for a in ans:
    a = format(a, '.2f')

  #Replace random fake answer with real one
  replace = random.randint(0, 5)
  ans[replace] = x

  return [question, ans, replace]

def style1():
  #Quant comparison; basic operations; no variables
  #Example: Quant Compare: (2)(6) and 2+6

  #Assign two small random value
  r0 = random.randint(-10, 10)
  r1 = random.randint(-10, 10)
 
  o = random.sample(set([' + ', ' - ', ' * ', ' / ']), 2)
  
  question = 'Quantity A: ' + '(' + str(r0) + ')' + o[0] + '(' + str(r1) + ')' + '\nQuantity B: ' + '(' + str(r0) + ')' + o[1] + '(' + str(r1) + ')'

  ans = ['Quantity A is greater', 'Quantity B is greater', 'The two quantities are equal', 'The relationship cannot be determined']

  quants=[0,0]
  for i in range(0,2):
    if (o[i] == ' + '):
      quants[i] = r0+r1
    if (o[i] == ' - '):
      quants[i] = r0-r1
    if (o[i] == ' * '):
      quants[i] = r0*r1
    if (o[i] == ' / '):
      quants[i] = r0/r1

  if (quants[0] > quants[1]):
    rep = 0
  if (quants[0] < quants[1]):
    rep = 1
  if (quants[0] == quants[1]):
    rep = 2

  return [question, ans, rep]
  
def askQuestion(num):
  if (num == 0):
    [q,a,r] = style0()
  elif (num ==1):
    [q,a,r] = style1()
  else:
    print('invalid question number')
    return

  printQuestion(q,a,r)  
  correct = False
  while (not correct):
    correct = receiveAnswer(r)

askQuestion(0)
askQuestion(1)



