#password2.py
#version 2: password manager program
#this program is a password manager to store the user's passwords and account safely
#r.tanner 22/03/2023

#declaring the variables/constants
MIN_AGE = 13 #the minimum age the user can be 
MAX_AGE = 100 #the maximum age the user can be
LOG_IN_ATTEMPTS = 3 #user's have 3 attempts to log in or they will be locked out

accounts_dict = {"r" :"t", "rosetta": "tanner"}
user_accounts_dict = {} #dictionary to add the user's accounts and passwords

#a function to ask the user their name and see if they are old enough to sign up 
def menu():
    name = input("Enter your name: ")
    print(f"Hi {name}, welcome to the password manager.")
    
    while True:
        try:
            age = int(input("Enter your age: "))
            
            if age >= MIN_AGE and age <= MAX_AGE: #if the user enter's an age that is valid. 
                break

            else: #if the user enters an invalid age, they cannot use the program. 
                print("Your are not old enough to be eligible for this program.")
                quit()

        except ValueError: #if the user does not enter a valid integer. 
            print("Please enter a valid integer. ")

#creating a log in function, so user's can log in to make the program extra secure
def log_in():
    LOG_IN_ATTEMPTS = 3 #the user has three attempts to log in with their correct details.
    while LOG_IN_ATTEMPTS >= 1:
        username = input("Enter your username : ")
        if username in accounts_dict:
            check_username = accounts_dict.get(username) #making the user's username equivalent to the correct username in the dictionary. 

        else:
            check_username = None #if the user's username is not found in the dictionary
        password = input("Enter your password: ")

        if check_username == password:
            print("Access Granted.") #if the user enters the correct username and password
            break

        else: #if the user's details are incorrect, they will have one less try.
            LOG_IN_ATTEMPTS -=1
            print("Incorrect details. Please try again.")
            print(f"Attempts remaining: {LOG_IN_ATTEMPTS}")


#allowing the user to create a new account for the password manager
def new_account():
    username = input("Enter your new username : ")
    password = input("Enter your new password : ")
    accounts_dict[username] = password #adding the user's username and password to the accounts dictionary
    print("Success. New account made. ")

#main function
def main():
    while True:
        #printing the options the user can undertake
        print("1. Add password")
        print("2. Get password")
        print("3. Exit")

        #asking the user which option they would like to choose
        choice = input("Enter your choice : ")

        if choice == "1":
            account = input("Enter account name: ")
            password = input("Enter password : ")
            user_accounts_dict[account] = password #adding the user's account and password to the dictionary


        elif choice == "2":
            account = input("Enter account name: ")
            #retrieving the user's password for their corresponding account they entered
            password = user_accounts_dict.get(account)

            if password: #printing the password
                print(f"Password for {account}: {password}")
            
            else: #if no password is found, then print that no password is found
                print(f"No password found for {account}")
        
        elif choice == "3": #if the user chooses to exit the program
            break
        
        else: #if the user does not enter a valid option of 1, 2 or 3
            print("Invalid choice.")

menu()
#asking the user what menu option they would like to do. 


while True:
    try:
        #asking the user which function they would like to run
        print("1. Login \n2. Create new account\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1 or choice == 2 or choice == 3:
            break

        #if the user does not enter a valid menu option.
        else:
            print("Please enter a valid input of 1, 2, or 3. ")
    
    #if the user does not enter an integer. 
    except ValueError:
        print("Please enter a valid integer.")

#if the user chooses the log in function
if choice == 1:
    log_in()
    main()

#if the user chooses to create a new account
if choice == 2:
    new_account()
    main()

#if the user wants to exit the password manager program
if choice == 3:
    print("Thank you for using password manager! Come back soon.")
    exit
