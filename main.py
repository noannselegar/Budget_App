from budget import *

food = Category('FOOD')
shopping = Category('SHOPPING')
clothing = Category('CLOTHING')


clothing.deposit(100, 'initial deposit')
shopping.deposit(300, 'initial deposit')
food.deposit(600, 'initial deposit')

food.withdraw(10.50)
shopping.withdraw(11.50)
food.withdraw(5.50)
shopping.withdraw(70)
clothing.withdraw(99)
food.transfer(75.89, shopping)

#food.log()
#shopping.log()
#clothing.log()


#spend_chart([food, shopping, clothing])