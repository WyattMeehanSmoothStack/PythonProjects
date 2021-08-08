'''
Created on Aug 5, 2021

@author: Wyatt Meehan
'''

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
            print("{0:0.2f} Degrees Fahrenhiet = {1:0.2f} Degrees Celsius".format(temp, (temp - 32) * 5/9))
            break
        except ValueError:
            print("Invalid input, please try again\n")
                    

if __name__ == '__main__':
    
    # 1) 
    divisible_by()
            
    # 2)
    cel_to_fahr()
    fahr_to_cel()
    
    # 3)
    
