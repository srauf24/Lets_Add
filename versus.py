import random
# versus mode
# timer = 60

# while timer > 0:
character = input(
    "Enter character you would like to select: dog1, dog2, dog3, dog4: \n")
while character != 'dog1' and character != 'dog2' and character != 'dog3' and character != 'dog4':
    character = input(
        "Character does not exist, please reenter your character:")
dog1operations = ['-', '*', '//', ]  # avoids addition
dog2operations = ['+', '*', '//', ]  # avoid subtraction
dog3operations = ['+', '-', '//', ]  # avoid multiplication
dog4operations = ['+', '-', '*', ]  # avoid multiplication
numbers1 = [1, 2, 3, 4, 5]  # note: excluded 0 bcs in division 0/5 causes error
numbers2 = [1, 2, 3, 4, 5]
score = 0
for i in range(0, 5):
    if (character == "Animations/dog1"):
        index = random.choice(dog1operations)
    if (character == "dog2"):
        index = random.choice(dog2operations)
    if (character == "dog3"):
        index = random.choice(dog3operations)
    if (character == "dog4"):
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
            print("correct, you have recievd a point")
            score += 1
        if user_answer != result:
            print("wrong, you did not recieved a point")
        print("score = ", score)
    if index == '-':
        result = num1 - num2
        user_answer = int(
            input(f"What is the difference of {num1} and {num2}? "))
        print(
            f"numbers1: {num1} numbers2:  {num2} should equal result: {result}")
        print(
            f"the answer should be {result} and the user entered {user_answer}")
        if user_answer == result:
            print("correct, you have recievd a point")
            score += 1
        if user_answer != result:
            print("wrong, you did not recieved a point")
        print("score = ", score)
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
            print("correct, you have recievd a point")
            score += 1
        if user_answer != result:
            print("wrong, you did not recieved a point")
        print("score = ", score)
    if index == '//':
        result = num1 // num2
        user_answer = int(
            input(f"What is the division of {num1} and {num2}? Be sure to round to the nearest integer "))
        print(
            f"numbers1: {num1} numbers2:  {num2} should equal result: {result}")
        print(
            f"the answer should be {result} and the user entered {user_answer}")
        if user_answer == result:
            print("correct, you have recievd a point")
            score += 1
        if user_answer != result:
            print("wrong, you did not recieved a point")
        print("score = ", score)
        # print(index)
