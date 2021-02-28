import time
class User:
    def __init__(self , name , age , gender):
        self.name = name
        self.age = age 
        self.gender = gender


class Bank(User):
    def __init__(self , name , age , gender , balance):
        super().__init__(name , age , gender)
        self.balance = balance
    
    def loading(self):
        animation = [
        "[        ]",
        "[=       ]",
        "[===     ]",
        "[====    ]",
        "[=====   ]",
        "[======  ]",
        "[======= ]",
        "[========]",
        "[ =======]",
        "[  ======]",
        "[   =====]",
        "[    ====]",
        "[     ===]",
        "[      ==]",
        "[       =]",
        "[        ]",
        "[        ]"
        ]
        i = 0
        for x in range(50):
            print(animation[i % len(animation)], end='\r')
            time.sleep(.1)
            i += 1

    def addFunds(self , amount):
        self.balance += amount
        user1.loading()
        print(f'\n{amount} added\nNew Balance is: {self.balance}')

    def withdrawFunds(self , amount):
        if self.balance >= amount:
            self.balance -= amount
            user1.loading()
            print(f'\n{amount} withdrawn\nNew Balance is: {self.balance}')
        else:
            print("\nYou do not have the Funds :(")
    
    def checkFunds(self):
        user1.loading()
        print(f'\nYour Balance is: {self.balance}')



user1 = Bank('Person' , 22 , 'Gender' , 50000)


while 1:
    atm = input("\nWhat would you like to do?\n(bal/deposit/withdraw): ")
    if atm.lower() == 'bal':
        user1.checkFunds()
    elif atm.lower() == 'deposit':
        amount = float(input('\nHow much do you want to Deposit?: '))
        user1.addFunds(amount)
    elif atm.lower() == 'withdraw':
        amount = float(input('\nHow much do you want to Withdraw?: '))
        user1.withdrawFunds(amount)
    elif atm.lower() == 'exit':
        print('Thanks!')
        exit()
    else:
        print("Not an Option")