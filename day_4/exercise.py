# ITP Week 1 Day 4 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
def subtract():
    firstNum = int(input("Please enter the first number you want to subtract: "))
    secondNum = int(input("Please enter the second number you want to subtract: "))
    # return (firstNum - secondNum)
    print(firstNum - secondNum)

subtract()
#     - A function that multiplies three integers
def multiple():
    num1 = int(input("Please enter the first number you want to multiple: "))
    num2 = int(input("Please enter the second number you want to multiple: "))
    num3 = int(input("Please enter the third number you want to multiple: "))    
    print(num1*num2*num3)

multiple()
#     - A function that adds four integers
def add():
    num1 = int(input("Please enter the first number you want to add: "))
    num2 = int(input("Please enter the second number you want to add: "))
    num3 = int(input("Please enter the third number you want to add: "))  
    num4 = int(input("Please enter the third number you want to add: "))  
    print(num1 + num2 + num3 + num4)

add()

# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.

# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.  You may use the math module from the Python standard library.

#Remember to first write in comments an outline of what you want to code (using regular words, no computer-speak) BEFORE you begin to code.  Break each part down to the smallest problem you can, and then address them individually.  CONSULT THE RESOURCES if you get stuck, and don't be afraid to Google.