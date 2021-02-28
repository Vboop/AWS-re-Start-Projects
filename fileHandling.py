import re
import os

titles = 'Date              Recieved        Spent       Balance\n'
def checkForFile():
    if not os.path.isfile('$.txt'):
        with open('$.txt' , 'w') as f:
            while 1:
                try:
                    balance = float(input("Enter First Time Current Balance: "))
                except:
                    print('Something went wrong with Balance!')
                    continue
                sure = input(f"Are You Sure This is Correct? {balance}\n(yes/no): ")
                if sure.lower() == 'no':
                    continue
                elif sure.lower() == 'yes':
                    break
                else:
                    print('Not an Option')
            while 1:
                date = input("Enter Date : --/--/---- : ")
                isValid = re.match('^[0123]\d/[01][012]/[2][0][2][1]$' , date)
                if not isValid:
                    continue
                break
            f.write(titles)
            f.write(f'{date}        0               0           {balance}\n')
            f.close()
            while 1:
                log = input("Would you like to log?\n(yes/no): ")
                if log.lower() == 'yes':
                    addLog()
                elif log.lower() == 'no':
                    exit()
                else:
                    print('Not an Option')
                    continue
    addLog()
            
            

def addLog():
    with open('$.txt' , 'r') as f:
        for line in f:
            pass
        try:
            prePrice = float(line[-12:].strip(' '))
            print(f'Previous Balance: {prePrice}')
        except:
            print("Something Wrong with Previous Balance!")
            exit()
            print(f'Previous Price Set To {prePrice}')
        print(prePrice)
        f.close()

    with open('$.txt' , 'a') as f:
        while 1:
            date = input("Enter Date : --/--/---- : ")
            isValid = re.match('^[0123]\d/[01][012]/[2][0][2][1]$' , date)
            if not isValid:
                continue
            break
        prevBal = prePrice
        while 1:
            try:
                balance = float(input("Enter Currant Balance: "))
            except:
                print("Something went wrong with Balance!")
                continue
            sure = input(f"Are You Sure This is Correct? {balance}\n(yes/no): ")
            if sure.lower() == 'no':
                continue
            elif sure.lower() == 'yes':
                break
            else:
                print('Not an Option')
        while 1:
            try:
                recieved = float(input("Enter This Weeks Wage: "))
            except:
                print("Something went wrong with Received!")
                continue
            sure = input(f"Are You Sure This is Correct? {recieved}\n(yes/no): ")
            if sure.lower() == 'no':
                continue
            elif sure.lower() == 'yes':
                break
            else:
                print('Not an Option')
        try:
            spent = round((prevBal + recieved) - balance , 2)
        except:
            print("Something went wrong with Spent!")
            exit()
        f.write(f'{date}        {recieved}           {spent}       {balance}\n')
        f.close()

checkForFile()