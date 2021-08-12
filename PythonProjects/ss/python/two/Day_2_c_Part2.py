"""
Created on Aug 5, 2021

@author: Wyatt Meehan
"""

if __name__ == '__main__':
    
    # Method for testing room crowdedness 
    def crowd_test(name_lis):
        if len(name_lis) > 5:
            print("There is a mob in the room.")
        elif len(name_lis) > 2:
            print("The room is crowded.")
        elif len(name_lis) > 0:
            print("The room is not crowded.")
        else:
            print("The room is empty.")
    
    # List creation
    name_list = ["Kat", "Wyatt", "Kieran", "Josh", "Sam", "Bailey"]
    crowd_test(name_list)
    
    name_list.pop(0)
    