#password3.py
#version 3: GUI based password manager
#this program is a password manager to store the user's passwords and account safely using a graphical user interface
#r.tanner 27/03/2023

from tkinter import* #importing tkinter to create the GUI
from tkinter.ttk import Combobox #importing the combobox, a specific widget used in this program

root = Tk()
root.geometry("500x500") 
root.title("Password manager")

pwm_account = {"rosetta": "tanner"} #creating a dictionary to store the user's password manager accounts and passwords
accounts_dict = {"r":"t"} #a dictionary for user's to store their personal accounts and passwords 

#creating the main frame, allowing user's to access the password manager
def frame0():
    global frame0 #making it global so I can access the function in other functions
    frame0 = Frame(root)
    frame0.grid() #using the grid method to layout my widgets
    
    title = Label(frame0, text = "Welcome to the password manager!", font = ("Arial Bold", 10))
    title.grid(row = 0, column = 0, padx = 10, pady = 10)

    option_message = Label(frame0, text = "Please choose an option: ", font = ("Arial Bold", 10))
    option_message.grid(row = 1, column = 0, padx = 10, pady = 10)

    #creating a combobox so user's can use the drop down to select their chosen option
    global combo_options
    combo_options = Combobox(frame0)
    combo_options["values"] = ("1. Log in", "2. Create new account", "3. Exit")
    combo_options.grid(row = 2, column = 0)

    #creating a submit button so user's can submit their chosen option
    submit_option_btn = Button(frame0, text = "Submit", command = options)
    submit_option_btn.grid(row = 2, column = 1, pady = 10, padx = 10)

#an option function to run the choice the user has selected
def options():
    check_option = combo_options.get() #retrieving the user's choice input
    if check_option == "1. Log in":
        frame1() #run frame1
    
    elif check_option == "2. Create new account":
        frame2() #run frame2
    
    elif check_option == "3. Exit":
        root.destroy() #destroy the entire window in order to exit the program

#creating frame 2, where user's can log in to the password manager
def frame1():
    global frame1 #making it global so I can access it from other functions
    frame0.grid_remove()
    frame1 = Frame(root)
    frame1.grid()

    username_title = Label(frame1, text = "Enter your username: ", font = ("Arial Bold", 10))
    username_title.grid(row = 1, column = 0, pady = 10)

    global username
    username = Entry(frame1)
    username.grid(row = 1, column = 1, pady = 10)

    password_title = Label(frame1, text = "Enter your password: ", font = ("Arial Bold", 10))
    password_title.grid(row = 2, column = 0, pady = 10)

    global password
    password = Entry(frame1, show = "*") #using this show feature so user's can not see the password they enter in order to make it more secure
    password.grid(row = 2, column = 1, pady = 10)

    submit_user_btn = Button(frame1, text = "Submit", command = check_pwm_account)
    submit_user_btn.grid(row = 3, column = 2, pady = 10, padx = 10)

#function to check the details the user has entered
def check_pwm_account():
    get_username = username.get() #retrieving the user's username input
    if get_username in pwm_account: #if the username the user entered is in the dictionary...
        index = list(pwm_account).index(get_username) #find the index of the user's inputted username 
        value1 = list(pwm_account.values())[index] #find the value of that index^

        get_password = password.get() #retrieving the password the user has entered
        if value1 == get_password: 
            frame1_menu()
    else:
        #if the user entered incorrect details
        error_message = Text(frame1, height = 5, width = 25)
        error_message.grid(row = 4, column = 1)
        error_message.insert(END, f"Incorrect details, please try again")


def frame1_menu():
    frame1.grid_remove() #remove frame 1
    menu_options() #go to the menu function

#creating frame 2, to allow user's to create a new account
def frame2():
    global frame2
    frame0.grid_remove() #this will hide frame 1
    frame2 = Frame(root)
    frame2.grid()
    
    lblAccount = Label(frame2, text = "Enter your new username: ", font = ("Arial Bold", 10))
    lblAccount.grid(row = 0, column = 0, pady = 10)

    entryAccount = Entry(frame2)
    entryAccount.grid(row = 0, column = 1, pady = 10)

    lblPass = Label(frame2, text = "Enter your new password: ", font = ("Arial Bold", 10))
    lblPass.grid(row = 1, column = 0, pady = 10)

    entryPass = Entry(frame2)
    entryPass.grid(row = 1, column = 1, pady = 10)

    #creating a button to submit the user's input
    btnEnter = Button(frame2, text = "submit", command = frame2_menu)
    btnEnter.grid(row = 2, column = 2, pady = 10, padx = 10)

def frame2_menu():
    frame2.grid_remove() #remove frame 2
    menu_options() #go to the menu function

#creating a menu function to ask user's what they would like to do in the password manager
def menu_options():   
    global frame4
    frame4 = Frame(root)
    frame4.grid()
    
    option_message1 = Label(frame4, text = "Please choose an option: ", font = ("Arial Bold", 10))
    option_message1.grid(row = 1, column = 0, padx = 10, pady = 10)

    #creating a combobox so user's can select their option from the drop down
    global pw_combo
    pw_combo = Combobox(frame4)
    pw_combo["values"] = ("1. Add password", "2. Get password", "3. Exit")
    pw_combo.grid(row = 2, column = 0)

    #submitting the option the user has selected
    submit_option_btn = Button(frame4, text = "Submit", command = password_options)
    submit_option_btn.grid(row = 2, column = 1, pady = 10, padx = 10)

#running the password options
def password_options():
    check_option = pw_combo.get() #retrieving the value the user entered in the combobox
    if check_option == "1. Add password":
        add_account() #run add account function
    
    elif check_option == "2. Get password":
        get_password_option() #run get password function
    
    elif check_option == "3. Exit":
        root.destroy() #destroy the root and exit the program

#creating an add account function to add a user's personal account to the password manager
def add_account():
    frame4.grid_remove() #remove frame 4
    global frame5
    frame5 = Frame(root)
    frame5.grid()
    account_title = Label(frame5, text = "Enter account name: ", font = ("Arial Bold", 10))
    account_title.grid(row = 1, column = 0, pady = 10)

    user_account = Entry(frame5)
    user_account.grid(row = 1, column = 1, pady = 10)

    pass_title = Label(frame5, text = "Enter password: ", font = ("Arial Bold", 10))
    pass_title.grid(row = 2, column = 0, pady = 10)

    user_pass = Entry(frame5)
    user_pass.grid(row = 2, column = 1, pady = 10)

    btnEnter = Button(frame5, text = "submit", command = lambda:accounts(user_account.get(),user_pass.get())) #adding the user's account to the dictionary using lamda
    btnEnter.grid(row = 2, column = 2, pady = 10, padx = 10)

#adding the user's account to the dictionary
def accounts(user_account, user_pass):
    accounts_dict[user_account] = user_pass

    #creating a textbox
    textbox1 = Text(frame5, height = 5, width = 25)
    textbox1.grid(row = 3, column = 1)
    
    #telling the user that their account has been made
    textbox1.insert(END, "Success! \nnew account added!")

    next_button1 = Button(frame5, text = "next", command = frame5_menu)
    next_button1.grid(row = 4, column = 1, pady = 10, padx = 10)

def frame5_menu():
    frame5.grid_remove() #removing frame 5
    menu_options() #going back to the menu function

def frame6_menu():
    frame6.grid_remove() #removing frame 6
    menu_options() #going back to the menu function

#creating a get password function to retrieve the user's password
def get_password_option():
    frame4.grid_remove() #removing frame 4
    global frame6
    frame6 = Frame(root)
    frame6.grid()

    account_title1 = Label(frame6, text = "Enter account name: ", font = ("Arial Bold", 10))
    account_title1.grid(row = 1, column = 0, pady = 10)
    
    global user_account1
    user_account1 = Entry(frame6)
    user_account1.grid(row = 1, column = 1, pady = 10)

    submit_button = Button(frame6, text = "Submit", command = retrieve_password)
    submit_button.grid(row = 2, column = 1, pady = 10, padx = 10)

#retrieving the user's password
def retrieve_password():
    #creating a textbox
    textbox = Text(frame6, height = 5, width = 25)
    textbox.grid(row = 3, column = 1)

    #retrieving the account the user entere
    get_user_acc = user_account1.get()
    
    #checking if that account is in the accounts dictionary
    if get_user_acc in accounts_dict:
        index = list(accounts_dict).index(get_user_acc) #getting the index of the user's inputted account
        value = list(accounts_dict.values())[index] #finding the value (password) of the user's inputted account

        #printing the password in the textbox
        textbox.insert(END, f"Password for {get_user_acc}:\n {value}")
    
    #if the user's account is not in the dictionary, then print that there is no password found
    else:
        textbox.insert(END, f"No password found \nfor {get_user_acc}")
    
    #a next button to go back to the options menu
    next_button2 = Button(frame6, text = "next", command = frame6_menu)
    next_button2.grid(row = 4, column = 1, pady = 10, padx = 10)

#main routine - running frame 0
frame0()

#closing the main loop 
root.mainloop()
