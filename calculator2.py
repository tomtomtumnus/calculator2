#Created on Fri Jan  3 17:58:47 2020
#slightly more advanced calculator
#@author: Thomas Gaudin

#import relevant math functions
from math import factorial, pow, log, sqrt, log2, log10
from numpy import prod
                
def length_checker(list, value):
    """Checks to make sure the input list is of the proper length."""
    #handles too short lists
    if len(list) < value:
            print("Too few arguments.")
            return False
    #handles too long lists
    elif len(list) > value:
            print("Too many arguments.")
            return False
    #passes valid lists to function
    else:
        return list
    
def subtract(list):
    """Subtracts every number in a list"""
    #initialize values
    difference = list[0]
    #subtract every value from initial value and return result
    for x in list[1:]:
        difference = difference - x
    return difference
    
def clear_all():
    """Resets lists and variables"""
    global operation, integers
    del operation, integers[:]
    
        
print("Greetings.")
print("I am a calculator.")
print("I can add, subtract, multiply, and divide.")
print("I can also take square roots and raise to exponents.")
print("Use me for factorials and logarithmic calculations.")
print("Press 'q' in 'operation prompt' to quit.")

while True:
    #generates a list of prompted integers, breaks for non-integer responses
    try:
        integers = list(map(int, input("Enter values: ").split()))
    except ValueError:
        print("Every input must be an integer!")
        break
    #operation input, break loop using 'q'
    operation = input("Pick an operation. (+, -, *, /, !, ^, sqrt, log, ln) ")
    if operation == 'q':
        break
    
    #function operation and print value
    if operation == "+":
        summation = sum(integers)
        print(summation)
        #delete inputs for next calculation
        clear_all()
    elif operation == "-":
        #call subrtact function on input integers
        answer = subtract(integers)
        print(answer) 
        #delete inputs for next calculation
        clear_all()
    elif operation == "*":
        #calls math product to complete calculation and print
        product = prod(integers)
        print(product)
        #delete inputs for next calculation
        clear_all()    
    elif operation == "/":
        #calculation through divide function and print
        try:    
            #initialize values
            dividend = integers[0]
            #divide every value from initial value:
            for divisor in integers[1:]:
                dividend = dividend / divisor
            print(dividend)
            #delete inputs for next calculation
        except ZeroDivisionError:
            print("Tried to divide by zero. Do not break math.")
            print("I quit.")
            break
        clear_all()
    elif operation == "!":
        #check that only one number is factorialed at a time
        if length_checker(integers, 1) == False:
            print("Please do not kill me.")
            print("I quit.")
            break
        else:
            #make sure that no value errors for negative or rational numbers appear
            for x in integers:
                try:
                    factorial(x)
                except ValueError:
                    print("Please use a positive integer.")
                    print("I quit.")
                    break
            #call math factorial function and print
            answer2 = factorial(integers[0])
            print(answer2)
            #delete inputs for next calculation
            clear_all()
    elif operation == "^":
        #make sure you have correct number of input values
        if length_checker(integers, 2) == False:
            print("You must raise one number at a time.")
            print("I quit.")
            break
        else:
            #math pow function and print answer
            answer3 = pow(integers[0], integers[1])
            print(answer3)
            #delete inputs for next calculation
            clear_all()
    elif operation == "sqrt":
        #run checks for one positive value
        if length_checker(integers, 1) == False:
            break
        elif integers[0] < 1:
            print("Do you want imaginary numbers? Because I don't.")
            print("I quit.")
            break
        else:
            #run math sqrt function and print answer
            answer7 = sqrt(integers[0])
            print(answer7)
            #delete inputs for next calculation
            clear_all()
    elif operation == "log":
        #checks for log and base using length checker function
        if length_checker(integers, 2) == False:
            print("Must select a log and base. No more. No less.")
            print("I quit.")
            break
        #run checks to prevent errors from negative numbers
        elif integers[0] < 0:
            print("Do you want domain errors? BECAUSE I DON'T.")
            print("I quit.")
            break
        elif integers[1] < 0:
            print("Do you want domain errors? BECAUSE I DON'T.")
            print("I quit.")
            break
        #two specific cases where the math log2 and math log10 functions will 
        #be more accurate
        elif integers[1] == 2:
            logarithm2 = log2(integers[0])
            print(logarithm2)
        elif integers[1] == 10:
            logarithm10 = log10(integers[0])
            print(logarithm10)
        #calculate and print. clear inputs for next calculation
        else:
            logarithmb = log(integers[0], integers[1])
            print(logarithmb)
            clear_all()
    elif operation == "ln":
        #prevent domain errors with checks
        if length_checker(integers, 1) == False:
            print("You have called log to base e. Do not select a base. Just a number.")
            print("I quit.")
            break
        elif integers[0] < 0:
            print("Do you want domain errors? BECAUSE I DON'T.")
            print("I quit.")
            break
        #calculate and print. use math log without a base specified so it uses e
        #clear inputs for next calculation
        else:
            natlog = log(integers[0])
            print(natlog)
            clear_all()
    else:
        print("Pick a valid operation.") #checks to make sure input is valid
        #delete inputs for next calculation
        clear_all()
