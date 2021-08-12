'''
Created on Aug 5, 2021

@author: Wyatt Meehan
'''
import string

if __name__ == '__main__':

    # 1) 
    print("Hello World"[8])

    # 2)
    print("Thinker"[2:5])
    s = "hello"
    print(s[1])

    # 3)
    s = "Sammy"
    print(s[2:])

    # 4) 
    print("".join(set("Mississippi")))

    # 5)
    while True:
        try:
            i = int(input("Please enter the number of phrases to enter: "))
            break
        except ValueError:
            print("Invalid input, please try again")

    pal_list = []
    for x in range(1, i + 1):
        ques = "Please enter phrase number %s\n" % (x)
        pal_list.append(input(ques))


    def reverse(stuff_list):
        ans_lis = []
        for thing in stuff_list:
            ans_lis.append(thing.upper().translate(str.maketrans('', '', string.punctuation))
                           == thing[::-1].upper().translate(str.maketrans('', '', string.punctuation)))
        return ans_lis


    ans_list = (reverse(pal_list))
    print("\n")
    for ans in ans_list:
        if ans:
            print('Y', end=" ")
        else:
            print('N', end=" ")
