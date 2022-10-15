import random
from time import *
import threading
# versus mode
# timer = 60

# while timer > 0:


def countdown():
    global my_timer
    my_timer = 10
    for i in range(10):
        # print(my_timer)
        my_timer -= 1
        sleep(1)
    # print("out of time")
    score = 0  # user score


countdown_thread = threading.Thread(target=countdown)

################## get question function for user A ###################


def get_question(character, score):
    dog1operations = ['-', '*', '//', ]  # avoids addition
    dog2operations = ['+', '*', '//', ]  # avoid subtraction
    dog3operations = ['+', '-', '//', ]  # avoid multiplication
    dog4operations = ['+', '-', '*', ]  # avoid division
    # note: excluded 0 bcs in division 0/5 causes error
    numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num1 = random.choice(numbers1)
    num2 = random.choice(numbers2)
    if character == "dog1":
        index = random.choice(dog1operations)
    if character == "dog2":
        index = random.choice(dog2operations)
    if character == "dog3":
        index = random.choice(dog3operations)
    if character == "dog4":
        index = random.choice(dog4operations)
    # index = '+'  # testing purposes
    if index == '+':
        result = num1 + num2
        user_answer = int(input(f"What is the sum of {num1} and {num2}? "))
        print(f"Your answer should be {result}")
        score = get_score(result, user_answer, score)
        print(f"your score is {score}")
    if index == '-':
        result = num1 - num2
        user_answer = int(
            input(f"What is the difference of {num1} and {num2}? "))
        print(f"Your answer should be {result}")
        score = get_score(result, user_answer, score)
        print(f"your score is {score}")
    if index == '*':
        result = num1 * num2
        user_answer = int(input(f"What is the product of {num1} and {num2}? "))
        print(f"Your answer should be {result}")
        score = get_score(result, user_answer, score)
        print(f"your score is {score}")
    else:  # if index == '*':
        result = num1 // num2
        user_answer = int(input(f"What {num1} divided by {num2}? "))
        print(f"Your answer should be {result}")
        score = get_score(result, user_answer, score)
        print(f"your score is {score}")
    # also return result, user_answer
    # returns question information & user answer & user score
    question_info = [num1, num2, index, result, user_answer, score]
    if my_timer == 0:
        print("\nTime is up!")
        return question_info
    return question_info
    # function for user2

 ################### get question function for user B ##################


def get_question2(character, score):
    dog1operations = ['-', '*', '//', ]  # avoids addition
    dog2operations = ['+', '*', '//', ]  # avoid subtraction
    dog3operations = ['+', '-', '//', ]  # avoid multiplication
    dog4operations = ['+', '-', '*', ]  # avoid division
    # note: excluded 0 bcs in division 0/5 causes error
    numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num1 = random.choice(numbers1)
    num2 = random.choice(numbers2)
    if (character == "dog1"):
        index = random.choice(dog1operations)
    if (character == "dog2"):
        index = random.choice(dog2operations)
    if (character == "dog3"):
        index = random.choice(dog3operations)
    if (character == "dog4"):
        index = random.choice(dog4operations)
    # index = '+'  # testing purposes
    if index == '+':
        result = num1 + num2
        user_answer = int(input(f"What is the sum of {num1} and {num2}? "))
        print(f"Your answer should be {result}")
        score = get_score(result, user_answer, score)
        print(f"your score is {score}")
    if index == '-':
        result = num1 - num2
        user_answer = int(
            input(f"What is the difference of {num1} and {num2}? "))
        print(f"Your answer should be {result}")
        score = get_score(result, user_answer, score)
        print(f"your score is {score}")
    if index == '*':
        result = num1 * num2
        user_answer = int(input(f"What is the product of {num1} and {num2}? "))
        print(f"Your answer should be {result}")
        score = get_score(result, user_answer, score)
        print(f"your score is {score}")
    else:  # if index == '*':
        result = num1 // num2
        user_answer = int(input(f"What {num1} divided by {num2}? "))
        print(f"Your answer should be {result}")
        score = get_score(result, user_answer, score)
        print(f"your score is {score}")
    # also return result, user_answer
    # returns question infomration & user answer & user score
    question_info = [num1, num2, index, result, user_answer, score]
    if my_timer2 == 0:
        print("\nTime is up!")
        return question_info
    return question_info


def get_score(result, user_answer, score):
    if result == user_answer:
        score += 1
    else:
        score = score
    return score


# can be used later possibly to determine winner/losser/tiebreaker
def final_score_user1(score):
    return score


# can be used later possibly to determine winner/losser/tiebreaker
def final_score_user2(score):
    return score


def game_start():
    score = 0
    character = input(
        "User A enter character you would like to select: dog1, dog2, dog3, dog4: \n")
    while character != 'dog1' and character != 'dog2' and character != 'dog3' and character != 'dog4':
        character = input(
            "Character does not exist, please re-enter your character: \n")
    countdown_thread.start()
    while my_timer > 0:
        # for i in range(0, 5):
        question = get_question(character, score)
        score = question[5]
        # index = '+'

        # print(index)
    # score = get_score(question[3], question[4], score)
    print(f"User A, your final score is {score}")
    user1_finalscore = final_score_user1(score)

    ###################### User 2 turn #########################


def countdown2():
    global my_timer2
    my_timer2 = 10
    for i in range(10):
        # print(my_timer)
        my_timer2 -= 1
        sleep(1)
    # print("out of time")
    score = 0  # user score


countdown2_thread = threading.Thread(target=countdown2)


def game_start2():
    score = 0  # reset score to 0
    character = input(
        "User B enter character you would like to select: dog1, dog2, dog3, dog4: \n")
    while character != 'dog1' and character != 'dog2' and character != 'dog3' and character != 'dog4':
        character = input(
            "Character does not exist, please reenter your character: \n")
    countdown2_thread.start()
    while my_timer2 > 0:
        # for i in range(0, 5):
        question = get_question2(character, score)
        score = question[5]
    print(f"UserB, your final score is {score}")
    user2_finalscore = final_score_user2(score)


game_start()
game_start2()
