while True:
    salary = int(input("Enter Salary: "))
    if salary <= 30000:
        tax = salary * .20
        takeHome = salary - tax
    elif salary <= 60000:
        tax = salary * .40
        takeHome = salary - tax
    print(f"Your Salary is {salary} , your Tax is {tax} and your net wage is {takeHome}")


 ########################################################################################


while 1: 
    string = input("Enter String: ")
    if string.lower() == 'exit':
        quit()
    elif string[0].isupper():
        print(f"{string[0]} is Uppercase")
    else:
        print(f"{string[0]} is Lowercase")


########################################################################################


vowels = 'aeiou'
while True:
    vowelAmount = 0
    string = input("Enter String: ")
    for x in string:
        if x.lower() in vowels:
            vowelAmount += 1
    print(f"Therer are {vowelAmount} vowels in {string}")


########################################################################################


canDrive = bool(input("Enter True or False: "))
hasLicence = bool(input("Enter True or False: "))

if canDrive and hasLicence:
    print("You can Drive")
elif canDrive and hasLicence == False:
    print("You can't drive :(")


if canDrive == 'Yes' or canDrive == 'Yeah':
    print("You can Drive")
elif canDrive == 'No' or canDrive == 'Nope':
    print('You cant drive')

weekdays = ['Monday' , 'Tuesday' , 'Wednesday' , 'Thursday' , 'Friday']
weekend = ['Saturday' , "Sunday"]

day = input("Enter a Day: ")
if day not in weekdays:
    print("Its the Weekend")
elif day not in weekend:
    print("Its a Week Day")


########################################################################################


fromDoor = input("Left or Right?: ")

if fromDoor == 'Left':
    print("You are in Kitchen!")
    fromKitchen = input("Left or Right?: ")
    if fromKitchen == "Left":
        print("You are in LivingRoom!")
    elif fromKitchen == "Right":
        print("You are in Bathroom")
    else:
        print("Your Standing Still? :/")
elif fromDoor == "Right":
    print("You are Upstairs!")
    fromUpstairs = input("Left or Right?: ")
    if fromUpstairs == "Left":
        print("You are in Bathroom")
    elif fromUpstairs == "Right":
        print("You are in Hall")
    else:
        print("Your Standing Still? :/")
else:
    print("Your Standing Still? :/")


"""
                LivingRoom
        Kitchen
FrontDoor       Bathroom
        Upstairs
                Hall
"""                 


    



########################################################################################


johnsCart = []
joesCart = []

shopItems = ['Milk' , 'Bread' , 'Butter' , 'Beans' , 'Eggs' , 'Water']

def addItem(item , cart):
    print('Cart Items:' , cart)
    cart.append(item)
    print('Cart Items:' , cart)

addItem(shopItems[3] , johnsCart)

###########################################################


def tradeResult(option , ticker , pip):

    if option.lower() == 'sell':
        print(f'You have Sold {ticker}. Pips: {pip}')
    elif option.lower() == 'buy':
        print(f'You have Bought {ticker}. Pips: {pip}')
    else:
        print('Incorrect Submission')

def makeTrade():
    op = input('Enter Buy or Sell: ')
    if op == 'exit':
      exit()
    tikr =  input('Enter Ticker: ')
    if tikr == 'exit':
      exit()
    pp = input('Enter Pips: ')
    if pp == 'exit':
      exit()
    return tradeResult(op , tikr , pp)
while 1:
    makeTrade()


###########################################################

symbol = '%'

cost = int(input('Enter Item Cost: '))
sale = int(input('Enter Discount: '))
def discount(price , percent):
    sale = percent / 100
    dis = price * sale
    newPrice = price - dis 
    print(f'Your price was {price} , with a discount of {percent}{symbol} your new price is {newPrice}')

discount(cost , sale)


########################################################################################


import random
while True:    
    name = input("Enter Full Name: ")
    if name == '':
        print("Not a Name!")
        continue
    def generator(name):
        half = int(len(name) / 2)
        fir = name[:half:-1]
        sec = name[half::-1]
        num = random.randint(0 , 9999)
        username = str(sec) + str(fir) + str(num)
        print(username.replace(' ' , ''))
    generator(name)


########################################################################################


import random
colors = ["red", "blue", "green", "purple", "pink", "yellow", "orange", "black", "white"]

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("Guess the color im thinking of: ")

    while True:
        if color == guess.lower():
            break
        else:
            guess = input("Nope, Try again: ")

    print(f"You guessed it, I was thinking about {color} Well done!")

    play_again = input("That was fun, prees 'Enter' to play again or type 'quit' to end: ")

    if play_again.lower() == "quit":
        break


########################################################################################

 
namesList = []
names = 0
while names < 5:
    name = input("Enter Your Name: ")
    namesList.append(name)
    names += 1 


firstname = namesList[0]
for n in namesList:
    if n.upper() < firstname.upper():
        firstname = n
print(f'{firstname} Is First Alphabetically')


while 1:
    print(namesList)
    choose = int(input('Choose A Name You Would Like To Replace, 1 2 3 4 5: '))
    if not choose > 0 and choose < 6:
        continue
    break
newName = input('Enter A Replacement Name: ')
namesList[choose - 1] = newName
print(namesList)

people = []


def addPerson(name , age , height):
    name = str(name)
    age = int(age)
    height = float(height)
    people.append([name , age , height])

def returnPerson(name):
    for row in people:
        for item in row:
            if name in row:
                return row

def averageAge(listt):
    age = 0
    for row in listt:
        age += row[1]
    return age / len(listt)

def tallest(listt):
    height = listt[0][2]
    for row in listt:
        if row[2] > height:
            height = row[2]
            return height

def shortest(listt):
    height = listt[0][2]
    for row in listt:
        if row[2] < height:
            height = row[2]
            return height


addPerson('Pat' , 22 , 160.0)
addPerson('Jim' , 32 , 50.0)
addPerson('Tom' , 100 , 1000.0)
print(people)

pat = returnPerson('Pat')
print(f'Showing content for {pat}')

average = averageAge(people)
print(f'The average age is {average}')

tall = tallest(people)
small = shortest(people)
diff = tall - small
print(f'The Difference between tallest and smallest is {diff}')

########################################################################################

cars = {
    'Audi' : 'A4' , 
    'BMW' : '7 Series' ,
    'Toyota' : 'Civic'
}

for make , model in cars.items():
    print(f'My {make} is a {model}')
