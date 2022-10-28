# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# ex 5  funtiile str.startswith   and str.endswith
# ex 9 *args  and **kwargs
# ex3 farcuregem cheile uni dictionar  -- putem sa faem flatters,  dintr-un dictionar cu mai multe niveluri facem un dictionar cu un singur nivel,
# ex3 trebuie sa returnam o lista de diferente.

# exercitiul 1
def operatii(list1_1,list1_2):
    set1=set(list1_1)
    set2=set(list1_2)
    intersect= set1.intersection(set2)
    reunion=set1.union(set2)
    list1_1_dif_list1_2= set1.difference(set2)
    list1_2_dif_list1_1= set2.difference(set1)
    return reunion,intersect, list1_1_dif_list1_2, list1_2_dif_list1_1


# exercitiul 2
def function_2(string):
    dict={}
    for i in string_2:
        if i !=' ':
            dict[i] = string.count(i)
    return dict

# exercitiul 4


def build_xml_element(tag, content, href, _class, id):

    string_4= f"<{tag} href=\"{href}\"_class=\"{_class}\"id=\"{id}\"> {content} </{tag}>"
    return  string_4


# exercitiul 6

def function_6(list_6):
    set_6 = set(list_6)
    b = len(list_6) - len(set_6)
    a = 0
    for i in set_6:
        if list_6.count(i) == 1:
            a = a + 1
    return (a, b)


# exercitiul 7
def function_7(*sets):
    dict = {}
    for i in sets:
        for j in sets:
            if sets.index(i) > sets.index(j): # pentru a evita duplicate
               dict['{}|{}'.format(i,j)] = i.union(j)
               dict['{}&{}'.format(i,j)] = i.intersection(j)
               dict['{}-{}'.format(i,j)] = i.difference(j)
               dict['{}-{}'.format(j,i)] = j.difference(i)
    return dict


#exercitiul 9
def function_9(*lists, **key_args):
    nr = 0
    # comparam valorile din lista cu valorile din dictionarul key_args
    for item in lists:
        for kwarg in key_args:
            if item == key_args[kwarg]: # ** operator indica faptul ca key_args trebuie tratati ca formand un dictionar
                nr += 1
    return nr


if __name__ == '__main__':

    #Ex3.1
    print("Ex. 1 =================================")
    list1_1 = [1, 2, 3, 4, 5]
    list1_2 = [1, 3, 5, 7, 9]
    print(operatii(list1_1, list1_2))

    # Ex3.2
    print("Ex. 2 =================================")
    string_2=input("Enter a string: ")
    print(function_2(string_2))
    # Ex3.3
    print("Ex. 3 =================================")
    # Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
    # Dict2 = {1: 'Geeks22', 2: 'For22', 3: 'Geeks22'}
    # dict= {1: Dict, 2: 2, 3: Dict2}
    # compare(dict, Dict)
    # Ex3.4
    print("Ex. 4 =================================")
    string_4=build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid ")
    print(string_4)
    # Ex3.5
    print("Ex. 5 =================================")
    # Ex3.6
    print("Ex. 6 =================================")
    print(function_6([1, 2, 3, 2, 5]))
    # Ex3.7
    print("Ex. 7 =================================")
    print(function_7({1, 2}, {2, 3},{5,6,8}))
    # Ex3.8
    print("Ex. 8 =================================")
    # Ex3.9
    print("Ex. 9 =================================")
    print(f"The number of positional arguments whose values can be found among keyword arguments values is: {function_9(1, 2, 3, 4, x=1, y=2, z=3, w=5)}")