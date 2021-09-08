import math
import random
import time

from questionTemplates import *
from formating import *

def askQuestion(num, score, showAnswer):
  Qs = [
        T0(),  T1(),  T2(),  T3(),  T4(),
        T5(),  T6(),  T7(),  T8(),  T9(),
        T10(), T11(), T12(), T13(), T14(),
        T15(), T16(), T17(), T18(), T19(),
        T20(), T21(), T22(), T23(), T24(),
        T25()]
  [q,a,r] = Qs[num]


  printQuestion(q,a,r,showAnswer)
  correct = False
  firstTry = True
  while (not correct):
    [correct, score] = receiveAnswer(r,score,firstTry)
    firstTry = False

  return score
def receiveAnswer(r,score,firstTry):
  guess = input("Your Guess: ")
  print()
  if (guess.lower() == getAnswerLetter(r) or guess.upper() == getAnswerLetter(r)):
    print('Right!')
    if (firstTry):
        score[0] = score[0] + 1
        score[1] = score[1] + 1
    time.sleep(2)
    return [True, score]
  elif(guess.lower()=='skip'):
    print('Too bad! The answer was ' + getAnswerLetter(r) + '.')
    if (firstTry):
        score[1] = score[1] + 1
    time.sleep(2)
    return [True, score]
  else:
    print('Wrong. Try again? (or \'skip\')')
    if (firstTry):
        score[1] = score[1] + 1
    return [False, score]

def main():
    printLine()
    print('Hello and Welcome to Sam\'s GRE Quant Infinite Question Generator')
    score = newScore()
    questionNum = 1
    printLine()

    while (1>0):
        printQuestionNumber(questionNum)
        score = askQuestion(random.randint(25,25),score,False)
        printScore(score)
        questionNum += 1

if __name__ == "__main__":
    main()
