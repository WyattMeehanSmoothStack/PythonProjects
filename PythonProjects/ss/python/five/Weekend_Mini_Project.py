'''
Created on Aug 10, 2021

@author: Wyatt Meehan
'''

import requests
from bs4 import BeautifulSoup


def getHTML():
    webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')
    webpage = webpage_response.content
    return webpage

if __name__ == '__main__':
    
    soup = BeautifulSoup(getHTML(), 'html.parser')

    print(soup.prettify())
    
    
    