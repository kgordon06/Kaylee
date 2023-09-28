from getpass import getpass # allows the user to input password without it being visible

player1=0
player2=0 # initializes the player input for the ui
player3=0 # initializes the player input for the ui

users = ['brandon', 'jones'] # all users
admin = ['jones'] # just admins
passwords = ['password1', 'password2'] # passwords of corresponding user

def chkuser():
    for x in users: # prints every user in user list
        print()
        print(x) # returns string

def chkadmin(): # prints every admin in admin list
    for x in admin:
        print()
        print(x) # returns string

def chkpwd():
    for x in passwords: # prints all passwords of admin and user
        print()
        print(x) # returns string
 
def changeadmin(): # changes the status of an admin from 1 or 0

    while True: # runs a loop for efficiency

        chkuser() # presents all users to pick from

        print()
        user = input('Enter the username to see status of user: ').lower() # grabs input from the user to select the user for change
        print()

        if user in users: # verifies if the selected user is real

            if user in admin: # checks to see if it is already an admin

                print('This user is an administrator') # declares to user that this user is an admin 
                change = input('Do you wish to change this (Y/N)').lower() # asks if they want to change this admin account to a regular account
                if change == "y": # if selected yes then the admin will be removed from his role
                    
                    if len(admin) == 1: # prevents the user from locking themself out of the admin menu

                        print()
                        print('Cannot change this admin, only admin on record') # replies back with a error
                    
                    else:
                        admin.remove(user) # removes the user from the group if there is more than one admin
                        print()
                        print('User removed from admin list') # responds

                else:
                    break # if the user doesn't type the options or says no
        
            else:

                print('This user is a normal user') # replies back if the user is not an admin saying its a normal user
                change = input('Do you wish to change this (Y/N)').lower() # asks if you wish to change this user to an admin

                if change == "y": # if yesthen it will go with the process
                    
                    admin.append(user) # added user to admin list
                    print()
                    print('User added to admin list') # respons
                
                else: # if the user doesn't type the options or says no
                    break # breaks out of loop

        else:  # respons with this is the user is not in the user list
            print('invalid user') # responds
            break # breaks out of the program

def adduser(): # adds users to the user lists, followed with a password for the account
            
    print()
            
    newuser = input('Please enter the new username: ').lower() # asks the user for the users new name
            
    while True: # runs a loop for efficiency

        print()
                
        password1 = getpass('Enter the new password: ').lower() # asks for a password for the new user
        password2 = getpass('Confirm new password: ').lower() # confirms the 2 passwords match
                
        print()
                
        if password1 == password2: # verifies that the passwords match
                    
            newadmin = input('Is this user an admin (Y/N): ').lower() # asks if you want to make this user an admin
            print()

            if newadmin == 'y': # if the user says this is an admin, it will add it to users and admin lists

                print('Admin Created') # respons
                users.append(newuser) # adds user to users list
                admin.append(newuser) # adds user to admin list
                passwords.append(password1) # adds password to password list with the corresponding index
                break # breaks out of the loop
                
            else: # if the user doesn't respond with the correct options or says no
 
                print('User Created') # responds
                users.append(newuser) # adds user to user list
                passwords.append(password1) # adds password to password list with the corresponding index
                break  # breaks out of the loop

        else: # if the passwords do not match it will respond with an error
            print('Passwords are not the same') # responds

def userchange(): # changes the username of the user
    
    print()
    
    user = input('Enter the user for change: ').lower() # asks for the username of the user
    password = getpass('Enter password: ').lower() # asks the passwords of said user
    userindex = users.index(user) # checks the index of the user to verify for password later
    
    if user in users: # sees if this user exists
        
        if password == passwords[userindex]: # checks to see if the password matches the users index
            
            print()
            
            newuser = input('Please enter new username: ').lower() # asks for the new username
            users.remove(user) # removes the user's old name
            users.insert(userindex, newuser) # replaces the users name in the index it was originally in to match the password index
            print()
                
        else: # if the passwords do not match 
            print()
            print('incorrect password') # responds
    else: # if the username doesn't match
        print()
        print('incorrect username') # responds

def passwordreset(): # resets the password of said user
    
    print()
    
    user = input('Enter the user for password change: ').lower() # asks for the username for change 
    password = getpass('Enter old password: ').lower() # asks for the old password before change
    userindex = users.index(user) # grabs the index of the user to verify for password later
    
    if user in users: # checks to see if user is in user list
        
        if password == passwords[userindex]: # checks to see if password matches the user passwords index
            
            while True: # runs a loop for efficiency

                print()
                
                password1 = getpass('Enter the new password: ').lower() # asks for the new password
                password2 = getpass('Confirm new password: ').lower() # confirms new password
                
                print()
                
                if password1 == password2: # verifies the passwords
                    print('Password Reset') # responds
                    passwords.remove(password) # removes the old password
                    passwords.insert(userindex, password1) # adds the new password in the corresponding index
                    break # breaks out of loop
                
                else: # passwords don't match
                    print('Passwords are not the same') # responds
        else: # user inputted wrong password
            print()
            print('incorrect password') # responds
    else: # user inputted wrong username
        print()
        print('incorrect username') # responds


while True: # loops the ui for efficiency
        
    try: # tries the code
        
        breakout = True # used for signing out

        print()
        
        print('Welcome to Brandon Incorporated') # welcomes user
        print('1. Login') # prompts user with options
        print('2. Exit')
        
        player1 = int(input('Please enter the corresponding integer: ')) # asks the user to input a number displayed by the ui
        if player1 == 1: # checks to see if input is 1
            
            print()
            
            user = input('Please enter your username: ').lower() # asks for the username
            password = getpass('Please enter your password: ').lower() # asks for the password
 
            if user in users: # verifies this user is real
                userindex = users.index(user) # grabs the index of the user to verify password
                
                if password == passwords[userindex]: # verifies password user typed with the corresponding password in the index
                        
                    if user in admin: # if the user is an admin it will display the admin UI

                        print()
                        print('Welcome Administrator', user) # welcomes said user

                        while breakout: # same as the while True loop just used with a variable to allow signing out, Used for the change admins prompt
                            
                            try: # tries the code

                                print()
                                print('ADMINISTRATOR ACCOUNT') # notifies user they are using an admin account
                                print()
                                print('1. Add User') # prompts user with options
                                print('2. Username Change')
                                print('3. Password change')
                                print('4. Check Users')
                                print('5. Check Admins')
                                print('6. Check Passwords')
                                print('7. Change Admins')
                                print('8. Sign out')
                                
                                player2 = int(input('Please enter the corresponding integer: ')) # asks the user to input a number displayed by the ui

                                if player2 == 1: # adds a user
                                    adduser()

                                if player2 == 2: # changes the username of user
                                    userchange()

                                if player2 == 3: # resets password of user
                                    passwordreset()

                                if player2 == 4: # checks all users on file
                                    chkuser()

                                if player2 == 5: # checks all admins on file
                                    chkadmin()

                                if player2 == 6: # checks all passwords on file, does not show users corresponding (check which order they are written)
                                    chkpwd()

                                if player2 == 7: # changes status of admin or regular account
                                    changeadmin()
                                    breakout = False

                                if player2 == 8: # signs out
                                    breakout = False
                            
                            except ValueError: # skips any errors presented running the code
                                pass
                        
                    else: # if user doesn't fall into admin group

                        print()
                        print('Welcome', user) # welcomes user

                        while breakout: # same as the while True loop just used with a variable to allow signing out, Used for the change admins prompt
                            
                            try: # tries the code
                                
                                print()
                                print('1. Check Users')
                                print('2. Sign out')
                                
                                player3 = int(input('Please enter the corresponding integer: ')) # asks the user to input a number displayed by the ui

                                if player3 == 1: # checks to see users on file
                                    chkuser()

                                if player3 == 2: # signs user out
                                    breakout = False
                            
                            except ValueError: # skips any errors presented running the code
                                pass

                else: # incorrect password
                    print()
                    print('Incorrect Password') # responds
            else: # incorrect username
                print()
                print('Incorrect Username') # responds
        
        if player1 == 2: # checks to see if user enters 2
            break # breaks out of loop ending the session

    except ValueError: # skips any errors presented running the code
        pass 