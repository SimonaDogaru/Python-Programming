

#ex1
# see the utils.py and app.py files from Moduls

#ex2

def function2(*args, **kwargs):
    sum = 0
    for i in kwargs.values():
        sum += i
    return sum


nameLess_function2 = lambda *arg, **kwargs: sum(kwargs.values())

#ex3
vowels = ['a', 'e', 'i', 'o', 'u']


def function3(String):
    vowelsInString = []
    for vowel in String:
        if vowel in vowels:
            vowelsInString.append(vowel)
    return vowelsInString

#ex4
def function4(*args, **kwargs):
    list_dictionaries = []
    output_list = []
    for item in args:
        if type(item) is dict:
            list_dictionaries.append(item)
    for item in kwargs.values():
        if type(item) is dict:
            list_dictionaries.append(item)
    for item in list_dictionaries:
        keys = item.keys()
        if len(keys) >= 2:
            min3Characters = False
            for j in keys:
                if len(str(j)) >= 3 and type(j) is str:
                    min3Characters = True
            if min3Characters:
                output_list.append(item)
    return output_list


#ex5
def function5(list):
    output_list = []
    for item in list:
        if type(item) is int or type(item) is float:
            output_list.append(item)
    return output_list


#ex6
def function6(list):
    list_odd = []
    list_even = []
    output_list = []
    for item in list:
        if item % 2 == 0:
            list_even.append(item)
        else:
            list_odd.append(item)
    for item in range(0, len(list_even)):
        output_list.append((list_even[item], list_odd[item]))
    return output_list


#ex7
def Fibonacci(n):
    list = []
    term1= 0
    list.append(term1)
    term2=1
    list.append(term2)
    n -=2
    while n > 0:
        term3 = term1+term2
        list.append(term3)
        term1=term2
        term2=term3
        n -= 1
    return list


def process(**kwargs):
    first1000 = Fibonacci(1000)
    Fibonacci_list = []
    if "filters" in kwargs.keys():
        list_filters = kwargs.get("filters")
        for fibo_number in first1000:
            toSave = True
            for filter in list_filters: # verificam fiecare filtru din lista de filtre
                toSave = toSave and filter(fibo_number)
            if toSave:
                Fibonacci_list.append(fibo_number)
    print(Fibonacci_list)
    if "offset" in kwargs.keys():
        x = kwargs.get("offset")
        Fibonacci_list = Fibonacci_list[x:]
    print(Fibonacci_list)
    if "limit" in kwargs.keys():
        x = kwargs.get("limit")
        Fibonacci_list = Fibonacci_list[:x]
    return Fibonacci_list


#ex8
def multiply_by_three(x):
    return x * 3


def multiply_by_two(x, **kwargs):
    return x * 2 * sum(kwargs.values())


def add_numbers(a, b):
    return a + b


def print_arguments(function):      #subpunctul a

    def subfunction_a(*args, **kargs):
        arg = []
        for item in args:
            arg.append(item)
        arg = tuple(arg)
        dict = {}
        # lista val e folsita pentru a acesa valorile kargs
        val= list(kargs.values())
        index=0
        for item in kargs:
            dict[item] = val[index]
        print("Arguments are: ", arg, dict)
        return function(*args, **kargs)

    return subfunction_a


def multiply_output(function):      #subpunctul b

    def subfuncion_b(*args, **kargs):
        return 2 * function(*args, **kargs)

    return subfuncion_b


def augment_function(function, decorators):     #subpunctul c - functia este facuta pentru exemplul din curs

    def subfuntion_c(*args, **kargs):
        firstFunction = decorators[0](function)
        secondFunction = decorators[1](function)
        return secondFunction(firstFunction(*args, **kargs),0)

    return subfuntion_c


#ex9
def function9(pairs):
    output_list = []
    for item in pairs:
        aDict = {'sum': item[0] + item[1],
                 'prod': item[0] * item[1],
                 'pow': pow(item[0], item[1])
                 }
        output_list.append(aDict)
    return output_list


if __name__ == '__main__':


    # Lab5.2
    print("Ex. 2 =================================")
    print(function2(1, 2, c=3, d=4, y=3))
    print((nameLess_function2(1, 2, c=3, d=4)))
    #Lab5.3
    print("Ex. 3 =================================")

    theString = "Programming in Python is fun"
    print(f"Normal function: {function3(theString)}")

    nameLess_function3 = list(filter(lambda x: x in vowels, theString))
    print(f"Lambda fucntion: {nameLess_function3}")

    # [expression for item in list] -syntax
    listComprehension = [letter for letter in theString if letter in vowels]
    print(f"List comprehensions: {listComprehension}")
    #Lab5.4
    print("Ex. 4 =================================")
    print(
        function4(

            {1345: 2, 3: 4, 5: 6},

            {'a': 5, 'b': 7, 'c': 'e'},

            {2: 3},

            [1, 2, 3],

            {'abc': 4, 'def': 5},

            3764,

            dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},

            test={1: 1, 'test': True}
        ))
    #Lab5.5
    print("Ex. 5 =================================")
    print(function5([1, "2", 3.45, {"3": "a"}, {4, 5}, 5, 6, 3.0]))
    #Lab5.6
    print("Ex. 6 =================================")
    print(function6([1, 3, 5, 2, 8, 7, 4, 10, 9, 2]))
    #Lab5.7
    print("Ex. 7 =================================")

    def sum_digits(x):
        return sum(map(int, str(x)))

    print("Functia returneaza: ", process(filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],  limit=2, offset=2 ))
    #Lab5.8
    print("Ex. 8 =================================")
    # subpunctul a

    augmented_multiply_by_two = print_arguments(multiply_by_two)
    x= augmented_multiply_by_two(10,c=2)
    print(x)

    augmented_add_numbers = print_arguments(add_numbers)
    augmented_add_numbers(3, 4)

    # subpunctul b

    augmented_multiply_by_three = multiply_output(multiply_by_three)
    print(augmented_multiply_by_three(10))

    # subpunctul c

    decorated_function = augment_function(add_numbers, [print_arguments, multiply_output])
    x = decorated_function(3, 4)
    print(x)

    #Lab5.9
    print("Ex. 9 =================================")
    print(function9(pairs = [(5, 2), (19, 1), (30, 6), (2, 2)]))










