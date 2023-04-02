#password1.py
#version 1: basic password manager
#this program is a password manager to store the user's passwords and account safely
#r.tanner 22/03/2023

#creating an empty dictionary to store account name and password 
passwords = {}

#using 3 functions like adding passwords to account and asking to get password from dictionary
def add_password(account, password):
    passwords[account] = password

#this is the get password function, to get the corresponding password of the account the user has entered
def get_password(account):
    return passwords.get(account, None)

#main function
def main():
    while True:
        #the user has 3 options of what they can do
        print("1. Add password")
        print("2. Get password")
        print("3. Exit")

        choice = input("Enter your choice : ") #asking the user their choice

        if choice == "1":
            account = input("Enter account name: ")
            password = input("Enter password : ")
            add_password(account, password) #using the add password function to add the user's account and password to the dictionary

        elif choice == "2":
            account = input("Enter account name: ")
            password = get_password(account) #returning the user's password

            if password: #if password is found
                print(f"Password for {account}: {password}")
            
            else: #if no password is found
                print(f"No password found for {account}")
        
        elif choice == "3":
            break #ending the program
        
        else: #if the user does not enter 1, 2, or 3
            print("Invalid choice.")

if __name__ == "__main__": #if no imported components are used then this is applicable
    main()  
