import pickle

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.funds = 0

    def check_funds(self, amount):
        if float(amount) <= self.funds: return True
        else: return False
    
    def deposit(self, amount, description=''):
        amount = float(amount)
        self.funds += amount
        self.ledger.append({'amount':amount, 'description':description})


    def withdraw(self, amount, description=''):
        amount = float(amount)
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
        amount = float(amount)
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
        print(f'Total: {float(self.funds):.2f}')
        print('\n')

def save_dict(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)

def load_dict(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)

def spend_chart(cat_names):
    def catch(k, i):
        try:
            return k[i]
        except:
            return ' '
    
    spent = {}
    [spent.setdefault(name.name, []).append(p['amount']) for name in cat_names for p in name.ledger if p['amount'] < 0 and not p['description'].startswith('Transfer')]
    spent = {k:sum(v) for k, v in spent.items()}
    totalSpent = sum(spent.values())
    percentSpent = {k:(int((v/totalSpent)*100)) for k, v in spent.items()}
    sortedwords = sorted([k for k in percentSpent.keys()], key=len)
    letterList = [catch(k, i) for i in range(len(sortedwords[-1])) for k in percentSpent.keys()]

    z = 110
    for y in range(11):
        z -= 10
        print(f'{z}|'.rjust(4), end='')
        for k, v in percentSpent.items():
            if v >= z:
                print(' o ', end='')
        else:
            print('')
    else:
        print('    '.ljust(len(spent)*4, '-'))
        for i in range(0, len(letterList), len(percentSpent)):
            print('    ', end='')
            for let in letterList[i:i+len(percentSpent)]:
                print(f' {let}', end=' ')
            else:
                print('')

        