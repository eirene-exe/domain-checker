import requests
from os import system

clear = lambda: system('cls||clear')
system('title Eirene Domain-Checker')
clear()


domain = input('Enter your domain: ')

url = f'https://{domain}'


try:
    response = requests.get(url)
    print('Busy')
except Exception:
    print('Free')