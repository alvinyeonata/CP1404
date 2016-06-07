import string, random

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SPECIAL = string.punctuation
"""
new_password = ""

for i in range(random.randint(5, 15)):
    rand_choice = random.randint(1, 4)
    if rand_choice == 1:
        new_password += random.choice(LOWER)
    elif rand_choice == 2:
        new_password += random.choice(UPPER)
    elif rand_choice ==3:
        new_password += random.choice(DIGITS)
    else:
        new_password += random.choice(SPECIAL)
print(new_password)
print(new_password[0] in LOWER)
"""

Menu = """Please enter a valid password \n Your password must be between 5 and 15 characters, and contain: \n 1 or more uppercase characters \n 1 or more lowercase characters \n 1 or more numbers \n and 1 or more special characters:  !@#$%^&*()_+[]\{}|;':",./<>?`~
 """
def check_password(pw, validator):
    for each in pw:
        if each in validator:
            return True
    else:
        return False
print(Menu)
user_password = input(">")

while True:
    if len(user_password) < 5 or len(user_password) >15:
        print("Invalid Password \n Length issue")
        user_password = input(">")
    elif not check_password(user_password, UPPER):
        print("Invalid Password \n Uppercase issue")
        user_password = input(">")
    elif not check_password(user_password, LOWER):
        print("Invalid Password \n Lowercase issue")
        user_password = input(">")
    elif not check_password(user_password, DIGITS):
        print("Invalid Password \n Digits issue")
        user_password = input(">")
    elif not check_password(user_password, SPECIAL):
        print("Invalid Password \n Special issue")
        user_password = input(">")
    else:
        print("Your", len(user_password) , "character password is valid:",user_password )
        break
