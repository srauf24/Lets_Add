import random
from time import *
from endless_score import update_endless

def get_question(character):
    dog1operations = ['-', '*', '//']  # avoids addition
    dog2operations = ['+', '*', '//']  # avoid subtraction
    dog3operations = ['+', '-', '//']  # avoid multiplication
    dog4operations = ['+', '-', '*']  # avoid division
    # note: excluded 0 bcs in division 0/5 causes error
    numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    num1 = random.choice(numbers1)
    num2 = random.choice(numbers2)
    if character == "Animations/SleepFoxAnimation":
        index = random.choice(dog1operations)
    elif character == "Animations/GoldieAnimation":
        index = random.choice(dog2operations)
    elif character == "Animations/SilverSitAnimation":
        index = random.choice(dog3operations)
    elif character == "Animations/CatRunAnimation":
        index = random.choice(dog4operations)
    # index = '+'  # testing purposes
    if index == '+':
        result = num1 + num2
        # user_answer = int(input(f"What is the sum of {num1} and {num2}? "))
        # print(f"Your answer should be {result}")
        # score = get_score(result, user_answer, score)
        # lives = get_lives(result, user_answer, lives)
        # print(f"your score is {score}")
        # print(f"You have {lives} lives")
    elif index == '-':
        result = num1 - num2
        # user_answer = int(
        #     input(f"What is the difference of {num1} and {num2}? "))
        # print(f"Your answer should be {result}")
        # score = get_score(result, user_answer, score)
        # lives = get_lives(result, user_answer, lives)
        # print(f"your score is {score}")
        # print(f"You have {lives} lives")
    elif index == '*':
        result = num1 * num2
        # user_answer = int(input(f"What is the product of {num1} and {num2}? "))
        # score = get_score(result, user_answer, score)
        # lives = get_lives(result, user_answer, lives)
        # print(f"your score is {score}")
        # print(f"You have {lives} lives")
    elif index == '//':
        result = num1 // num2
        # user_answer = int(input(f"What {num1} divided by {num2}? "))
        # score = get_score(result, user_answer, score)
        # lives = get_lives(result, user_answer, lives)
        # print(f"your score is {score}")
        # print(f"You have {lives} lives")
    # also return result, user_answer
    # returns question information & user answer & user score
    
    question = str(num1) + " " + str(index) + " " + str(num2) + " = ?"
    print("num1 is ",num1)
    print("index is ", index)
    print("num2 is ", num2)
    print("result is " , result)
    question_info = [question, result]
    return question_info
    # function for user2


# def get_score(result, user_answer, score):
#     if result == user_answer:
#         score += 1
#     else:
#         score = score
#     return score


# def get_lives(result, user_answer, lives):
#     if result != user_answer:
#         lives -= 1
#     return lives


# # can be used later possibly to determine winner/losser/tiebreaker
# def final_score_user1(score):
#     return score


# def game_start():
#     score = 0
#     lives = 3
#     character = input(
#         "User A enter character you would like to select: dog1, dog2, dog3, dog4: \n")
#     while character != 'dog1' and character != 'dog2' and character != 'dog3' and character != 'dog4':
#         character = input(
#             "Character does not exist, please re-enter your character: \n")
#     while lives > 0:
#         # for i in range(0, 5):
#         question = get_question(character, score, lives)
#         score = question[5]
#         lives = question[6]
#         # index = '+'

#         # print(index)
#     # score = get_score(question[3], question[4], score)
#     print(f"User A, your final score is {score}")
#     user1_finalscore = final_score_user1(score)
#     update_endless(score)

    ###################### User 2 turn #########################
