import random
from time import *
import threading
from versus_score import update_versus
# versus mode
# timer = 60

# while timer > 0:


def countdown():
    global my_timer
    my_timer = 60
    for i in range(60):
        # print(my_timer)
        my_timer -= 1
        sleep(1)
    #print("out of time")


def countdown2():
    global my_timer2
    my_timer2 = 60
    for i in range(60):
        # print(my_timer)
        my_timer2 -= 1
        sleep(1)
    #print("\nTime is up!")
    #print("out of time")


countdown_thread = threading.Thread(target=countdown)
countdown2_thread = threading.Thread(target=countdown2)

character = input(
    "User A enter character you would like to select: dog1, dog2, dog3, dog4: \n")
while character != 'dog1' and character != 'dog2' and character != 'dog3' and character != 'dog4':
    character = input(
        "Character does not exist, please re-enter your character:")
dog1operations = ['-', '*', '//', ]  # avoids addition
dog2operations = ['+', '*', '//', ]  # avoid subtraction
dog3operations = ['+', '-', '//', ]  # avoid multiplication
dog4operations = ['+', '-', '*', ]  # avoid division
# note: excluded 0 bcs in division 0/5 causes error
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
score = 0  # user score
countdown_thread.start()
while my_timer > 0:
    # for i in range(0, 5):
    if character == "dog1":
        index = random.choice(dog1operations)
    if character == "dog2":
        index = random.choice(dog2operations)
    if character == "dog3":
        index = random.choice(dog3operations)
    if character == "dog4":
        index = random.choice(dog4operations)
    # index = '+'
    num1 = random.choice(numbers1)
    num2 = random.choice(numbers2)
    if index == '+':
        result = num1 + num2
        user_answer = int(input(f"What is the sum of {num1} and {num2}? "))
        print(
            f"numbers1: {num1} numbers2:  {num2} should equal result: {result}")
        print(
            f"the answer should be {result} and the user entered {user_answer}")
        if user_answer == result:
            print("Correct, you have received a point!")
            score += 1
        if user_answer != result:
            print(
                "Wrong, you did not receive a point, your score remains the same:")
        print("score = ", score)
        if my_timer == 0:
            print("\nTime is up!")
            break
    if index == '-':
        result = num1 - num2
        user_answer = int(
            input(f"What is the difference of {num1} and {num2}? "))
        print(
            f"numbers1: {num1} numbers2: {num2} should equal result: {result}")
        print(
            f"the answer should be {result} and the user entered {user_answer}")
        if user_answer == result:
            print("Correct, you have received a point!")
            score += 1
        if user_answer != result:
            print(
                "Wrong, you did not receive a point, your score remains the same:")
        print("score = ", score)
        if my_timer == 0:
            print("\nTime is up!")
            break
        # print(index)
    if index == '*':
        result = num1 * num2
        user_answer = int(
            input(f"What is the product of {num1} and {num2}? "))
        print(
            f"numbers1: {num1} numbers2:  {num2} should equal result: {result}")
        print(
            f"the answer should be {result} and the user entered {user_answer}")
        if user_answer == result:
            print("Correct, you have received a point!")
            score += 1
        if user_answer != result:
            print(
                "Wrong, you did not receive a point, your score remains the same:")
        print("score = ", score)
        if my_timer == 0:
            print("\nTime is up!")
            break
    if index == '//':
        result = num1 // num2
        user_answer = int(
            input(f"What is the division of {num1} and {num2}? Be sure to round to the nearest integer "))
        print(
            f"numbers1: {num1} numbers2:  {num2} should equal result: {result}")
        print(
            f"the answer should be {result} and the user entered {user_answer}")
        if user_answer == result:
            print("Correct, you have received a point!")
            score += 1
        if user_answer != result:
            print(
                "Wrong, you did not receive a point, your score remains the same:")
        print("score = ", score)
        if my_timer == 0:
            print("\nTime is up!")
            break
    # print(index)
print(f"Your final score is {score}")
########################################
character = input(
    "User B enter character you would like to select: dog1, dog2, dog3, dog4: \n")
while character != 'dog1' and character != 'dog2' and character != 'dog3' and character != 'dog4':
    character = input(
        "Character does not exist, please reenter your character:")
dog1operations = ['-', '*', '//', ]  # avoids addition
dog2operations = ['+', '*', '//', ]  # avoid subtraction
dog3operations = ['+', '-', '//', ]  # avoid multiplication
dog4operations = ['+', '-', '*', ]  # avoid division
# note: excluded 0 bcs in division 0/5 causes error
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
score2 = 0  # user score
countdown2_thread.start()
while my_timer2 > 0:
    # for i in range(0, 5):
    if character == "dog1":
        index = random.choice(dog1operations)
    if character == "dog2":
        index = random.choice(dog2operations)
    if character == "dog3":
        index = random.choice(dog3operations)
    if character == "dog4":
        index = random.choice(dog4operations)
    # index = '+'
    num1 = random.choice(numbers1)
    num2 = random.choice(numbers2)
    if index == '+':
        result = num1 + num2
        user_answer = int(input(f"What is the sum of {num1} and {num2}? "))
        print(
            f"numbers1: {num1} numbers2:  {num2} should equal result: {result}")
        print(
            f"the answer should be {result} and the user entered {user_answer}")
        if user_answer == result:
            print("Correct, you have received a point!")
            score2 += 1
        if user_answer != result:
            print(
                "wrong, you did not received a point, your score remains the same:")
        print("score = ", score2)
        if my_timer2 == 0:
            print("\nTime is up!")
            break
    if index == '-':
        result = num1 - num2
        user_answer = int(
            input(f"What is the difference of {num1} and {num2}? "))
        print(
            f"numbers1: {num1} numbers2:  {num2} should equal result: {result}")
        print(
            f"the answer should be {result} and the user entered {user_answer}")
        if user_answer == result:
            print("Correct, you have received a point!")
            score2 += 1
        if user_answer != result:
            print(
                "Wrong, you did not receive a point, your score remains the same:")
        print("score = ", score2)
        if my_timer2 == 0:
            print("\nTime is up!")
            break
        # print(index)
    if index == '*':
        result = num1 * num2
        user_answer = int(
            input(f"What is the product of {num1} and {num2}? "))
        print(
            f"numbers1: {num1} numbers2:  {num2} should equal result: {result}")
        print(
            f"the answer should be {result} and the user entered {user_answer}")
        if user_answer == result:
            print("Correct, you have received a point!")
            score2 += 1
        if user_answer != result:
            print(
                "Wrong, you did not receive a point, your score remains the same:")
        print("score = ", score2)
        if my_timer2 == 0:
            print("\nTime is up!")
            break
    if index == '//':
        result = num1 // num2
        user_answer = int(
            input(f"What is the division of {num1} and {num2}? Be sure to round to the nearest integer "))
        print(
            f"numbers1: {num1} numbers2:  {num2} should equal result: {result}")
        print(
            f"the answer should be {result} and the user entered {user_answer}")
        if user_answer == result:
            print("Correct, you have received a point!")
            score2 += 1
        if user_answer != result:
            print(
                "Wrong, you did not receive a point, your score remains the same:")
        print("score = ", score2)
        if my_timer2 == 0:
            print("\nTime is up!")
            break
    # print(index)
print(f"Your final score is {score2}")
print(f"User A scored {score} and user B scored {score2}")
if score > score2:
    print("User A has been victorious and user B has loss")
    update_versus(score)
else:
    print("User B has been victorious and user A has loss")
    update_versus(score2)

