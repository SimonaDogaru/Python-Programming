# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# exercitiul 1

import os
import sys

def function1(director):
    list_e = []
    continut = os.listdir(director)
    for i in continut:
        if os.path.isfile(i):
            if '.' in i:
                j = i.rindex('.')
                if i[j:] not in list_e:
                    list_e.append(i[j:])
    list_e.sort()
    return list_e


# exercitiul 2

def function2(director, fisier):
    continut = os.listdir(director)
    f = open(fisier, "w")
    for i in continut:
        if i.startswith('A') and os.path.isfile(i):
            f.write(os.path.abspath(i) + "\n")
    f.close()


# exercitiul 3

def SortSecondElemTupla(aTuple):
    return aTuple[1]


def ExtensiiDirector(path):
    list = []
    c = os.listdir(path)
    for i in c:
        if os.path.isfile(i):
            j = i.rindex('.')
            list.append(i[j:])
        elif os.path.isdir(i):
            k = ExtensiiDirector(i)
            list.extend(k)
        elif '.' in i:
            j = i.rindex('.')
            list.append(i[j:])
    return list

def sortSecondElemTupla(aTuple):
    return aTuple[1]

def function3(my_path):
    if os.path.isfile(my_path):
        f = open(my_path, "r")
        content = f.read()
        return content[-20:]

    if os.path.isdir(my_path):
        extList = ExtensiiDirector(my_path)
        finalList = []
        for i in extList:
            finalList.append((i, extList.count(i)))
        finalList = set(finalList)
        finalList = list(finalList)
        finalList.sort(key = sortSecondElemTupla,reverse=True)
        return finalList



# exercitiul 4

# terminal -> comanda: py ./main.py ./

def function4(path):
    continut = os.listdir(path)
    list = []
    to_delete=[]
    for i in continut:
        if not os.path.isdir(i) and '.' in i:
            j = i.rindex('.')
            list.append(i[j:])
    for i in list:
        if list.count(i) > 1:
            to_delete.append(i)   # evit stergerea din lista si parcurgerea ei in acelasi timp!
    for j in to_delete:
        list.remove(j)
    list.sort()
    return list

# exercitiul 5

def searchInFile(target, to_search):
    f = open(target, "r")
    continut = f.read()
    if to_search in continut:
        return True
    return False


def searchInFolder(target, to_search):
    list = []
    continut = os.listdir(target)
    for i in continut:
        if os.path.isfile(target + '/' + i): #ca sa ajunga la fisier, i-am dat calea de forma: target/file
            if searchInFile(target + '/' + i, to_search):
                list.append(i)
        elif os.path.isdir(target + '/' + i):
            k = searchInFolder(target + '/' + i, to_search)
            list.extend(k)
    return list


def searchInTarget(target, to_search):
    List = []
    try:
        if os.path.isfile(target):
            if searchInFile(target, to_search):
                List.append(target)
        elif os.path.isdir(target):
            aux = searchInFolder(target, to_search)
            List.extend(aux)
        else:
            raise ValueError()
        return List
    except ValueError as ve:
        print("Eroare la cautare continut fisier")
        #print(ve)  # nu afiseaza text



# exercitiul 6

# not very sure about
def CallBack(e):
    print(e)

def searchInFile6(target, to_search):
    f = open(target, "r")
    continut = f.read()
    if to_search in continut:
        return True
    return False


def searchInFolder6(target, to_search):
    list = []
    continut = os.listdir(target)
    for i in continut:
        if os.path.isfile(target+'/'+i):
            if searchInFile6(target+'/'+i, to_search):
                list.append(i)
        elif os.path.isdir(target+'/'+i):
            k = searchInFolder6(target+'/'+i, to_search)
            list.extend(k)
    return list


def searchInTarget6(target, to_search, callback):
    List = []
    try:
        if os.path.isfile(target):
            if searchInFile6(target, to_search):
                List.append(target)
        elif os.path.isdir(target):
            aux = searchInFolder6(target, to_search)
            List.extend(aux)
        else:
            raise ValueError()
        return List
    except ValueError as ve:
        callback("Eroare la cautare continut fisier")
        # callback(ve)


# exercitiul 7

def funtion7(file):
    dict = {"full_path": os.path.abspath(file),
            "file_size": os.path.getsize(file)} #  os.path.getsize returneaza dimensiunea in Bytes
    if '.' in file:
        j = file.rindex('.')
        dict["file_extension "] = file[j:]
    else:
        dict["file_extension "] = ""
    try:
        with open(file) as f:
            s = f.read()
            dict["can_read"] = True
    except IOError as x:
        dict["can_read"] = False

    try:
        with open(file, 'w') as f:
            dict["can_write"] = True
    except IOError as x:
        dict["can_write"] = False
    return dict


# exercitiul 8
def function8(dir_path):
    List = []
    continut = os.listdir(dir_path)
    for i in continut:
        if os.path.isfile(i):
            List.append(os.path.abspath(i))
    return List


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #Ex4.1
    print("Ex. 1 =================================")
    director = '.'  #directorul curent
    print(function1(director))
    # Ex4.2
    print("Ex. 2 =================================")
    director = '.'
    fisier = 'file2.txt'
    function2(director, fisier)
    # Ex4.3
    print("Ex. 3 =================================")
    director = '.'
    fisier = 'Afile.txt'
    print(function3(fisier))
    print(function3(director))
    # Ex4.4
    print("Ex. 4 =================================")
    # terminal -> comanda: py ./main.py ./
    print(function4(sys.argv[1]))
    # Ex4.5
    print("Ex. 5 =================================")
    file = "./Afile.txt"
    folder = "./Folder"
    folder_error = "./NotExist"
    to_seach = "text_cautat"

    print(searchInTarget(file, to_seach))
    print(searchInTarget(folder, to_seach))
    print(searchInTarget(folder_error, to_seach))
    # Ex4.6
    print("Ex. 6 =================================")
    file = "./Afile.txt"
    folder = "./Folder"
    folder_error = "./NotExist"
    to_seach = "text_cautat"

    print(searchInTarget6(file, to_seach, CallBack))
    print(searchInTarget6(folder, to_seach,CallBack))
    print(searchInTarget6(folder_error, to_seach, CallBack))
    # Ex4.7
    print("Ex. 7 =================================")
    print(funtion7("Afile.txt"))
    # Ex4.8
    print("Ex. 8 =================================")
    print(function8("."))

