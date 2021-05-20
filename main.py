'''
04/19/2021

Review

Function 

def FunctionName(PARAMETERS):
  BODY
  return(optional)



# list if user numbers
numbers = []

def getNumbers():
  userNumber = input("Enter a number or 'q' to quit: ")

  while (userNumber != 'q'):
    numbers.append(int(userNumber))
    userNumber = input("Enter a number or 'q' to quit: ")

getNumbers()

def sum(numberList):
  total = 0

  for i in numberList:
    total += i 
  print("The sum total is " + str(total))

sum(numbers)

#def product(numberList):
def product(numberList):
  total = 1

  for i in numberList:
    total *= i 
  print("The product total is " + str(total))

product(numbers)


# Warm up 2- Fahrenheit to Celcius Conversion
# (F - 32) * 5/9 = C

# Function
def temperature(F):
  C=(F-32) * 5/9 
  print("The temperature in Celcius in function temperature is " + str(C))
  #return C

x = int(input("What is the temperature in Fahrenheit: "))
#Ctemp = temperature(x)
temperature(x)
# #F = #C
#print("The temperature in Celcius is " + str(Ctemp))


def getInfo(name, age, school, grade):
  print("Name: " + name)
  print("Age: " + age)
  print("School: " + school)
  print("Grade: " + grade)

getInfo(input("What is your name? "), input("How old are you? "), input("What is your school? "), input("What is your grade? "))



Recursion
-A defined function can call itself. It is a common mathematical and programming concept. Every recursion function requires to have a parameter and a base condition.

Formula:
def funtionName(parameter):
  if (CONDITION): # base condition
    return something
  else:
    return something 


'''


# Recursion (Factorial)
def factorial(x):
  if (x==1):
    return 1
  else:
    return x * factorial(x-1)

print(factorial(5)) #5! = 5 * 4 * 3 * 2 * 1 = 120 