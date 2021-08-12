"""
Created on Aug 5, 2021

@author: Wyatt Meehan
"""

if __name__ == '__main__':

    # 1)
    my_list = [1, "Hello", 10.99]
    print(my_list)

    # 2)
    nest_list = [1, 1, [1, 2]]
    print(nest_list[2][1])

    # 3)
    lst = ['a', 'b', 'c']
    print(lst[1])

    # 4)
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday",
            4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

    # 5) 
    d = {"k1": [1, 2, 3]}
    print(d['k1'][1])

    # 6)
    con_list = [1, [2, 3]]
    con_tup = tuple(con_list)
    print(con_tup)

    # 7)
    mis_set = "".join(set("Mississippi"))
    mis_set = set(mis_set)
    print(mis_set)

    # 8) 
    mis_set.add('X')
    print(mis_set)

    # 9)
    print(set([1, 1, 2, 3]))

    # Question 1

    for x in range(2000, 3201):
        if x % 7 == 0 and x % 5 != 0:
            print(x, end=", ")

    # Quesiton 2 
    print("\n")


    def fact(x_var):
        if x_var == 0:
            return 1
        return x_var * fact(x_var - 1)


    while True:
        try:
            x = int(input("Please enter the number you would like factorial: \n"))
            break
        except ValueError:
            print("Invalid input, please try again\n")

    print(fact(x))

    # Question 3
    print("\n")
    while True:
        try:
            x = int(input("Please enter the max dictionary number: \n"))
            break
        except ValueError:
            print("Invalid input, please try again\n")

    d = dict()
    for i in range(1, x + 1):
        d[i] = i * i

    print(d)

    # Question 4
    values = input("\nPlease enter a comma separated list of numbers: \n")
    comma_lis = values.split(",")
    comma_tup = tuple(comma_lis)
    print(comma_lis)
    print(comma_tup)

    # Question 5
    class InputOutString(object):
        def __init__(self):
            self.s = ""

        def get_string(self):
            self.s = input("\nEnter a test value for the object:\n")

        def print_string(self):
            print(self.s.upper())


    strObj = InputOutString()
    strObj.getString()
    strObj.printString()
