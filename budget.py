class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.funds = 0

    def check_funds(self, amount):
        if amount <= self.funds: return True
        else: return False
    
    def deposit(self, amount, description=''):
        self.funds += amount
        self.ledger.append({'amount':amount, 'description':description})


    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.funds -= amount
            self.ledger.append({'amount':-amount, 'description':description})
            return True
        else:
            print('Not sufficient funds')
            return False
        
    def get_balance(self):
        print(self.funds)
        return self.funds
    
    def transfer(self, amount, varname):
        if self.check_funds(amount):
            self.funds -= amount
            self.ledger.append({'amount':-amount, 'description':f'Transfer to {varname.name}'})
            varname.funds += amount
            varname.ledger.append({'amount':amount, 'description':f'Transfer from {self.name}'})
            return True
        else:
            print('Not sufficient funds')
            return False
    
    def log(self):
        print(self.name.center(30, '*'))
        for pair in self.ledger:
            print(f'{pair["description"].ljust(20)}{str(pair["amount"]).rjust(10)}', end='')
            print('')
        print('-'.center(30, '-'))
        print('Total: ', float(self.funds))
        print('\n')

def spend_chart(cat_names):
    amounts = [p['amount'] for name in cat_names for p in name.ledger if p['amount'] < 0]
    spent = {}
    [spent.setdefault(name.name, []).append(p['amount']) for name in cat_names for p in name.ledger if p['amount'] < 0]
    spent = {k:sum(v) for k, v in spent.items()}
    totalspent = sum(spent.values())
    med = totalspent 

    print(spent, amounts, totalspent)