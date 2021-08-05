'''
Created on Aug 4, 2021

@author: Wyatt Meehan
'''

if __name__ == '__main__':
    
    # 1) 
    sumExample = 50 + 50
    print(sumExample)
    diffExample = 100 - 10
    print(diffExample, '\n')
    
    # 2)
    
    test = 6 ^ 6
    print(test)
    
    exponent = 6 ** 6
    print(exponent)
    
    add = 6 + 6 + 6 + 6 + 6
    print(add , '\n')
    
    # 3)
    
    print('Hello World')
    print('Hello World: 10\n')
    
    # 4)
    
    p = float(input("Please enter the loan size:\n"))
    y = float(input("Please enter the interest rate in percentage:\n"))
    n = float(input("Please enter the number of n:\n"))
    
    print('\nInput data ===========================\nLoan: {a} Interest rate: {b}% Months: {c}'
          .format(a = p, b = y, c = n))
    
    r = y/100/12
    
    monthly_payment = p * (r * (1+r) ** n)/((1+r)**n-1)
    
   
    print("\nJoel should pay ${0:0.0f} per month!".format(monthly_payment))
    

        
        
         
        
        
    
    
    
    
    