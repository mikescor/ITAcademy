import time
from random import randint


def greetings(arg):
    print("Heelo, %s" % arg)



def my_sum(arr):
    result = 0
    for num in arr:
        result += num
    return result



def multiply(arr):
    result = 1
    for num in arr:
        result *= num
    return result



def my_reverse(str):
    return str[::-1]



def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])



def histogram(arr):
    for num in arr:
        print('*'*num)
        time.sleep(0.5)




def caesar_cipher(s, k):
    result = ""
    for c in s:
        if not c.isalpha():
            result += c
        else:
            if c.isupper():
                if (ord(c) + k) not in range(65, 91):
                    result += chr(ord('A') + (ord(c) + k) % 26)
                else:
                    result += chr(ord(c) + k)
            else:
                if (ord(c) + k) not in range(97, 123):
                    result += chr(ord('a') + (ord(c) + k) % 26)
                else:
                    result += chr(ord(c) + k)
    return result



def diagonal_reverse():
    file_input = open('input_matrix.txt', 'r')
    matrix = [list(map(int, line.split(' '))) for line in file_input]
    rev_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    return rev_matrix



def game(start, finish):
    magic_number = randint(start, finish)
    user_input = int(input("Please enter a random number from {0} to {1}: ".format(start, finish)))
    while user_input != magic_number:
        print("Ooopps! You didn't guess the number. Try again!")
        user_input = int(input("Please enter a random number from {0} to {1}: ".format(start, finish)))
    else:
        print("Ooohhoo! Congrats! You guessed the number! ")
        time.sleep(2)
        print("Game over! Bye!")




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
        return print("OK")
    else:
        return print("NOT OK")


def char_freq(String):
    dictionary = {String[0]:1}
    for char in String[1:]:
        if char in dictionary.keys():
            value = dictionary.get(char)
            value += 1
            dictionary[char] = value
        else:
            dictionary2 = {char:1}
            dictionary.update(dictionary2)
    return dictionary



def dec_to_bin(integer):
    if integer != 1:
        dec_to_bin(integer//2)
    print(integer % 2, end='')



def ship_battle(order):
    print("************Welcome to Battleship Game!************")
    x = randint(0, order)
    y = randint(0, order)
    print(x, y)
    var1, var2 = input("Enter two number here: ").split(' ')
    while int(var1) != x or int(var2) != y:
        print("You missed! Please try again!")
        time.sleep(0.5)
        var1, var2 = input("Enter two number here: ").split(' ')
    else:
        print("Congrats! You sunk my battleship!")
