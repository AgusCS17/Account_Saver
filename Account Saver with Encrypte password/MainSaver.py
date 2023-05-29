import time
import random
from cryptography.fernet import Fernet

menu_option = ("1","2","3")




print()
print("Hai, Welcome to Account Saver")
time.sleep(2)

'''
*Use this code once only for creating the key after that comment it
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key =load_key()
fer = Fernet(key)

def add():
    email = str(input("Email : "))
    password = input("Password : ")
    game = input("Input Game Name : ")

    with open("Account.txt", 'a') as f:
        f.write(email + "|" + fer.encrypt(password.encode()).decode()+ "|" + game + "\n")
    
def view():
    with open("Account.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            Email, passw , game = data.rsplit("|")
            print("Email: " + Email + " Password: " + fer.decrypt(passw.encode()).decode() + " Game: " + game)




while(True):
    print()
    print("XXXX Menu XXX")
    time.sleep(1)
    print()
    print("1. Add Account")
    print("2. view Account")
    print("3. Exit")
    time.sleep(1)
    option = str(input("Please input your Choice : "))
    
    if option in menu_option:

        if option == "1":
            add()

        if option == "2":
            view()

        if option == "3":
            break
        
    else:

        print()
        print("there was no option")
        

