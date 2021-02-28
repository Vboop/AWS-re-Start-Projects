import time

class User():
    def __init__(self , name):
        self.name = name
        self.score = 0
        self.level = 1
        self.fails = 0

    def levelUp(self):
        loading()
        self.level += 1
        print(f"\nYou Just Leveled Up!")
        print(f"Level {self.level}\n")
        return


    def addScore(self):
        self.score += 10
        print(f"\nYou Scored {self.score} Points!\n")
        if self.score == 20 or self.score == 40:
            self.levelUp()
        return

    def addFail(self):
        self.fails += 1
        return

    def failScreen(self):
        print(f"You have failed with a score of {self.score} and {self.fails} fails :(")
    
    def winScreen(self):
        print(f"You have won with a score of {self.score} and you made it to level {self.level}")


def loading():
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

quiz = ''
user = User('Person')
while 1:
    while 1:
        try:
            quiz = input("Do you like Beans?\n(yes/no): ")
        except:
            print("Something Went Wrong")
        if quiz.lower() == 'yes':
            user.addScore()
            break
        elif quiz.lower() == 'no':
            user.addFail()
            break
            if user.fails == 3:
                break
        else:
            print("Not an Option!")
            continue

    if user.fails == 3:
        break

    while 1:
        try:
            quiz = input("Do you like Greens?\n(yes/no): ")
        except:
            print("Something Went Wrong")
            continue
        if quiz.lower() == 'no':
            user.addScore()
            break
        elif quiz.lower() == 'yes':
            user.addFail()
            break
            if user.fails == 3:
                break
        else:
            print("Not an Option!")
            continue
    
    if user.fails == 3:
        break

    while 1:
        try:
            quiz = input("Do you like Potatoes?\n(yes/no): ")
        except:
            print("Something Went Wrong")
            continue
        if quiz.lower() == 'yes':
            user.addScore()
            break
        elif quiz.lower() == 'no':
            user.addFail()
            break
            if user.fails == 3:
                break
        else:
            print("Not an Option!")
            continue
    
    if user.fails == 3:
        break

    while 1:
        try:
            quiz = input("Do you like Tomatoes?\n(yes/no): ")
        except:
            print("Something Went Wrong")
            continue
        if quiz.lower() == 'yes':
            user.addScore()
            break
        elif quiz.lower() == 'no':
            user.addFail()
            break
            if user.fails == 3:
                break
        else:
            print("Not an Option!")
            continue
        break

    if user.fails == 3:
        break

    while 1:
        try:
            quiz = input("Do you like Beetroot?\n(yes/no): ")
        except:
            print("Something Went Wrong")
            continue
        if quiz.lower() == 'no':
            user.addScore()
            break
        elif quiz.lower() == 'yes':
            user.addFail()
            break
        else:
            print("Not an Option!")
            continue
        break
    break

if user.fails == 3:
    user.failScreen()
else:
    user.winScreen()