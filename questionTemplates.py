import math
import random
import time

from formating import *

def T0():
  #Solve for x; one variable
  #Example: If 5x - 22 = 12x - 57, what is the value of x?

  value = random.randint(-15, 15) #Assign value of each side of the eqaulity

  x = random.randint(1, 15) #Assign value of x

  r0 = random.randint(3, 10) #Assign random x coefficeint
  r1 = value - r0*x #Calculate differnce to ensure this side of equality equals value

  r2 = random.randint(2, 10) + random.randint(2, 10) #repeat for other side of equation
  r3 = value - r2*x

  while (r1==r3): #Reassign if x coefficeints are equal
    r2 = random.randint(2, 10) + random.randint(2, 10)
    r3 = value - r2*x

  #Format question
  question = 'If ' + format1(r0,r1) + ' = ' + format1(r2,r3) +', what is the value of x?'

  #Create, format, shuffle wrong answers
  ans = [x+3,2*x, x-1, x/2, x^2, x -2.5]
  for a in ans:
    a = format(a, '.2f')

  #Replace random wrong answer with right one
  replace = random.randint(0, 5)
  ans[replace] = x

  return [question, ans, replace]
def T1():
  #Quant comparison; basic operations; no variables
  #Example: Quant Compare: (2)(6) and 2+6

  #Assign two small random value
  r0 = random.randint(-10, 10)
  r1 = 0
  while (r1 == 0): #Ensure that r1 is not equal to 0
    r1 = random.randint(-10, 10)

  o = random.sample(set([' + ', ' - ', ' * ', ' / ']), 2) #Choose two operations to compare

  a = '(' + str(r0) + ')' + o[0] + '(' + str(r1) + ')' #Format two quantities
  b = '(' + str(r0) + ')' + o[1] + '(' + str(r1) + ')'

  question = formatQuantities(a, b, False) #More formatting

  quants=[0,0]
  for i in range(0,2): #Assign value to answer based on earlier chosen operation
    if (o[i] == ' + '):
      quants[i] = r0+r1
    if (o[i] == ' - '):
      quants[i] = r0-r1
    if (o[i] == ' * '):
      quants[i] = r0*r1
    if (o[i] == ' / '):
      quants[i] = r0/r1

  if (quants[0] > quants[1]): #Calculate correct answer
    rep = 0
  if (quants[0] < quants[1]):
    rep = 1
  if (quants[0] == quants[1]):
    rep = 2

  return [question, quantityAnswers(), rep]
def T2():
    # Quant comparison; multiple inequalities, three variables
    # Example: Quant Compare: f + g + h > 5  -and-  7 > g + h; A = f, B = -5

    #Get random consecutive variable letters
    n = random.randint(0,22)
    v0 = chr(ord('a') + n)
    v1 = chr(ord('a') + n + 1)
    v2 = chr(ord('a') + n + 2)

    c0 = random.randint(-10,10) #Get two random values for other side of inequalities
    c1 = random.randint(-10,10)

    eq0 = v0 + ' + ' + v1 + ' + ' + v2 + ' > ' + str(c0)
    eq1 = str(c1)+ ' > ' + v1 + ' + ' + v2

    a = v0 #Assign two quantites
    b = c0-c1-random.randint(0,5)

    question = eq0 + '  -and-  ' + eq1 + '\n\n' +formatQuantities(a,b,False) #Format question

    return [question, quantityAnswers(), 0]
def T3():
    # Quant comparison; single inequality; three variables
    # Example: b < c < d < -7; A = d + c, B = d - b

    #Get random consecutive variable letters
    n = random.randint(0,22)
    v0 = chr(ord('a') + n)
    v1 = chr(ord('a') + n + 1)
    v2 = chr(ord('a') + n + 2)

    #Random number for oposite side in inequality
    c0 = random.randint(-10,10)

    #Change equation based on value of c0
    if (c0 <= 0):
        eq0 = v0 + ' < ' +  v1 + ' < ' + v2 + ' < ' + str(c0)
    else:
        eq0 = v0 + ' > ' +  v1 + ' > ' + v2 + ' > ' + str(c0)

    #Format quantites
    a = v2 + ' + ' + v1
    b = v2 + ' - ' + v0

    #Format question
    question = eq0 + '\n\n' +formatQuantities(a,b,False)

    #Change answer based on value of c0
    if (c0 <= 0):
        r = 1
    else:
        r = 0

    return [question, quantityAnswers(), r]
def T4():
    ## Quant comparison; fractions with one variable
    ## Example: x > -3; A = 1/(x+1), B = -x/(1-x)

    #Format fractions on multiple lines
    a = '   1  \n -----\n x + 1'
    b = '  -x  \n -----\n 1 - x'

    #Randomly choose value of x
    x = random.choice([-5,-4,-3,-2,2,3,4,5])

    #Randomly choose which way to make equality, then calculate answer choice
    if (random.randint(0,1) == 0):
        eq0 = 'x > ' + str(x)+ '\n\n'
        if (x > 0):
            r = 1
        else:
            r = 3
    else:
        eq0 = 'x < ' + str(x)+ '\n\n'
        if (x > 0):
            r = 3
        else:
            r = 0

    #Format question
    question = eq0 + formatQuantities(a,b,True)

    return [question, quantityAnswers(), r]
def T5():
    ## Quant comparison; fractions with one variable
    ## Example: x > -1; A = 1/x, B = (x+1)/x^2

    #Assign x not equal to 0
    x = 0
    while (x == 0):
        x = random.randint(-5,5)

    #Format fractions for multiple lines
    a = '   1  \n -----\n   x  '
    b = ' x + 1  \n -----\n  x^2'

    #Randomly choose direction of inequality
    if (random.randint(0,1) == 0):
        eq0 = 'x > ' + str(x) + '\n\n'
    else:
        eq0 = 'x < ' + str(x) + '\n\n'

    #Format question
    question = eq0 + formatQuantities(a,b,True)
    return [question, quantityAnswers(), 1]
def T6():
    ## Word problem; simple interest rate
    ## A business owner obtained a $5154.57 loan at a simple annual interest rate
     # of R percent in order to purchase a computer. After one year, the owner made
     # a single payment of $5850.43 to repay the loan, including the interest.
     # What is the value of R?

    #Randomly choose value of interest rate r
    r = round(random.uniform(5, 20),1)

    #Randomly choose loan amount
    l = round(500 * random.uniform(2, 20),2)

    #Randomly choose how many years the grow the loan
    years = random.randint(1,5)

    #Format question
    question = 'A business owner obtained a $' + '{:,.2f}'.format(l) + ' loan at a simple annual interest rate of R percent in order to purchase a car. After ' + str(years) + ' year(s), the owner made a single payment of $' + '{:,.2f}'.format((round(years * l * (r/100) + l,2))) + ' to repay the loan, including the interest. What is the value of R?'

    #Create and format wrong answers
    ans = [r+1.4, r/2, r-2.3, 1.5*r, r+5.4, math.sqrt(r)]
    for i in range(0,len(ans)):
        ans[i] = round(ans[i],1)

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = r

    return [question, ans, replace]
def T7():
    ## Fractions; two variables
    ## Example: If (a-b)/(a+b) = 2 and b = -1, what is the value of a?

    #Randomly choose a not equal to 0
    a = random.choice([-3,-2,-1,1,2,3])

    #Randomly choose b not equal to abs(a)
    b = a
    while (abs(a) == abs(b)):
        b = random.choice([-3,-2,-1,1,2,3])

    #Calculate value of fraction v
    v = (a-b)/(a+b)

    #Format question
    question = '     a-b\nIf  ----- = ' + str(round(v,4)) + ' and b = ' + str(b) + ', what is the value of a?\n     a+b'

    #Create and format wrong answers
    ans = [a+1,a-2,a-0.5,a*2,-1*a,a/3]
    for i in range(0,len(ans)):
        ans[i] = round(ans[i],4)

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = a

    return [question, ans, replace]
def T8():
    ## Word problem; ratios
    ## Example: At Company R, the ratio of female employees to the number of male
     # employees is 2 to 7. If there are 700 female employees at the company, how
     # many male employees are there at the company?

    #Randomly choose company name
    n = random.randint(0,24)
    c = chr(ord('A') + n)

    #Randomly choose ratio and ensure a not equal to b
    a = random.randint(1,10)
    b = a
    while (a == b ):
        b = random.randint(1,10)

    #Reduce ratio
    [a,b] = reduceFrac(a, b)

    #Format numbers
    a = int(a)
    b = int(b)

    #Randomly choose number of female employees
    e = random.randint(1,20)*50

    #Format question
    question = 'At Company ' + str(c) + ', the ratio of female employees to the number of male employees is ' + str(a) + ' to ' + str(b) + '. If there are ' + str(e) + ' female employees at the company, how many male employees are there at the company?'

    #Create and format wrong answers
    ans = [(e*b)/(a+b), (e*b)/(2*a), (e*a)/b, e/(b*a), (e*1.5*b)/a, (100*a)/b]
    for i in range(0,len(ans)):
        ans[i] = int(round(ans[i],0))

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = int(round(e*b/a,0))

    return [question, ans, replace]
def T9():
    ## Word problem; simple arithmetic
    ## The floor space at a convention center is rented for $27 per 30 square feet
     # for one day. In the convention center, Alice rented a rectangular floor space
     # that measured 5 feet by 21 feet, and Betty rented a rectangular floor space
     # that measured 30 feet by 9 feet. If each person rented their floor space
     # for one day, how much more did Betty pay than Alice?

    #Randomly choose price for each area
    price = random.randint(5,50)
    amount = 5 * random.randint(5,10)

    #Randomly choose area for person 1
    dim0 = random.randint(5,30)
    dim1 = random.randint(5,30)

    #Calculate areas
    area0 = dim0 * dim1
    area1 = 0

    #Randomly choose person 2 area which is more than person 1's
    while (area1 < area0):
        dim2 = random.randint(5,30)
        dim3 = random.randint(5,30)
        area1 = dim2 * dim3

    #Format question
    question = 'The floor space at a convention center is rented for $' + str(price) + ' per ' + str(amount) + ' square feet for one day. In the convention center, Alice rented a rectangular floor space that measured ' + str(dim0) + ' feet by ' + str(dim1) + ' feet, and Betty rented a rectangular floor space that measured ' + str(dim2) + ' feet by ' + str(dim3) + ' feet. If each person rented their floor space for one day, how much more did Betty pay than Alice?'

    #Create and format wrong answers
    ans = [price*(area1 - area0), amount*(area1 - area0), (price*area1)/amount, (price*area0)/amount, price*(area1 - area0)/(2*amount), amount*(area1 - area0)/price]
    for i in range(0,len(ans)):
        ans[i] = '$' + "{:.2f}".format(ans[i])

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = '$' + "{:.2f}".format(price*(area1 - area0)/amount)

    return [question,ans,replace]
def T10():
    ## Arithmetic means, basic arithmetic
    ## List S: 4, y, z; List T: 1, 6, 9, y, z; If the average (arithmetic mean)
     # of List S is 23/3, what is the average of List T?

    #Randomly choose letters for lists
    n = random.randint(0,24)
    l0 = chr(ord('A') + n)
    l1 = chr(ord('A') + n + 1)

    #Randomly choose value of summed variables
    v = random.randint(10,30)

    #Choose first value of List 1
    n0 = random.randint(1,10)

    #Randomly choose letters for variables
    a = random.randint(0,24)
    n1 = chr(ord('a') + a)
    n2 = chr(ord('a') + a + 1)

    #Choose values for list 2 in increading order
    m0 = random.randint(1,5)
    m1 = random.randint(m0+1, 9)
    m2 = random.randint(m1+1, 10)

    #Ensure the fraction is irreducible
    while ((v+n0)%3==0):
        v = random.randint(10,30)

    #Format lists
    L0 = 'List ' + str(l0) + ': ' + str(n0) + ', ' + str(n1) + ', ' + str(n2)
    L1 = 'List ' + str(l1) + ': ' + str(m0) + ', ' + str(m1) + ', ' + str(m2)+ ', ' + str(n1) + ', ' + str(n2)

    #Format question
    question = L0 + '\n' + L1 + '\n\nIf the average (arithmetic mean) of List ' + str(l0) + ' is ' + str(v+n0) + '/3, what is the average of List ' + str(l1) + '?'

    #Create and format wrong answers
    ans = [v*5, v, v+m0+m1, 5*(v+m0+m1+m2), m0+m1+m2, 2+v+m0+m1+m2]
    for i in range(0,len(ans)):
        ans[i] = ans[i]/5

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = (v + m0 + m1 + m2)/5

    return[question, ans, replace]
def T11():
    ## Exponent rules
    ## If (125)[5^(6x)] = 5^n, where n and x are integers, what is the value of
     # n in terms of x?

    #Choose values of exponents and base
    e2 = random.randint(2,3)
    b = e2
    while (b==e2):
        b = random.randint(2,5)
    e1 = random.randint(6,10)

    #Format question
    question = 'If (' + str(b**e2) + ')[' + str(b) + '^(' + str(e1) + 'x)] = ' + str(b) + '^n, where n and x are integers, what is the value of n in terms of x?'

    #Create and format wrong answers
    ans = [str(e1) + ' + ' + str(e2) + 'x',str(e1) + ' + ' + str(e1) + 'x',str(b) + ' + ' + str(e1) + 'x', str(b) + 'x', str(b-1) + ' + ' + str(e2) + 'x',str(e1) + 'x']

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = str(e2) + ' + ' + str(e1) + 'x'

    return [question, ans, replace]
def T12():
    ## Median calclations of whole numbers
     # Test Scores: [94, 87, 79, 98, 89, 89, 66, 96, 86, 73]
     # What is the median test score of the 10-student class?

    #Add test scores to array
    nums = []
    for i in range (0,10):
        nums.append(random.randint(60,99))

    #Format question
    question = 'Test Scores: ' + str(nums) + '\n\nWhat is the median test score of the 10-student class?'

    #Sort array to calculate median
    nums.sort()
    median = (nums[4]+nums[5])/2

    #Create and format wrong answers
    ans = [nums[4], round(sum(nums)/len(nums),1),nums[5],median+2,int(median/2),'There is no median.']
    for i in range(0,4):
        ans[i] = '{0:g}'.format(ans[i])

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = '{0:g}'.format(median)

    return [question,ans,replace]
def T13():
## Sum-totaling chart dealio? IDK the name
 # In a certain voting district there are 448 registered voters. Of these voters,
  # 238 of them were women, and 202 of them were from minority groups. If 4/7 of
  # the women are from minority groups, how many of the voters are neither women
  # nor from a minority group?

    #Randomly choose group size of each two characteristic combo
    AZ = 6 * random.randint(3,40)
    AX = 6 * random.randint(3,40)
    BZ = 6 * random.randint(3,40)
    #Except for minority women which is a random (from set) fraction of total women
    BX = BZ * random.choice([3/2,5/2,4/3,5/3,5/4])

    #Calculte totals of each group
    A = AZ + AX
    B = BZ + BX
    Z = AZ + BZ
    X = AX + BX

    #Check if adding aligns to total
    try:
        A+B == Z+X
    except:
        print('adding error')

    #Calculate total
    total = int(A+B)

    #Reduce fraction of minority women out of women
    [f0,f1] = reduceFrac(BX, B)

    #Format question
    question = 'In a certain voting district there are ' + str(total) + ' registered voters. Of these voters, ' + str(int(B)) + ' of them were women, and ' + str(int(X)) + ' of them were from minority groups. If ' + str(int(f0)) + '/' + str(int(f1)) + ' of the women are from minority groups, how many of the voters are neither women nor from a minority group?'

    #Create and format wrong answers
    ans = [A,BX,AX,BZ,B,BX,Z]
    for i in range(0,len(ans)):
        ans[i] = int(ans[i])

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = AZ

    return [question, ans, replace]
def T14():
    ## Prime facorization; exponent rules; divisibility
     # If an integer is divisible by both 30 and 27, then the integer also must
     # be divisible by which of the following...

    #Randomly choose prime factors from set to create two non-equal numbers
    primes0 = random.choices([2,2,2,2,3,3,5,5],k=3)
    primes0.sort()

    num0 = multiply(primes0)
    num1 = num0

    #Ensure they are not equal
    while (num0==num1):
        primes1 = random.choices([2,2,2,2,3,3,5,5],k=3)
        num1 = multiply(primes1)

    #Append prime factors to create their product
    Primes = primes0 + primes1
    Primes.sort()
    Num = multiply(Primes)

    #Count number of each prime factor
    Twos = Primes.count(2)
    Threes = Primes.count(3)
    Fives = Primes.count(5)

    #Create and format wrong answers
    ans = []

    ran2 = random.randint(0,Twos)
    ran3 = random.randint(0,Threes)
    ran5 = random.randint(0,Fives)

    ans.append(multSpecial([Twos+1,ran3,ran5]))
    ans.append(multSpecial([ran2,Threes+1,ran5]))
    ans.append(multSpecial([ran2,ran3,Fives+1]))
    ans.append(multSpecial([Twos+2,ran3,ran5]))
    ans.append(multSpecial([Twos+1,Threes+1,ran5]))
    ans.append(multSpecial([Twos+1,ran3,Fives+1]))

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = multSpecial([Twos-1,Threes,Fives])

    question = 'If an integer is divisible by both ' + str(num0) + ' and ' + str(num1) + ', then the integer also must be divisible by which of the following'

    return [question,ans,replace]
def T15():
    s = random.randint(5,100)
    question = 'If an object travels at ' + str(s) + ' feet per second, how many feet does it travel in one hour?'

    #Create and format wrong answers
    ans = [s*60, s*60*24, s*30*30, s*60*60/2, s*1000, 5280]
    for i in range(0,len(ans)):
        ans[i] = '{:,.0f}'.format(int(ans[i]))

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = '{:,.0f}'.format(int(s*60*60))

    return [question, ans, replace]
def T16():
    m = random.randint(6,14)
    b = random.randint(11,20)

    sum = 0
    for i in range(1,b):
        sum += m*i
    avg = sum/(b-1)

    #Create and format wrong answers
    ans = [avg + (3*m/b), avg - (3*m/b), m*b, avg+m, avg-b, 2*avg]
    for i in range(0,len(ans)):
        ans[i] = int(ans[i])

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = int(avg)

    question = 'What is the average (arithmetic mean) of all the multiples of ' + str(m) + ' from ' + str(m) + ' to ' + str(m*(b-1)) + ' inclusive?'

    return [question, ans, replace]
def T17():
    w = random.randint(10,30)

    l = random.randint(3,10)
    factor = random.randint(2,5)

    question = 'A cubical block of metal weighs ' + str(w) + ' pounds and has a side length of ' + str(l) + ' feet. How much will another cube with a side length of ' + str(factor*l) + ' feet and made of the same metal weigh?'

    #Create and format wrong answers
    ans = [w * factor**2, w * factor**4, factor**3, w**3, w**2 * factor**2, 6*w]
    for i in range(0,len(ans)):
        ans[i] = '{:,.0f}'.format(int(ans[i])) + ' lbs.'

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = '{:,.0f}'.format(int(w * factor**3)) + ' lbs.'

    return [question, ans, replace]
def T18():
    g0 = random.randint(30,60)
    g1 = random.randint(30,60)
    both = random.randint(10,30)
    neither = random.randint(10,30)

    total = g0 + g1 + both + neither

    question = 'In a class of ' + str(total) + ' students '+ str(g0+both) + ' are taking French, ' + str(g1+both) + ' are taking German. Of the students taking French or German, ' + str(both) + ' are taking both courses. How many students are not enrolled in either course?'

    #Create and format wrong answers
    ans = [total-g0-g1-2*min(both,neither), total-g1-2*both, total-g0-2*both, total-3*neither, total-g0-g1, total-5*neither  ]
    for i in range(0,len(ans)):
        ans[i] = int(abs(ans[i]))

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = neither

    return [question,ans,replace]
def T19():
    base = random.randint(2,9)
    exp0 = random.randint(5,100)
    exp1 = random.randint(5,100)

    question = '(' + str(base) + '^' + str(exp0) + ')' + '(' + str(base) + '^' + str(exp1) + ') = '

    #Create and format wrong answers
    ans = [str(base) + '^' + str(exp0*exp1), str(base) + '^' + str(int((exp0+exp1)/2)),str(base**2) + '^' + str(exp0), str(base*exp1) + '^' + str(exp0), str(base) + '^' + str(exp0*base), str(base) + '^' + str(base*exp1)]

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = str(base) + '^' + str(exp0+exp1)

    return [question, ans, replace]
def T20():
    rateLarge = random.randint(2,5)
    rateSmall = random.randint(20,50)

    hours = 2*random.randint(2,5)

    largeFactor = 2*random.randint(3,25)
    smallFactor = 2*random.randint(3,25)

    largeNeeded = rateLarge * largeFactor
    smallNeeded = rateSmall * smallFactor

    helpers = round((largeFactor + smallFactor) / hours,0)

    question = 'Helpers are needed to prepare for the party. Each helper can make either ' + str(rateLarge) + ' regular cakes or ' + str(rateSmall)+ ' cupcakes per hour. The kitchen is available for ' + str(hours) + ' hours and ' + str(largeNeeded) + ' regular cakes and ' + str(smallNeeded) + ' cupcakes are needed. How many helpers are required?'

    #Create and format wrong answers
    ans = [largeFactor+smallFactor, largeFactor/hours, smallFactor/hours, (largeNeeded+smallNeeded)/hours, helpers*2, helpers/2]
    for i in range(0,len(ans)):
        ans[i] = int(abs(ans[i]))

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = int(helpers)

    return [question, ans, replace]
def T21():
    num = random.randint(20,60)

    question = 'What is the sum of all integers x, such that -' + str(num+2) + ' < x ≤ ' + str(num) + '?'
    ans = [num-2, -num-2, num, -num, num-1, 2*num+1]

    #Replace random wrong answer with right one
    replace = random.randint(0, 5)
    ans[replace] = -num-1

    return [question, ans, replace]
def T22():
    nums = random.sample(range(2,10),4)

    choices = random.sample(range(2,10),4)
    a = str(choices[0]) + 'a + ' + str(choices[1]) + 'b'
    b = str(choices[2]) + 'c + ' + str(choices[3]) + 'd'

    A = nums[0]*choices[0] + nums[1]*choices[1]
    B = nums[2]*choices[2] + nums[3]*choices[3]

    question = 'a, b, c, and d are positive.\n\n(a/'+str(nums[0])+') + (b/'+str(nums[1])+') = (c/'+str(nums[2])+') + (d/'+str(nums[3])+')'+ '\n\n' +formatQuantities(a,b,False)

    if A > B:
        r = 0
    elif B > A:
        r = 1
    elif A == B:
        r = 2

    return [question, quantityAnswers(), r]
def T23():
    factor = random.randint(2,6)
    hours = random.choice([12,18,24,36,48])

    question = 'Beth can paint a house ' + str(factor) + ' times faster than Alice can. If, working together, it takes Alice and Beth ' + str(hours) + ' hours to paint a house, then how many hours would it take Beth to paint the house alone?'
    ans = [hours, hours*factor, hours*factor-1, hours*(factor+1), hours/factor, hours/(factor-1)]

    replace = random.randint(0, 5)
    ans[replace] = (hours*(factor+1))/factor

    return [question, ans, replace]
def T24():
    p = random.randint(10,99)
    n = random.randint(2,10)

    question = 'What percent of ' + str(p) + ' is ' + str(p) + ' percent of ' + str(n) + '?'
    ans = [n*p/1000, n*p/100, n*p/10, p, n*p, n*p*10]

    replace = random.randint(0, 5)
    ans[replace] = n

    key = 'x% of y == y% of x'

    return [question, ans, replace]
def T25():
    primes = [i for i in range(20,100) if isPrime(i)]
    candies = random.choice(primes)

    div = random.sample([2,3,5,7],2);
    div.append(random.choice([11,13]));

    question = 'Marge has n candies, where n is an integer such that 20 < n < \
50. If Marge divides the candies equally among ' +str(div[0])+ ' children, she \
will have ' +str(candies%div[0])+ ' candies remaining. If she divides the \
candies among ' +str(div[1])+ ' children, she will have ' +str(candies%div[1])+ \
' candies remaining. How many candies will remain if she divides the candies \
among ' +str(div[2])+ ' children?';
    ans = [0,candies%div[0],candies%div[1],candies,div[0]*div[1],div[2]];

    replace = random.randint(0, 5);
    ans[replace] = candies%div[2];

    return [question, ans, replace]

def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1


def multSpecial(num):
    n = 1
    for i in range(0,num[0]):
        n *= 2
    for i in range(0,num[1]):
        n *= 3
    for i in range(0,num[2]):
        n *= 5

    return n
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
def reduceFrac(n, d):
    def gcd(n, d):
        while d != 0:
            t = d
            d = n%d
            n = t
        return n
    greatest=gcd(n,d)
    n/=greatest
    d/=greatest
    return [n, d]
