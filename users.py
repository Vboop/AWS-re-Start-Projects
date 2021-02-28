#Imports 
import pprint
import random
# Empty Dictionary
people = dict()
def addUser():
    # Loop while theres less than 4 Dictionary Entries
    while len(people) < 4:
        # Loop to restart naming process if name is in dictionary already 
        while 1:
            name = str(input('Enter Name: '))
            if name in people.keys():
                print('Name Already In Use, Please Try Again!')
                continue
            break
        age = None
        # Loop to restart age input if it is not an int
        while type(age) != int:
            try:
                age = int(input('Enter Age: '))
            except:
                print('Error')
                continue
        hTown = str(input('Enter Home Town: '))
        # Using Empty Dictionary from the beginning to store name as key and list of dictionaries as values , sub Dictionaries hold age and hometown
        people[name] = [{'Age' : age} , {'HomeTown' : hTown}]
        # Prints vertically 
        pprint.pprint(people)
        # Appending Data to File
        with open('file.txt' , 'a') as f:
            f.write(name + " : " + str(people[name])+'\n')
    # Reading Data from File
    with open('file.txt' , 'r') as f:
        print('\n'+f.read())