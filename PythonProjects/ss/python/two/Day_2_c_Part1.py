'''
Created on Aug 5, 2021

@author: Wyatt Meehan
'''


if __name__ == '__main__':
    
    # Method for testing room crowdedness 
    def crowd_test(name_lis):
        if len(name_lis) > 3:
            print("The room is crowded")
    
    # List creation
    name_list = ["Kat", "Wyatt", "Kieran", "Josh"]
    crowd_test(name_list)
    
    name_list.pop(0)
    
    crowd_test(name_list)
        
        