import re

# 1
while 1:
    number = input("Enter Landline Number: ")
    isValid = re.match(r'^[0]{1}\d{8}$' , number)
    if isValid:
        print('Valid Number :)')
    else:
        print('Not a Valid Number :(')

# 2
numbers = []
while 1:
    number = input('Enter Mobile Number: ')
    isValid = re.match(r'^08[35679]\d{7}$' , number)
    if isValid:
        numbers.append(number)
        print('Number Added :)')
    else:
        print('Not a Valid Number :(')
        continue
    print('Would You Like To Search for Number or Continue Adding Numbers?')
    q = input('Type Add to Continue Adding or Type Search to Search Numbers: ')
    if q.lower() == 'add':
        continue
    elif q.lower() == 'search':
        search = ''
        while search.lower() != 'add':
            search = input('Enter First 3 Digits to Search for Number or Add to Add more Numbers: ')
            for n in numbers:
                if n.startswith(search):
                    print(n)


# 3
while 1:
    region = input("Are You In ROI or NI?: ")
    pCode = input('Prove it, Enter your Postcode: ')
    isValid = re.match(r'(?:^[AC-FHKNPRTV-Y][0-9]{2}|D6W)[ -]?[0-9AC-FHKNPRTV-Y]{4}$' , pCode)
    isOtherValid = re.match(r'^[A-Z]{1,2}\d[A-Z\d]? ?\d[A-Z]{2}$' , pCode)
    if isValid and region.upper() == 'ROI':
        print('Ok I Believe You')
    elif isOtherValid and region.upper() == 'NI':
        print('Ok I Believe You')
    else:
        print('I Do Not Believe You')


# 4
emails = []
while 1:
    email = input("\nEnter Email: ")
    isValid = re.match(r'^[a-z]+[.]{1}[a-z]+@generation.org{1}$' , email)
    isOtherValid = re.match(r'^[a-z]+@generation.org{1}$' , email)
    if isValid or isOtherValid:
        print("Valid :)")
        emails.append(email)
    else:
        print("Not Valid :(")
        print('\nValad Emails: ')
        print(emails)
        continue
    print('\nValid Emails:')
    print(emails)


# 5
while 1:
    dob = input("Enter Date Of Birth: ")
    isValid = re.match(r'^[012]{1}[0-9]{1}/[01]{1}[0-9]{1}/[1]{1}[9]{1}[0-9]{1}[0-9]{1}$' , dob)
    isOtherValid = re.match(r'^[012]{1}[0-9]{1}/[01]{1}[0-9]{1}/[0-9]{1}[0-9]{1}$' , dob)
    if isValid or isOtherValid:
        print("Valid" , dob)
    else:
        print("Not Valid" , dob)


while 1:
    userID = input("Enter UserName: ")
    isValid = re.match(r'^[a-zA-Z]+[0-9]{3}$' , userID)
    if isValid:
        print('Valid Username')
    else:
        print('Invalid Username')