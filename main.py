from budget import *
from collections import defaultdict

categoryDict = defaultdict()
run = True
print('Welcome! What do you wanna do? (press Enter to review options)')
categoryDict = load_dict('data.pickle')

while run==True:
    command = input('What next? ')
    if command == '':
        print('1) Create new category')
        print('2) Deposit')
        print('3) Withdraw')
        print('4) Transfer')
        print('5) Check the logs of a category')
        print('6) Check Spend Chart')
        print('7) Quit')

    if command == '1':
        cat1 = input('Category name: ').split()
        for _ in range(len(cat1)):
            categoryDict[cat1[_]] = Category(cat1[_])
    if command == '2':
        val_cats = input('List category(ies) and values to deposit: ').split()
        for _ in range(len(val_cats)//2):
            categoryDict[val_cats[_]].deposit(val_cats[_+len(val_cats)//2])
    if command == '3':
        val_cats = input('List category(ies) and values to withdraw: ').split()
        for _ in range(len(val_cats)//2):
            categoryDict[val_cats[_]].withdraw(val_cats[_+len(val_cats)//2])
    if command == '4':
        value, fromCat, toCat = input('Transfer how much from which category to which? ').split()
        categoryDict[fromCat].transfer(value, categoryDict[toCat])
    if command == '5':
        cat5 = input('Check the logs for which category(ies)? ').split()
        for _ in range(len(cat5)):
            categoryDict[cat5[_]].log()
    if command == '6':
        print('')
        spend_chart(list(categoryDict.values()))
    if command == '7':
        run=False

save_dict(categoryDict)
