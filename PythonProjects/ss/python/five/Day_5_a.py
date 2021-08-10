'''
Created on Aug 9, 2021

This python file is for solving python problems Day_5_A

@author: Wyatt Meehan
'''

# Get a valid integer from 1-5 from the user
def get_number():
    while True:
        try:
            number = int(input("\nPlease enter the number of BMI's you would like to calculate (5 max):\n"))
            if number <= 0 or number > 5:
                print("Invalid input, please try again\n")
                continue
            return number
        except ValueError:
            print("Invalid input, please try again\n")
            continue        


# Get a valid integer from 1-5 from the user
def get_bmis(num):
    bmis = []
    for x in range(0, num):
        while True:
            try:
                ques = "\nPlease enter the weight (kg) and height (m) separated by a space (entry {}/{}):\n".format(x + 1, num)
                weight, height = input(ques).split(" ")
                weight = float(weight)
                height = float(height)
                bmis.append(weight / (height) ** 2)
                break
            except ValueError:
                print("Invalid input, please try again\n")
                continue
    return bmis    

# Get grades and print them based on BMI
def get_grades(bmis):
    grades = []
    for bmi in bmis:
        if bmi >= 30.0:
            grades.append("obesity")
            print("obesity", end=" ")
        elif bmi >= 25.5:
            grades.append("overweight")
            print("overweight", end=" ")
        elif bmi >= 18.5:
            grades.append("normal")
            print("normal", end=" ")
        else:
            grades.append("udnerweight")
            print("underweight", end=" ")

       
if __name__ == '__main__':
    get_grades(get_bmis(get_number()))
    
