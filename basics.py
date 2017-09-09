import time
import numbers
import random


def greetings(arg):
    print("Heelo, %s" % arg)


def my_sum(arr):
    if arr:
        result = 0
        for num in arr:
            if isinstance(num, numbers.Number):
                result += num
            else:
                raise ValueError("Wrong input - %s" % num)

        return result
    else:
        raise ValueError("Input list is empty!")


def multiply(arr):
    if arr:
        result = 1
        for num in arr:
            if isinstance(num, numbers.Number):
                result *= num
            else:
                raise ValueError("Wrong input - %s" % num)
        return result
    else:
        raise ValueError("Input list is empty!")


def my_reverse(str):
    return str[::-1]


def toChars(s):
    s = s.lower()
    result = ""

    for char in s:
        if char.isalpha():
            result += char

    return result


def is_palindrome(s):
    if type(s) != str:
        raise ValueError("Not a string!")
    elif len(s) <= 1:
        return True
    else:
        s = toChars(s)
        return s[0] == s[-1] and is_palindrome(s[1:-1])


def histogram(arr):
    if arr:
        for num in arr:
            if type(num) == int and num > 0:
                print('*'*num)
                time.sleep(0.5)
            else:
                raise ValueError("Wrong input - %s" % num)
    else:
        raise ValueError("Input list is empty!")


def caesar_cipher(s, k):
    if type(s) != str:
        raise ValueError("Input value is not a string!")
    elif not s:
        raise ValueError("Input value is empty!")

    result = ""
    for c in s:
        if not c.isalpha():
            result += c
        else:
            if k >= 26: k %= 26
            newLetter_code = ord(c) + k
            if c.isupper():
                if newLetter_code not in range(65, 91):
                    result += chr(ord('A') + (24 - k))
                else:
                    result += chr(newLetter_code)
            else:
                if newLetter_code not in range(97, 123):
                    result += chr(ord('a') + (24 - k))
                else:
                    result += chr(newLetter_code)
    return result


def diagonal_reverse():
    try:
        file_input = open('input_matrix.txt', 'r')
        matrix = [list(map(int, line.split(' '))) for line in file_input]
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    except IOError:
        print("An I/O error occured")

    except ValueError:
        print("A ValueError occured")


def game(start, finish):
    try:
        magic_number = random.randint(start, finish)
        user_input = int(input("Please enter a random number from {0} to {1}: ".format(start, finish)))
        while user_input != magic_number:
            print("Ooopps! You didn't guess the number. Try again!")
            user_input = int(input("Please enter a random number from {0} to {1}: ".format(start, finish)))
        else:
            print("Ooohhoo! Congrats! You guessed the number! ")
            time.sleep(2)
            print("Game over! Bye!")
            return magic_number

    except ValueError:
        print("You should have given an int!")


def checkBrackets(seq):
    s = []
    balanced = True
    index = 0
    while index < len(seq) and balanced:
        symbol = seq[index]
        if symbol == "[":
            s.append(symbol)
        else:
            if not s:
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and not s:
        return "OK"
    else:
        return "NOT OK"


def char_freq(String):
    if type(String) != str:
        raise ValueError("Not a string!")
    elif len(String) <= 1:
        return True
    else:
        dictionary = {String[0]: 1}
        for char in String[1:]:
            if char in dictionary.keys():
                value = dictionary.get(char)
                value += 1
                dictionary[char] = value
            else:
                dictionary2 = {char: 1}
                dictionary.update(dictionary2)
        return dictionary


def dec_to_bin(integer):
    res = ""
    if type(integer) != int or integer < 0:
        raise ValueError("Wrong input value: %s" % integer)
    elif integer == 0:
        return 0
    else:
        while integer != 0:
            res += str(integer % 2)
            integer //= 2
    return int(res[::-1])


def ship_battle(order):
    print("************Welcome to Battleship Game!************")
    x = random.randint(0, order)
    y = random.randint(0, order)
    print(x, y)
    var1, var2 = input("Enter two number here: ").split(' ')
    while int(var1) != x or int(var2) != y:
        print("You missed! Please try again!")
        time.sleep(0.5)
        var1, var2 = input("Enter two number here: ").split(' ')
    else:
        print("Congrats! You sunk my battleship!")
