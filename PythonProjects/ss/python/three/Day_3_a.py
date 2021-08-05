'''
Created on Aug 5, 2021

@author: Wyatt Meehan
'''

if __name__ == '__main__':
    
    for x in range(1500, 2701):
        if x % 7 == 0 and x % 5 == 0:
            print(x, end=", ")
            
