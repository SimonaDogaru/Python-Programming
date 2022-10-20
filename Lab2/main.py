# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import  numpy as np

def Fibbo_N(n):
    list_fibo=[1,1]
    iteration=2
    while iteration < n:
        list_fibo.append(list_fibo[iteration-1]+list_fibo[iteration-2])
        iteration+=1
    return  list_fibo


#ex 2
def is_prim(number):
    for a in range(2, number):
        if number % a == 0:
            return False
    return True


def numerePrime(list):
    prime_list= []
    for number in list:
        if is_prim(number):
            prime_list.append(number)
    return prime_list


# ex3
def operatii(list1 , list2):
    intersectare = []
    for item in list1:
        if item in list2 :
            intersectare.append(item)
    reuniune = []
    for item in list1+list2:
        if item not in reuniune:
            reuniune.append(item)
    aminusb = []
    for item in list1:
        if item not in list2:
            aminusb.append(item)
    bminusa = []
    for item in list2:
        if item not in list1:
            bminusa.append(item)
    return intersectare, reuniune, aminusb, bminusa


# ex4
def compose(notes, moves, start):
    i = 0
    pos = start
    final_list = [notes[pos]]
    while i != len(moves):
        pos = abs(pos + moves[i]) % 5 # pentru ca sunt  5 note muzicale
        final_list.append(notes[pos])
        i = i+1
    return final_list


# ex5
def underMainDiagonal(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > j:
                matrix[i][j] = 0
    return matrix

#ex 6
# deoarece *lists este numar variabil de param, am pus x la inceput
def x_items( x, *lists):
    list = []
    finalList = []
    for i in lists:
        list = list + i
    print(list)
    for i in list:
        if list.count(i) == x and i not in finalList:
            finalList.append(i)
    return finalList

#ex 7
def is_palindrome(number):

    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

def howManyPalindromes(list):
    counter = 0
    greatest = 0
    for number in list:
        if is_palindrome(number):
            counter += 1
            if number > greatest:
                greatest = number
    myTuple = (counter, greatest)
    return myTuple


#ex8
def function_8(listStrings, flag, x = 1):
    myList = []
    if flag:
        for i in listStrings:
            miniList = []
            for j in i:
                if ord(j) % x == 0:
                    miniList.append(j)
            if len(miniList) > 0:
                myList.append(miniList)
    else:
        for i in listStrings:
            miniList = []
            for j in i:
                if ord(j) % x != 0:
                    miniList.append(j)
            if len(miniList) > 0:
                myList.append(miniList)
    return myList

#ex 9
def function_9(matrix):
    finalList = []
    matrix = matrix.T # transpusa, am considerat ca este mai usor sa merg pe linii
    for i in range(len(matrix)):
        greatest = matrix[i][0]
        for j in range(1, len(matrix[i])):
            if greatest >= matrix[i][j]:
                myTuple = (j, i)
                finalList.append(myTuple)
            else:
                greatest = matrix[i][j]
    return finalList

# ex 10
def function_10(*lists):

    number_of_lists = len(lists)
    max=0
    for val in range(number_of_lists):
        if max < len(lists[val]):
            max=len(lists[val])
    finalList = []
    for i in range(max):
        miniList = []
        for j in range(number_of_lists):
            if i >= len(lists[j]):
                miniList.append(None)
            else:
                miniList.append(lists[j][i])
        finalList.append(tuple(miniList))
    return finalList


#ex 11
def get_key(Strings):
    #Strings = list(Strings)
    return Strings[1][2] # din cel de-al doilea string iau al treilea caracter


def sort_function(strings):
    strings.sort(key = get_key) # sortez dupa o cheie/valoare aleasa da mine - conform enuntului
    return strings


#ex 12
def group_by_rhyme(list):
    rhymes = []
    for i in list:
        aRhyme = []
        ok = True
        # daca cuvantul mai apare in alte rime dam break
        for j in rhymes:
            for x in j:
                if x in i:
                    ok = False
                    break
        #daca nu mai apare putem sa creem o alta pereche de cuvinte care rimeaza
        if ok:
            aRhyme.append(i)
            for j in list:
                if j[-2:] in i[-2:] and j != i: # daca ultimele 2 litere conincid si
                    aRhyme.append(j)
        if len(aRhyme) != 0:
            rhymes.append(aRhyme)
    return rhymes
# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # Lab2.1
    # Get the numbers
    print("Ex. 1 =================================")
    number1=int(input("Enter a number: "))
    print(f"Primele {number1} din sirul Fibbonaci sunt: ")
    print(Fibbo_N(number1))

    # Lab2.2
    print("Ex. 2 =================================")
    list = [1, 2, 3, 4, 5, 6, 7]
    print(f"Numerele prime din lista {list} sunt: ")
    print(numerePrime(list))

    # Lab2.3
    print("Ex. 3 =================================")
    list2_1 = [1, 2, 3, 4, 5]
    list2_2 = [1, 3, 5, 7, 9]
    print(operatii(list2_1, list2_2))

    #Lab2.4
    print("Ex. 4 =================================")
    myNotes = ["do", "re", "mi", "fa", "sol"]
    myMoves = [1, -3, 4, 2]
    myStart = 2
    print(compose(myNotes, myMoves, myStart))

    # Lab2.5
    print("Ex. 5 =================================")
    matrix = [[1, 4, 5],
              [-5, 8, 9],
              [-6, 7, 11]]
    matrix=underMainDiagonal(matrix)
    for i in range(len(matrix)):
            print(matrix[i])

    # Lab2.6
    print("Ex. 6 =================================")
    print(x_items(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))

    # Lab2.7
    print("Ex. 7 =================================")
    list7 = (1561, 313, 4554, 10001, 7, 89, 9)
    print(howManyPalindromes(list7))

    #Lab2.8
    print("Ex. 8 =================================")
    print(function_8( ["test", "hello", "lab002"], False, 2))

    #Lab 2.9
    print("Ex. 9 =================================")
    myMatrix = np.array([[1, 2, 3, 2, 1, 1],
                         [2, 4, 4, 3, 7, 2],
                         [5, 5, 2, 5, 6, 4],
                         [6, 6, 7, 6, 7, 5]])
    print(function_9(myMatrix))

    #Lab 2.10
    print("Ex. 10 =================================")
    print(function_10([1, 2, 3], [5, 6, 7], ["a", "b", "c","d"]))

    #Lab 2.11
    print("Ex. 11 =================================")
    print(sort_function([('abc', 'bcd'), ('abc', 'zza'),('abc', 'ddb')]))

    # Lab2.12
    print("Ex. 12 =================================")
    print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))