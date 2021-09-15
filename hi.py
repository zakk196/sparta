#import sys
#import math
import re
#from string import printable
password = (input(" Enter your password: "))

length = str(len(password))
password_length_good = False
#working
if len (password) < 8:
    print("[!] Password should be atleast 8 characters long")
    print("[!] Password is only", length, "characters long" )
    password_length_good = False;

else:
    print("(*) Your password is", length, "characters :)  ")
    password_length_good = True;
#

# working
UpperLength = len(re.findall(r'[A-Z]', password))
print("(*) Your password contains", UpperLength, "uppercase characters")

if UpperLength == 0:
    print("[!] Your password should have atleast 1 uppercase character!")
#

#working
digits = len(re.findall(r'[0-9]', password))
print("(*) Your password contains", digits, "numeric digits")

if digits == 0:
    print("[!] Your password should have atleast 1 Number!")
#
#working
def count_special_character(password):

    special_char= 0
    for i in range(0, len(password)):
        if (password[i].isalpha()):
            continue
        elif (password[i].isdigit()):
            continue
        else:
            special_char += 1
    if special_char >= 1:
        print("(*) You have {} Special Character/s in your password ".format(special_char))
    else:
        print("[!] Your password should have atleast 1 special character!")

if __name__ == '__main__' :
    string = password
    count_special_character(string)





















#add common password code under here

#matchedPass = False
#commonPasswords = ['password','letmein','lemon']

#for commonPass in commonPasswords:
#    if commonPass == password:
#        matchedPass == True
#        print(matchedPass)
#
#    if matchedPass == True:
#        print("Your password is common !")
#    else:
#        print("your password is not common")
