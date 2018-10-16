# *********************************************************************
# Code by Akeel Ur Rehman                                            **
# First Function is to format phone number,                          **
# You can check by entering phone number like :+46-73-212345         **
# *********************************************************************
import re
def format_phone(num):
    REGEX = '^\d'
    s = re.sub(r'[^\w\s]', '', num)  # Remove all - from a phone number entered
    print("Phone format",
    re.sub(r'(\d{3})(\d{2})(\d{5})', r'(\1) \2-\3', s))  # Proper format of a phone number like (467)32-12345
    area_code = (re.sub(r'(\d{5})(\d{0})(\d{0})', r'\1 \0 \0', s))

    # print(type(area_code))
    # Only extracting the area code which is first 5 digits: +46-73-212345  aread code will be 46732
    # Here code will split Phone Num into its code and number
    ac, phonenum = area_code.split(' ', 1)
    print("Area Code=  ", ac)
    print("Phone Number=  ", phonenum)
    #  print(type(s))
    # Call the function and pass area code:
    # Function call to find the area code from the list given in file Ratelist
    Match_Number(ac)

def Match_Number(num):
    # List to store all possible matches

    mymatch = []
    bestrate = 1000
    code = 'Free Call'

    # Open rate list in read mode as f
    with open('Callrates.txt', 'r') as f:
        # Checking line by line
        for line in f:
            # Compare any match  ?
            if re.match(num,line):
                #print(re.match(num ,line))
                #print(line)
                words = line.split()
                temp = float(words[1])
                #print(temp)
                for w in words:
                    #print(w)
                    mymatch.append(w)
                if temp < bestrate:
                    bestrate=float(temp)
                    code = words[2]
                    #print(words[0])
    if bestrate == 1000:
        print("Sorry no Caller available for this Area code try again.")
    else:
        print("I found only these matches :",mymatch)
        print("Its better to call with Company: " ,code,"  as low as @",bestrate,"$")
# End of the functions

#################################################################################################
# Code to Print Menu for user:
print("\nIf you enter a phone number like this +46-73-212345 it will convert to:Phone format (467) 32-12345 "
      "\nIts assumed that code can be maximum 5 digit")
num = input("Enter any phone number \n")
num2=len(num)
print(num2)
if num2<5 :
    print("Your phone number is not upto required length.\n Still you can search with this Proceed Y/N")
    op=input()
    if op=='y' or op== 'Y':
        Match_Number(num)

else:
    format_phone(num)