#Below you will find several older homework questions done correctly using input
#and print statements. our task is to take each one and convert it to arguments and returns instead.


#modify the below function such that it asks the user for 2 numbers as input.
#Then have it print out the larger number
def larger():
    n1 = input("give me a number")
    n2 = input("give me a number")
    n1 = int(n1)
    n2 = int(n2)
    if( n1 > n2):
        print (n1)
    else:
        print (n2)

def larger(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

#Modify the below function such that it asks for the users score as an input.
#Then based on the score print out a letter grade.
# 90+ A
# 80+ B
# 70+ C
# 60+ D
# 59- F
def grade(g):
    g = input("Give me your grade")
    if( g>=90):
        print ("A")
    elif( g>= 80):
        print ("B")
    elif(g >= 70):
        print ("C")
    elif(g >= 60):
        print ("D")
    else:
        print ("F")

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
#Modify the below function such that it asks the user for a number then
#if the number is divisible by 3 print "fizz"
#if the number is divisible by 5 print "buzz"
#if both are the case then print "Fizzbuzz" instead of the prior two
#if niether are the case print the number.
def fizzbuzz():
    n = input("Give me a number")
    n = int(n)
    if(n%5==0 and n%3==0):
        print( "FizzBuzz")
    elif(n%3==0):
        print ("fizz")
    elif(n%5==0):
        print ("buzz")
    else:
        print(n)

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return n
#modify the below function such that it asks the user for an input number.
#if the number is even divide it by two.
#if the number is odd multiply it by 3 and add 1
#then print the new number.
def collatz():
    n = input("Give me a number")
    n = int(n)
    if(n==1):
        print (n)
    if(n%2==0):
        print (n/2)
    else:
        print (3*n+1)

def collatz(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def convertTemperature(temp_str):
    temp_str = temp_str.strip().upper()

    # last character is the unit
    unit = temp_str[-1]
    value = float(temp_str[:-1])  # everything except last char

    if unit == "C":
        fahrenheit = (value * 9 / 5) + 32
        return f"{int(fahrenheit)}F"
    elif unit == "F":
        celsius = (value - 32) * 5 / 9
        return f"{int(celsius)}C"
    else:
        # in case they pass something weird
        return "Invalid"


#Modify the below function such that it asks the user for a temperature.
#The format for temperature should end in F For Fahrenheit and C for Celcius
#Then given the temperature if it is in Fahrenheit convert it to Celsius on vice versa
#Example 32F -> 0C  20C -> 68F
def convert_temperature(temp_str):
    """
    Convert "32F" -> "0C" or "20C" -> "68F".
    Expects a string ending in 'F' or 'C'.
    """
    temp_str = temp_str.strip().upper()
    unit = temp_str[-1]
    value = float(temp_str[:-1])

    if unit == "C":
        fahrenheit = (value * 9 / 5) + 32
        return f"{int(fahrenheit)}F"
    elif unit == "F":
        celsius = (value - 32) * 5 / 9
        return f"{int(celsius)}C"
    else:
        return "Invalid temperature format"
