"""
Assignment #3, Part 2
Andrew Park
"""

import random

#ask what type they want to solve, if not any option, say invalid choice and end game.

Type = str.upper(input("What type of problem do you want to try? ADDITION, SUBTRACTION, MULTIPLICATION, or RANDOM? "))
if Type == "ADDITION":
    print("Selection saved - ADDITION")
    selection = Type
    print("Operator to use: +")
    Operator = "+"

    print()

    #use random.randint to create 2 variables and an answer variable for the problem
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = (num1 + num2)
    print("Guess #1")
    print("What is", num1, "+", num2, "?")
    choice = int(input("What is your answer? "))
    #compare the answer and the user's choice together
    if choice == answer:
        print("You answered correctly on your first try!")
    #second chance
    else:
        print("You did not answer correctly on your first try.")
        if choice > answer:
            print("Your answer was too high. Try a lower number next time.")
        else:
            print("Your answer was too low. Try a higher number next time.")
        
        print()

        print("Guess #2")
        print("What is", num1, "+", num2, "?")
        choice = int(input("What is your answer? "))
        #compare the answer and the user's choice together
        if choice == answer:
            print("You answered correctly on your second try!")
        #third chance
        else:
            print("You did not answer correctly on your second try.")
            if choice > answer:
                print("Your answer was too high. Try a lower number next time.")
            else:
                print("Your answer was too low. Try a higher number next time.")
        
            print()

            print("Guess #3")
            print("What is", num1, "+", num2, "?")
            choice = int(input("What is your answer? "))
            #compare the answer and the user's choice together
            if choice == answer:
                print("You answered correctly on your third try!")
            #answer reveal
            else:
                #the sep brings the period and number together. because using , , causes natural spacing,
                #adding a space in front of was would add 2 spaces which sep would remove one of them causing 
                #the correct spacing
                print("You did not guess correctly on your third try. The correct answer was ", answer,".", sep='')


elif Type == "SUBTRACTION":
    print("Selection saved - SUBTRACTION")
    selection = Type
    print("Operator to use: -")
    Operator = "-"

    print()

    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = (num1 - num2)
    print("What is", num1, "-", num2, "?")
    choice = int(input("What is your answer? "))
    #compare the answer and the user's choice together
    if choice == answer:
        print("You answered correctly!")
    #second chance
    else:
        print("You did not answer correctly on your first try.")
        if choice > answer:
            print("Your answer was too high. Try a lower number next time.")
        else:
            print("Your answer was too low. Try a higher number next time.")
        
        print()

        print("Guess #2")
        print("What is", num1, "-", num2, "?")
        choice = int(input("What is your answer? "))
        #compare the answer and the user's choice together
        if choice == answer:
            print("You answered correctly on your second try!")
        #third chance
        else:
            print("You did not answer correctly on your second try.")
            if choice > answer:
                print("Your answer was too high. Try a lower number next time.")
            else:
                print("Your answer was too low. Try a higher number next time.")
        
            print()

            print("Guess #3")
            print("What is", num1, "-", num2, "?")
            choice = int(input("What is your answer? "))
            #compare the answer and the user's choice together
            if choice == answer:
                print("You answered correctly on your third try!")
            #answer reveal
            else:
                #the sep brings the period and number together. because using , , causes natural spacing,
                #adding a space in front of was would add 2 spaces which sep would remove one of them causing 
                #the correct spacing
                print("You did not guess correctly on your third try. The correct answer was ", answer,".", sep='')

elif Type == "MULTIPLICATION":
    print("Selection saved - MULTIPLICATION")
    seleciton = Type
    print("Operator to use: *")
    Operator = "*"

    print()

    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    answer = (num1 * num2)
    print("What is", num1, "*", num2, "?")
    choice = int(input("What is your answer? "))
    #compare the answer and the user's choice together
    if choice == answer:
        print("You answered correctly!")
    #second chance
    else:
        print("You did not answer correctly on your first try.")
        if choice > answer:
            print("Your answer was too high. Try a lower number next time.")
        else:
            print("Your answer was too low. Try a higher number next time.")
        
        print()

        print("Guess #2")
        print("What is", num1, "*", num2, "?")
        choice = int(input("What is your answer? "))
        #compare the answer and the user's choice together
        if choice == answer:
            print("You answered correctly on your second try!")
        #third chance
        else:
            print("You did not answer correctly on your second try.")
            if choice > answer:
                print("Your answer was too high. Try a lower number next time.")
            else:
                print("Your answer was too low. Try a higher number next time.")
        
            print()

            print("Guess #3")
            print("What is", num1, "*", num2, "?")
            choice = int(input("What is your answer? "))
            #compare the answer and the user's choice together
            if choice == answer:
                print("You answered correctly on your third try!")
            #answer reveal
            else:
                #the sep brings the period and number together. because using , , causes natural spacing,
                #adding a space in front of was would add 2 spaces which sep would remove one of them causing 
                #the correct spacing
                print("You did not guess correctly on your third try. The correct answer was ", answer,".", sep='')

elif Type == "RANDOM":
    #use random.randint to choose between the 3 options of 1,2,3 (+, *, -) 
    rand = random.randint(1,3)
    if rand == 1:
        Type = "ADDITION"
        print("... we selected", Type, "as your random problem type")
        print("Operator to use: +")

        print()

        #use random.randint to create 2 variables and an answer variable for the problem
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        answer = (num1 + num2)
        print("Guess #1")
        print("What is", num1, "+", num2, "?")
        choice = int(input("What is your answer? "))
        #compare the answer and the user's choice together
        if choice == answer:
            print("You answered correctly on your first try!")
        #second chance
        else:
            print("You did not answer correctly on your first try.")
            if choice > answer:
                print("Your answer was too high. Try a lower number next time.")
            else:
                print("Your answer was too low. Try a higher number next time.")
            
            print()

            print("Guess #2")
            print("What is", num1, "+", num2, "?")
            choice = int(input("What is your answer? "))
            #compare the answer and the user's choice together
            if choice == answer:
                print("You answered correctly on your second try!")
            #third chance
            else:
                print("You did not answer correctly on your second try.")
                if choice > answer:
                    print("Your answer was too high. Try a lower number next time.")
                else:
                    print("Your answer was too low. Try a higher number next time.")
            
                print()

                print("Guess #3")
                print("What is", num1, "+", num2, "?")
                choice = int(input("What is your answer? "))
                #compare the answer and the user's choice together
                if choice == answer:
                    print("You answered correctly on your third try!")
                #answer reveal
                else:
                    #the sep brings the period and number together. because using , , causes natural spacing,
                    #adding a space in front of was would add 2 spaces which sep would remove one of them causing 
                    #the correct spacing
                    print("You did not guess correctly on your third try. The correct answer was ", answer,".", sep='')

    elif rand == 2:
        Type = "SUBTRACTION"
        print("... we selected", Type, "as your random problem type")
        print("Operator to use: -")

        print()

        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        answer = (num1 - num2)
        print("What is", num1, "-", num2, "?")
        choice = int(input("What is your answer? "))
        #compare the answer and the user's choice together
        if choice == answer:
            print("You answered correctly!")
        #second chance
        else:
            print("You did not answer correctly on your first try.")
            if choice > answer:
                print("Your answer was too high. Try a lower number next time.")
            else:
                print("Your answer was too low. Try a higher number next time.")
            
            print()

            print("Guess #2")
            print("What is", num1, "-", num2, "?")
            choice = int(input("What is your answer? "))
            #compare the answer and the user's choice together
            if choice == answer:
                print("You answered correctly on your second try!")
            #third chance
            else:
                print("You did not answer correctly on your second try.")
                if choice > answer:
                    print("Your answer was too high. Try a lower number next time.")
                else:
                    print("Your answer was too low. Try a higher number next time.")
            
                print()

                print("Guess #3")
                print("What is", num1, "-", num2, "?")
                choice = int(input("What is your answer? "))
                #compare the answer and the user's choice together
                if choice == answer:
                    print("You answered correctly on your third try!")
                #answer reveal
                else:
                    #the sep brings the period and number together. because using , , causes natural spacing,
                    #adding a space in front of was would add 2 spaces which sep would remove one of them causing 
                    #the correct spacing
                    print("You did not guess correctly on your third try. The correct answer was ", answer,".", sep='')
    else:
        Type = "MULTIPLICATION"
        print("... we selected", Type, "as your random problem type")
        print("Operator to use: *")

        print()

        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        answer = (num1 * num2)
        print("What is", num1, "*", num2, "?")
        choice = int(input("What is your answer? "))
        #compare the answer and the user's choice together
        if choice == answer:
            print("You answered correctly!")
        #second chance
        else:
            print("You did not answer correctly on your first try.")
            if choice > answer:
                print("Your answer was too high. Try a lower number next time.")
            else:
                print("Your answer was too low. Try a higher number next time.")
            
            print()

            print("Guess #2")
            print("What is", num1, "*", num2, "?")
            choice = int(input("What is your answer? "))
            #compare the answer and the user's choice together
            if choice == answer:
                print("You answered correctly on your second try!")
            #third chance
            else:
                print("You did not answer correctly on your second try.")
                if choice > answer:
                    print("Your answer was too high. Try a lower number next time.")
                else:
                    print("Your answer was too low. Try a higher number next time.")
            
                print()

                print("Guess #3")
                print("What is", num1, "*", num2, "?")
                choice = int(input("What is your answer? "))
                #compare the answer and the user's choice together
                if choice == answer:
                    print("You answered correctly on your third try!")
                #answer reveal
                else:
                    #the sep brings the period and number together. because using , , causes natural spacing,
                    #adding a space in front of was would add 2 spaces which sep would remove one of them causing 
                    #the correct spacing
                    print("You did not guess correctly on your third try. The correct answer was ", answer,".", sep='')

else:
    Type = False
    print("Invalid choice, game will end now.")
    