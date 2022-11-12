import utils

if __name__ == '__main__':

    # Lab5.1
    print("Ex. 1 =================================")
    while True:
        in_x = input("Give me a number:")
        if in_x == 'q':
            break
        print(utils.process_item(int(in_x)))
