# warm up excercise
# ** step 1 write our functions for the caclulator **
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y


# **Step 2: write our user interface **
print("***********************************************************************")
print("* Welcome to Quinni's Calculator sponsored by Quinni Calculations.inc *")
print("***********************************************************************")
print(                                                                         )
print("Please choose from the following:")
print("1. Addition + ")
print("2. Subtraction - ")
print("3. Multiplication * ")
print("4. Division / ")

# **Step 3: allow our users to make a choice and input their 2 numbers **
# while true allows us to enter loop at least once; define choice so input variable can call corresponding function.
# while true clause creates infinite back to enter choice; if any error is encountered except and continue clause take
# us back need to make breaks in order to break this loop and go back to previous prompt NOT first prompt (enter choice)
while True:

    while True:
        try:
            choice = input("Enter Choice of operation: ")
    # code will not work if '=' instead of in (input must be in list of 1-4)
            if choice in ('1', '2', '3', '4'):
                break
            elif choice not in ('1','2','3','4'):
              print("Choose the number of operation (1-4)")
        except ValueError:
          print("Invalid input Queen! Try a number!")
    # using try... except to account for invalid input, allow another try and to stop programming crashing.
    while True:
        try:
           num1 = float(input("Enter first num: "))
           break
        except ValueError:
           print("Invalid input Queen! Try a number!")
    while True:
        try:
            num2 = float(input("Enter second num: "))
            break
        except ValueError:
            print("Invalid input Queen! Try a number!")


    # ** Step 4: call functions according to user input and print result **
    # output will be x _ y = ans
    if choice == '1':
        print(num1, "+", num2,"=", add(num1, num2))
        print("^ There's your answer queen <3 ^")
    elif choice == '2':
        print(num1, '-', num2, '=', sub(num1, num2))
        print("^ There's your answer queen <3 ^")

    elif choice == '3':
        print(num1, '*', num2, '=', mult(num1, num2))
        print("^ There's your answer queen <3 ^")

    elif choice == '4':
        print(num1, '/', num2, '=', div(num1, num2))
        print("^ There's your answer queen <3 ^")
     # **Step 5: new calculation or end programme
     # break programme if user input is "no"
     # NOTE INDENTATION HERE - IT'S CRITICAL

    while True:
        nextcalc = input("Would you like to do another calculation? \n Yes or No?: ")
        if nextcalc in ["yes", "no"]:
            break
        else:
            print("Invalid input! Please enter 'yes' or 'no':")
# no while loop bc we want to break from the first one we set so it doesnt loop back to option choice
    if nextcalc == "no":
        print("Thank you for using Quinni Calculations for your mathematical needs \n Goodbye! <33")
        break
# research when to use continue and when to use break


