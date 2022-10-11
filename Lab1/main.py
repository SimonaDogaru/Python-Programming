# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

"""
for i,x in enumerate(listName)
    i- index
    x- val
"""

import  math
import re

#ex1
def GCD(numbers):
    last_gcd = math.gcd(numbers[0], numbers[1])
    for number in numbers[2:len(numbers)]:
        last_gcd = math.gcd(last_gcd, number)
    return last_gcd


#ex2
def vowels_number(some_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    number_of_vowels = 0
    for letter in some_string:
        if letter in vowels:
            number_of_vowels += 1
       # print(f"vocala {letter} numer of vocale {number_of_vowels}")
    return number_of_vowels


#ex4
def camel_to_snake(string_input):
    # this expression - recognize the UpperCase letter isn't the first letter of the string
    # when a letter matches, then '_' will be plased on the left of the letter
     return re.sub(r'(?<!^)(?=[A-Z])', '_', string_input).lower()


#ex5.1
def read_characters_matrix(dimension):
    matrix = []
    for index1 in range(dimension):
        line = []
        word = input()
        for letter in word:
            line.append(letter)
        matrix.append(line)
    return matrix


#ex5.2
def spiral_order(matrix,dimension):
    s = ""
    nr_square = 0  # this var. will memorize how many square are in the matrix
    while nr_square < dimension / 2:
        for index2 in range(nr_square, dimension - nr_square):
            s = s + matrix[nr_square][index2]
        index2 = dimension - 1 - nr_square
        for index1 in range(nr_square + 1, dimension - nr_square):
            s = s + matrix[index1][index2]
        index1 = index2
        for index2 in range(dimension - 2 - nr_square, nr_square - 1, -1):
            s = s + matrix[index1][index2]
        for index1 in range(dimension - 2 - nr_square, nr_square, -1):
            s = s + matrix[index1][nr_square]
        nr_square += 1
    return s

#ex6
def is_palindrome(number):

    if str(number) == str(number)[::-1]:
        return "Palindrome"
    else:
        return  "Not a palindrome"

#ex7
def first_number_from_string(string_input):
    number = 0;
    find_number = 0
    for letter in string_input:
        if '0' <= letter and letter <= '9':
            find_number = 1
            number = number * 10 + (int(letter) - int('0'))
        else:
            if find_number == 1:
                break

    return number

#ex8
def counts_bits_1(number):
    count = 0
    while number > 0:
        count += number % 2
        number = number // 2
    return count

#ex9
def print_the_frequent_char(string_input):
    letterlist = [0] * 26  # create a frequency list for the charactes
    string_input = string_input.lower()
    maxim = 0
    for letter in string_input:
        if 'a' <= letter and letter <= 'z':
            index = (ord(letter) - ord('a'))
            letterlist[index] += 1
            if letterlist[index] > maxim:
                maxim = letterlist[index]
                letter_max = chr(index + ord('a'))

    print(letter_max, maxim)

#ex10  - I make sure that tha string_input is trimed, so I have spaces only between words.
#I just have to count the whitespaces and add 1, to find the correct result
def number_of_words(string_input):
    string_input = string_input.strip()
    count_whitespaces = 0
    for letter in string_input:
        if letter == ' ':
            count_whitespaces += 1
    number_of_words = count_whitespaces + 1
    return number_of_words


if __name__ == '__main__':


    # Lab1.1
    # Get the numbers
    print("Ex. 1 =================================")
    print("How many numbers: ")
    length = int(input())
    numbers = []
    while length > 0:
        numbers.append(int(input()))
        length -= 1

    print(f" The GCD of all number is : {GCD(numbers)}")


    # Lab1.2
    print("Ex. 2 =================================")
    string2 = input("Enter a string: ");
    print(f"The numbers of vowels in the string is: {vowels_number(string2)}")

    #Lab1.3
    print("Ex. 3 =================================")
    string3_1= input("Enter the first string: ")
    string3_2= input("Enter the second string: ")
    print(f"The {string3_1} appears in {string3_2} for {string3_2.count(string3_1)} times")

    #Lab1.4
    print("Ex. 4 =================================")
    string4 = input("Enter a camelCase string:  ")
    print(f"The snake format for {string4} is : {camel_to_snake(string4)}")

    #Lab1.5
    print("Ex. 5 =================================")
    # read the matrix
    dimension = int(input("Enter the dimension of the square matix: "))
    matrix = read_characters_matrix(dimension)
    print(f"The spiral reading result is : {spiral_order(matrix, dimension)}")

    #Lab1.6
    print("Ex. 6 =================================")
    number6 = int(input("Enter a number: "))
    print(f"The number {number6} is : {is_palindrome(number6)}")

    #Lab1.7
    print("Ex. 7 =================================")
    string7 = input("Enter a string: ")
    print(f" The first number is : {first_number_from_string(string7)}")

    #Lab1.8
    print("Ex. 8 =================================")
    number8 = int(input("Enter a number: "))
    print(f"The numbers of bits with value 1 is : {counts_bits_1(number8)}")

    #Lab1.9
    print("Ex. 9 =================================")
    string9 = input("Enter a string: ")
    print("The frequent character and his number of occurrences is: "), print_the_frequent_char(string9)


    #Lab1.10
    print("Ex. 10 =================================")
    string10=input("Enter a string: ")
    print(f" In the input string are {number_of_words(string10)} words")












