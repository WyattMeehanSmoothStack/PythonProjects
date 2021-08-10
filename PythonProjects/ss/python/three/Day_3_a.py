'''
Created on Aug 5, 2021

This python file is for solving python problems Day_3_A

@author: Wyatt Meehan
'''
import random


def divisible_by():
        for x in range(1500, 2701):
            if x % 7 == 0 and x % 5 == 0:
                print(x, end=", ")

               
def cel_to_fahr():
    while True:
        try:
            temp = float(input("\n\nPlease enter the degrees in Celsius you would like converted: \n"))
            print("{0:0.2f} Degrees Celcius = {1:0.2f} Degrees Fahrenhiet".format(temp, temp * 1.8 + 32))
            break
        except ValueError:
            print("Invalid input, please try again\n")

                    
def fahr_to_cel():
    while True:
        try:
            temp = float(input("\n\nPlease enter the degrees in Fahrenhiet you would like converted: \n"))
            print("{0:0.2f} Degrees Fahrenhiet = {1:0.2f} Degrees Celsius".format(temp, (temp - 32) * 5 / 9))
            break
        except ValueError:
            print("Invalid input, please try again\n")
                    

def random_guess():
    rand_num = random.randint(1, 10)
    while True:
        try:
            temp = int(input("\nPlease guess an integer 1 - 10\n"))
            if temp == rand_num:
                print("\nYou guessed correctly! Thanks for playing.\n")
                break
            else:
                print("\nIncorrect guess, please try again\n")
                print(rand_num)
                continue
        except ValueError:
            print("Invalid input, please try again\n")
                    

def print_pattern():
    pattern = ""
    for x in range(0, 9):
        if x < 5:
            pattern += "*"
            print(pattern)
        else:
            pattern = pattern[:-1]
            print(pattern)


def reverse_word():
    while True:
        try:
            rev_str = str(input("\nPlease enter the thing you would like reversed:\n"))
            print(rev_str[::-1])
            break
        except ValueError:
            print("Invalid input, please try again\n")
                    

def count_evenodd(eo_list):
    evens = 0
    odds = 0
    for num in eo_list:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    print("\nNumber of even numbers: {}".format(evens))
    print("Number of odd numbers: {}\n".format(odds))

    
def print_types(type_list):
    for thing in type_list:
        print("Thing: {}             Type: {}".format(thing, type(thing)))

        
def print_nums():
    print("\n")
    for x in range(0, 7):
        if x == 3 or x == 6:
            continue
        else: 
            print(x)
            
            
if __name__ == '__main__':
    
    # 1) 
    divisible_by()
            
    # 2)
    cel_to_fahr()
    fahr_to_cel()
    
    # 3)
    random_guess()
    
    # 4)
    print_pattern()
    
    # 5)
    reverse_word()
    
    # 6)
    eo_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 0, 102, -1000]
    count_evenodd(eo_list)
    
    # 7)
    datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    print_types(datalist)
    
    # 8)
    print_nums()
    
