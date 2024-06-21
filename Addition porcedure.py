# Libarys and variables
import math
global num_1
num_1 = 0
global num_2
num_2 = 0
global num_3
num_3 = 0
global ans
ans = 0
global reset_ans
# Procedures
# Addition
def addition():
    if ans != 0:
        reset_ans = input("Would you like to reset the value of ans to 0: ")
        if reset_ans == "Yes":
            num_1 = float(input("Please enter the first number for the addition: "))
            num_2 = float(input("Please enter the second number for the addition: "))
            ans = num_1 + num_2
            print(num_1, "+", num_2, "=", ans)
            carry_on = input("Would you like to add another number to your answer: ")
            if carry_on == "Yes":
                new_or_carry_on =  input("Would you like to do a new calculator or add another number to the calculation just performed: ")
            if new_or_carry_on == "New calculation":
                while carry_on == "Yes":
                    num_1 = float(input("Please enter the first number for the addition: "))
                    num_2 = float(input("Please enter the second number for the addition: "))
                    ans = num_1 + num_2
                    print(num_1, "+", num_2 ,"=", ans)
                    carry_on = input("Would you like to add another number to your answer: ")
            elif new_or_carry_on == "Carry on":
                while carry_on == "Yes":
                    num_3 = float(input("Please enter the number which you would like to add to the total", ans ,": "))
                    first_answer = num_1+num_2
                    ans = ans+num_3
                    print(first_answer, "+", num_3, "=", ans)
                    carry_on = input("Would you like to add another number to your answer: ")
        elif reset_ans == "yes":
            num_1 = float(input("Please enter the first number for the addition: "))
            num_2 = float(input("Please enter the second number for the addition: "))
            ans = num_1 + num_2
            print(num_1, "+", num_2, "=", ans)
            carry_on = input("Would you like to add another number to your answer: ")
            if carry_on == "Yes":
                new_or_carry_on =  input("Would you like to do a new calculator or add another number to the calculation just performed: ")
            if new_or_carry_on == "New calculation":
                while carry_on == "Yes":
                num_1 = float(input("Please enter the first number for the addition: "))
                num_2 = float(input("Please enter the second number for the addition: "))
                ans = num_1 + num_2
                print(num_1, "+", num_2 ,"=", ans)
                carry_on = input("Would you like to add another number to your answer: ")
            elif new_or_carry_on == "Carry on":
                while carry_on == "Yes":
                    num_3 = float(input("Please enter the number which you would like to add to the total", ans ,": "))
                    first_answer = num_1+num_2
                    ans = ans+num_3
                    print(first_answer, "+", num_3, "=", ans)
                    carry_on = input("Would you like to add another number to your answer: ")
        else:
            while carry_on == "Yes"
                num_3 = int(input("Please enter the number which you would like to add to the total", ans ,": "))
                ans_o = ans
                ans = num_3 + ans
                print(ans_o, "+", num_3 ,"=",ans)
                carry_on = input("Would you like to add another number to your answer: ")
    else:
        num_1 = float(input("Please enter the first number for the addition: "))
        num_2 = float(input("Please enter the second number for the addition: "))
        ans = num_1 + num_2
        print(num_1, "+", num_2, "=", ans)
        carry_on = input("Would you like to add another number to your answer: ")
        if carry_on == "Yes":
            new_or_carry_on =  input("Would you like to do a new calculator or add another number to the calculation just performed: ")
        if new_or_carry_on == "New calculation":
            while carry_on == "Yes":
                num_1 = float(input("Please enter the first number for the addition: "))
                num_2 = float(input("Please enter the second number for the addition: "))
                ans = num_1 + num_2
                print(num_1, "+", num_2 ,"=", ans)
                carry_on = input("Would you like to add another number to your answer: ")
        elif new_or_carry_on == "Carry on":
            while carry_on == "Yes":
                num_3 = float(input("Please enter the number which you would like to add to the total", ans ,": "))
                first_answer = num_1+num_2
                ans = ans+num_3
                print(first_answer, "+", num_3, "=", ans)
                carry_on = input("Would you like to add another number to your answer: ")
    print("The final total is", ans)
addition()
