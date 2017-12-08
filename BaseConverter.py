#!/usr/bin/env python

#
# File:     Converter.py
# Project:  COMP163 Project, Fall 2017
# Author:   Faisal Shaheen
# Date:     12/08/17
# Github:   https://github.com/Vudark/baseConverter.git
# E-mail:   fshaheen@luc.edu  

# This is a newer version of my basic digit base converter

# The main idea implemented was taken from:
# https://cs.stackexchange.com/questions/10318/the-math-behind-converting-from-any-base-to-any-base-without-going-through-base?newreg=9f58193d052842b39866a3844188805e

# it expands the old version's capabilities to support many more bases.
# promises to support bases up to base 62.
# the refactoring of Andrej's code in the link was used in order for
# this to work with Python 3

# used to display links in the Help page
import webbrowser


# this list of symbols allows conversion of numbers represented until base 62
# More symbols can be added to represent higher bases but that would require decisions of conventional agreement.
baseSymbols='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# This function converts the value of a positive number (num) 
# to its digit representation in base (base). 
def valueToDigits(num, base):
    
    # Initiates an empty string variable as a placeholder 
    # for the digit representaion of num.
    numDigits = ''

    # while loop keeps running if num is a positive integer bigger than 0.
    while num > 0:

        # Add the numDigits string to itself + its digit representation.
        # Digit representaion is the:
        #   baseSymbol at the index of the remainder value of num 
        #   divided by the base value.
        numDigits += baseSymbols[num % int(base)]

        # The new value of num is its integer division by the base value.
        num  = num // int(base)
    return numDigits

    # For example:
    # To get the digit representation in base 2 for number 6 in base 10:
    #   While loop checks: num = 6, num > 0, true -> FIRST Iteration
    #   We look for the index value of baseSymbols at 6 % 2 which is 0
    #   so baseSymbols[0] = 0, therefore,
    #   0 is added to the begining of string numDigit.
    #   Then, we perform integer division on our initial number 6 by the 
    #   base value which is 2. Meaning, 6 // 2 = 3
    #
    #   While loop checks: num = 3, num > 0, true -> SECOND Iteration
    #   We look for the index value of baseSymbols at 3 % 2 which is 1
    #   so baseSymbols[1] = 1, therefore,   
    #   1 is added to the begining of string numDigit
    #   Then, we perform integer division on our second number 3 by the 
    #   base value which is 2. Meaning, 3 // 2 = 1
    #   
    #   While loop checks: num = 1, num > 0, true -> THIRD Iteration
    #   We look for the index value of baseSymbols at 1 % 2 which is 1
    #   so baseSymbols[1] = 1, therefore,   
    #   1 is added to the begining of string numDigit
    #   Then, we perform integer division on our third number 3 by the 
    #   base value which is 2. Meaning, 1 // 2 = 0
    #
    #   While loop checks: num = 0, num > 0, false -> stops Iterating
    #
    #   We end up with numDigits = '110' which equals 6 in base 10.
    #   We return numDigits.


# This function converts 
# the digit representation of a positive number (numDigits) 
# to its value in base (base). 
def digitsToValue(numDigits, base):

    # Initiate an integer variable num to 0.
    num = 0

    # For loop iterates through every character (i) in 
    # our string numDigits and performs the following :
    #   num is set to the value of the base multiplied by num plus:
    #       the index value at (i) in baseSymbols restricted to:
    #           the first index of baseSymbols
    #           to the index at the base value
    #       for example:
    #           baseSymbols[:16] = '0123456789ABCDEF'
    #           then,
    #           baseSymbols[:16].index('A') = 10
    #           so, num now equals 16 * 0 + 10 = 10
    for i in numDigits:
        num = int(base) * num + baseSymbols[:int(base)].index(i)
    return num

def baseToBase(numDigits, base1, base2):
    # Convert the digit representation of a number 
    # from the first base (base1) to second base (base2).

    # returns a call to valueToDigits and passes:
    #   the output of digitsToValue and the second base to convert to.
    #   Meaning, digitsToValue will take:
    #       numDigits and its base 
    #       (to be passed to (numDigits) and (base)) 
    #   and return: 
    #       the number's value (num).
    #   Then, the number's value and the second base (base2) will:
    #       be passed to valueToDigits as it's (num) and (base).
    #   Therefore, the function returns numDigits as the final output
    #   which is the number's representation in the base we want to
    #   convert to.
    result = valueToDigits(digitsToValue(numDigits, base1), base2)

    # flips the string of the result to output the correct answer
    return result[::-1]

# Simply, converts both numbers to base 10, performs addition, then returns
# the answer in the wanted base system.
def addBases(num1, base1, num2, base2, baseOfAnswer):
    num1Base10 = baseToBase(num1, base1, "10")
    num2Base10 = baseToBase(num2, base2, "10")

    answer = int(num1Base10) + int(num2Base10)

    result = baseToBase(str(answer), "10", baseOfAnswer)

    return result

# Converts both numbers to base 10, performs Subtraction, then returns
# the answer in the wanted base system.
def subtBases(num1, base1, num2, base2, baseOfAnswer):
    num1Base10 = baseToBase(num1, base1, "10")
    num2Base10 = baseToBase(num2, base2, "10")

    answer = int(num1Base10) - int(num2Base10)

    result = baseToBase(str(answer), "10", baseOfAnswer)

    return result

# Converts both numbers to base 10, performs multiplication, then returns
# the answer in the wanted base system.
def multBases(num1, base1, num2, base2, baseOfAnswer):
    num1Base10 = baseToBase(num1, base1, "10")
    num2Base10 = baseToBase(num2, base2, "10")

    answer = int(num1Base10) * int(num2Base10)

    result = baseToBase(str(answer), "10", baseOfAnswer)

    return result

# Converts both numbers to base 10, performs division, then returns
# the answer in the wanted base system.
def divBases(num1, base1, num2, base2, baseOfAnswer):
    num1Base10 = baseToBase(num1, base1, "10")
    num2Base10 = baseToBase(num2, base2, "10")

    answer = int(num1Base10) / int(num2Base10)

    result = baseToBase(str(answer), "10", baseOfAnswer)

    return result

def main():
    # A variable to hold the user's input to make sure the program
    # keeps running until the user chooses to end it.
    userInput = 1;
    while userInput != -1:
        userInput = int(input("Welcome to BaseConverter,\n\t1. Convert a number's base.\n\t2. Perform arithmetic.\n\t3. Help\nChoose an option or type '-1' to exit: "))
        if userInput == 1:
            userBaseConvertFrom = input("Enter the base number that you want to convert from: ")
            userNumConvertFrom = input("Enter the number you want to convert: ")
            userBaseConvertTo = input("Enter the base to convert it to: ")
            if int(userBaseConvertFrom) < 0 or int(userNumConvertFrom) < 0 or int(userBaseConvertTo) < 0:
                print("\nNegative numbers are not supported!\nPlease enter positive integers only\n")
            else:
                if int(userBaseConvertFrom) > 62 or int(userBaseConvertTo) > 62:
                    print("\nBases bigger than 62 are not supported!\nPlease enter bases less than 62\n")
                else:
                    print(baseToBase(userNumConvertFrom,userBaseConvertFrom,userBaseConvertTo))
        elif userInput == 2:
            userInput2 = 1
            while userInput2 != -1:
                userInput2 = int(input("\t1. Addition\n\t2. Subtraction.\n\t3. Multiplication.\n\t4. Division.\nChoose an option or type '-1' to exit: "))
                base1 = input("Enter the base of your 1st number: ")
                num1 = input("Enter your 1st number: ")
                base2 = input("Enter the base of your 2nd number: ")
                num2 = input("Enter your 2nd number: ")
                baseOfAnswer = input("Enter the base you want your answer in: ")
                if int(base1) < 0 or int(num1) < 0 or int(base1) < 0 or int(base2) < 0: 
                    print("\nNegative numbers are not supported!\nPlease enter positive integers only\n")
                else:
                    if int(base1) > 62 or int(base2) > 62 or int(baseOfAnswer) > 62:
                        print("\nBases bigger than 62 are not supported!\nPlease enter bases less than 62\n")
                    else:
                        if userInput2 == 1:
                            print(addBases(num1,base1,num2,base2, baseOfAnswer))
                        elif userInput2 == 2:
                            print(subtBases(num1,base1,num2,base2, baseOfAnswer))
                        elif userInput2 == 3:
                            print(multBases(num1,base1,num2,base2, baseOfAnswer))
                        elif userInput2 == 4:
                            print(divBases(num1,base1,num2,base2, baseOfAnswer))
        elif userInput == 3:
            print("Help:\nA. If you're having errors converting or performing arithmetic,\nit's most likely because you selected a digit that cannot be represented in that base.\n")
            print("For example: there is no digit such as: '2' in base-2.\n")
            print("If errors still occur, please visit this script's Github repository (type: github to access)\n")
            print("All the code of this script was inspired by the work of Andrej Bauer and mmj (type source to access)\n")
            print("Links can be found in the code")
            userInput3 = ''
            while userInput3 != '-1':
                userInput3 = input("Type: 'github' , 'source' , or '-1' to return back to main menu: ")
                if userInput3 == 'github':
                    webbrowser.open("https://github.com/Vudark/baseConverter.git")
                elif userInput3 == 'source':
                    webbrowser.open("https://cs.stackexchange.com/questions/10318/the-math-behind-converting-from-any-base-to-any-base-without-going-through-base?newreg=9f58193d052842b39866a3844188805e")
                

main()
