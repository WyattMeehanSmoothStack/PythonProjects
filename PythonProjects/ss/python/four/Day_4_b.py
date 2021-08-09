'''
Created on Aug 9, 2021

@author: Wyatt Meehan
'''



def make_list(order_number, product, quantity, price):
    return[(order_number), (product, quantity, price)]



if __name__ == '__main__':
    # Make the original orders and store in a list
    order1 = make_list(34587, 'Learning Python, Mark Lutz', 4, 40.95)
    order2 = make_list(98762, 'Programming Python, Mark Lutz', 5, 56.95)
    order3 = make_list(77226, 'Head First Python, Paul Barry', 3, 32.95)
    order4 = make_list(88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.95)
    order5 = make_list(99999, 'T3st, Wyatt', 4, 50000)
    order_list = [order1, order2, order3, order4, order5]

    cheap_orders = list(filter(lambda x: x[1][2] * x[1][1] < 10000, order_list))
    print(cheap_orders)    
    cheap_orders = list(map(lambda x: x[1][2] + 10, cheap_orders))
    print(cheap_orders)
    
        
        
        
        
        
        
        
    