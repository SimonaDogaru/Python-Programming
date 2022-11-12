import math


def prim(x):

    for index in range(2, x//2):
        if x % index == 0:
            return False
    return True


def process_item(param1):
    param1 += 1
    while not prim(param1):
        param1 += 1
    return param1
