'''
Created on Aug 8, 2021

@author: Wyatt Meehan
'''


def hello_world():
    print("Hello World")
    
def func1(name):
    print("\nHi my name is {}".format(name))
    
def func3(x, y, z):
    if z == True:
        return x
    else: return y

def func4(x, y):
    return x * y

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

def is_greater_than(x, y):
    if x > y:
        return True
    else:
        return False
    
def sum_of(*args):
    sum_of = 0
    for x in args:
        sum_of += x
    return sum_of

def get_evens(*args):
    evens = []
    for x in args:
        if x % 2 == 0:
            evens.append(x)
    return evens       

def even_odd_string(string_1):
    new_str = ""
    for letter in string_1:
        if ord(letter) % 2 == 0:
            new_str += letter.upper()
        else: new_str += letter.lower()
    return new_str

def greater_lesser(x, y):
    if x % 2 == 0 and y % 2 == 0:
        if x > y: 
            return y
        else:
            return x
    else:
        if x > y:
            return x
        else:
            return y
        
def start_same(x, y):
    if x[0].upper() == y[0].upper():
        return True
    else:
        return False
    
def twice_as_far(x):
    if x > 7:
        return 7 - ((x - 7) * 2)
    elif x == 7:
        return 7
    else:
        return 7 + ((7 - x) * 2)
    
def first_forth(cap_str):
    new_cap = ""
    for x in range(0,len(cap_str)):
        if x == 0 or x == 3:
            new_cap += cap_str[x].upper()
        else:
            new_cap += cap_str[x]
    return new_cap     
if __name__ == '__main__':
    
    # 1)
    hello_world()
    
    # 2)
    func1("Wyatt")
    
    # 3)
    print(func3("\nYes", "\nNo", True))
    print(func3("Yes\n", "No\n", False))
    
    # 4)
    print(func4(4, 5))
    print(func4("hi", 5))
    
    # 5)
    print("\n", is_even(2))
    print(is_even(1), "\n" )
    
    # 6)
    print(is_greater_than(11, 10))
    print(is_greater_than(10, 10))
    print(is_greater_than(9, 10))
    
    # 7)
    print("\n" , sum_of(5, 6, 10))
    print(sum_of(-5, 6, 10, 100, -20.50))
    
    # 8)
    print("\n", get_evens(1,2,3,4,5,6,7,8,9, 100, 0, 102, -1000))
    
    # 9)
    print(even_odd_string("Hello World"))
    
    # 10)
    print("\n",greater_lesser(20, 22))
    print(greater_lesser(20, 23), "\n",)
    
    # 11)
    print(start_same("Hello", "Hi"))
    print(start_same("Hello", "hello"))
    print(start_same("Hello", "trello"), "\n")
    
    # 12)
    print(twice_as_far(5))
    print(twice_as_far(9))
    print(twice_as_far(50))
    print(twice_as_far(4))
    
    # 13) 
    print("\n", first_forth("Hello"))
    print("\n", first_forth("Testing"))
    
    
    
    
    
    
    
    
    
    
    