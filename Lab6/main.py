import re
import  os

#ex1
def function1(string1):
    return re.split("[^0-9a-z'A-Z]+", string1)

#ex2
def function2(regex, string2, x):
    result = re.findall(regex, string2)
    list_of_substrings=[]
    for item in result:
        if len(item)== x:
            list_of_substrings.append(item)
    return list_of_substrings

#ex3
def function3(string, regexs):
    set_r=set()
    for r in regexs:
        result = re.findall(r,string)
        set_r.update(result)
    return set_r


#ex6
def convert(word):
    new_word=""
    for i in range(len(word)):
        if i%2!=0:
            new_word+='*'
        else:
            new_word+=word[i]
    return new_word


def function6(string):
    r= re.compile("^[AEIOUaeiou].*[AEIUOaeiou]$")
    new_string=""
    list_words= function1(string)
    for word in list_words:
        if r.match(word):
            word=str(convert(word))
        new_string=new_string + " " +word
    return  new_string


#ex8

def directory_re(dir, regex):
    r= re.compile(regex)
    continut= os.listdir(dir)
    for item in continut:
        ok=0
        if os.path.isfile(item) == True:
            name=item
            name=name[0:name.rindex('.')]
            if r.match(name):
                ok+=1
            file =open(os.path.abspath(item),'r')
            if r.search(file.read()):
                ok+=1
            if ok ==2:
                print(">>"+item)
            elif ok == 1:
                print(item)
        if os.path.isdir(item) == True:
            directory_re(item,regex)



if __name__ == '__main__':
    s = "Today I'm having a 3part 0980 python course"

    # Lab6.1
    print("Ex. 1 =================================")
    s = "Today I'm having a  3part 0980 python course"
    print(function1(s))
    # Lab6.2
    print("Ex. 2 =================================")

    print(function2("[0-9]+[a-z]*","Color from 3pixel 20,30 is 123",3))
    #Lab6.3
    print("Ex. 3 =================================")
    list=["\d+","!{3}"]
    print(function3("ceva.txt numar 123 si !!!", list))
    #Lab6.4
    print("Ex. 4 =================================")

    #Lab6.5
    print("Ex. 5 =================================")
    #Lab6.6
    print("Ex. 6 =================================")
    string= "Aceste materiale acopera o mare parte a umezelei"
    print(function6(string))
    #Lab6.7
    print("Ex. 7 =================================")

    r=re.compile("5|6[0-9]{2}((0[1-9])|(1[0-2]))(([0-2][0-9])|3[0-1])[0-9]{6}")
    list_CNP=["6000709017281","5070720015026"]
    for cnp in list_CNP:
        if r.match(cnp):
            print(f"{cnp} is a valid CNP")
    #Lab6.8
    print("Ex. 8 =================================")
    print(directory_re(".","[0-9]{2}"))



