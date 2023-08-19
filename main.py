from budget import *
from collections import defaultdict
import sys

categoryDict = defaultdict()

print('Welcome! What do you wanna do? ')
print('1) Create new category')
print('2) Deposit')
print('3) Withdraw')
print('4) Transfer')
print('5) Check the logs of a category')
print('6) Check Spend Chart')
print('7) Quit')
command = input()

if command == '1':
    cat = input('Category name: ')
    categoryDict[cat] = Category(cat)
if command == '7':
    exit()

print(categoryDict)
#spend_chart([food, shopping, clothing, rent])