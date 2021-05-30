#!/usr/bin/env python3.8

from credentials import Credentials
from user import User 
from password import *

def create_user(username, password):
    '''
    function used to create a new user
    '''
    new_user =User(username, password)
    return new_user

def save_user(user):
    '''
    function to save users
    '''
    user.save_user()  

def check_existing_user(username, password):
    '''
    function that returns saved users
    '''
    return User.user_exist(username, password) 


def create_credentials(account,username,password):
    '''
    function to create new credentials
    ''' 
    new_credentials= Credentials(account,username,password)
    return new_credentials  

def save_credentials(credentials):
    '''
    functon to save credentials
    '''
    credentials.save_credentials() 

def del_credentials(credentials):
    '''
    function to delete credentials
    '''
    credentials.del_credentials()

def find_credentials(username):
    '''
    function that finds credential by username and returns the credential
    '''
    return Credentials.find_by_username(username)

def display_credentials():
    '''
    function that returns saved credentials
    '''
    return Credentials.display_credentials()  

def check_existing_credentials(username):
    '''
    function that checks if a credential exists with that username
    '''
    return Credentials.credentials_exist(username)    


def main():
    print("Hello, Welcome to FUTURE SAVER!. Create an account to save your passwords.")
    while True:
        print('\n')
        print('**********')
        print('Use these short codes to navigate : cu - create a new user, lg - login to your account, ex -exit the future saver')
        print('**********')

        shortCode = input().lower()

        if shortCode == 'cu':
            print('Enter Your Username')
            username = input()

            passResponse = input(
            'Do you want a generated password? \n  Respond with \'y\' for YES or \'n\' for NO: ').lower()

            if passResponse == 'y':
                createdPass = passwordGenerator(getPassLength())
                password= createdPass

                print(f'New password ({str(len(createdPass))}):------>{createdPass}')
            else:

                print("What's your password")
                password = input()
                print("Confirm password ....")
                confirm_password = input()
    
            while confirm_password != password:
                    print("Password did not match")
                    print("password ....")
                    password = input()
                    print("Confirm password ....")
                    confirm_password = input()
            
            else:
                    save_user(create_user(username, password))
                    print(f'CONGRATULATIONS!! 🎉, New Account has been created for: {username} using password: {password}')
                    print("Proceed to login")
                    print("username")
                    entered_username= input()
                    print("your password")
                    entered_password = input()

        elif shortCode == 'lg':

                    print('Enter Your Username: ')
                    defaultUserName = input()

                    print('Enter password: ')
                    defaultPassword = input()
                    print('\n')
                    print('Login success! \n')
                    print('\n')

                    while entered_username != username or entered_password != password:
                            print("Invalid username or password")
                            print('username')
                            entered_username = input()
                            print("Your password")
                            entered_password = input()
                    else:                
                    
                            print(f'WELCOME {entered_username} 😍. Please choose an option to proceed')

                            while True:
                                    print('\n ………')
                                    print(
                                        'Use these short codes to navigate through credentials : ac - add credential, lc - list credentials, dc - delete credential, ex - exit')
                                    print('………')

                                    shortCode = input().lower()
                                    if shortCode == 'ac':
                                        print('----------')
                                        print('Save New Credential...')
                                        print('----------')
                                        print('Enter account to save credentials for: ')
                                        credAccount = input()
                                        print('…')

                                        print('Enter username: ')
                                        credUserName = input()
                                        print('…')

                                        passResponse = input(
                                            'Do you want a generated password? \n  Respond with \'y\' for YES or \'n\' for NO: ').lower()

                                        if passResponse == 'y':
                                            createdPass = passwordGenerator(getPassLength())
                                            confirmedPass = createdPass

                                            save_credentials(create_credentials(
                                                credAccount, credUserName, createdPass))
                                            print(
                                                f'New password ({str(len(createdPass))}): -----> {createdPass}')
                                        else:
                                            print('Enter password: ')
                                            credPass = input()

                                            print('Confirm Password: ')
                                            confirmedPass = input()

                                            print('\n')

                                            if credPass != confirmedPass:
                                                print('Invalid: Passwords did not match!')
                                                print('Enter password: ')
                                                credPass = input()

                                                print('Confirm password: ')
                                                confirmedPass = input()
                                            else:
                                                save_credentials(create_credentials(
                                                    credAccount, credUserName, credPass))
                                                print(
                                                    f'CONGRATULATIONS!! Your credentials for {credAccount} was successfully created!')
                                                print('\n')

                                    # source of error have a look
                                    #
                                    elif shortCode == 'lc':
                                        if display_credentials():
                                            print('HERE IS A LIST OF ALL YOUR ACCOUNTS')
                                            print('\n')
                                            for credential in display_credentials():
                                                print(
                                                    f'{credential.account}: \nuser name: {credential.username}, password: {credential.password}')

                                            print('\n')
                                        else:
                                            print('\n')
                                            print("You dont seem to have any contacts saved yet")
                                            print('\n')
                                    elif shortCode == "dc":
                                        print("Enter User Name For The Account You Would Like To Delete")
                                        username = input()
                                        if  check_existing_credentials(username):
                                            print("Please wait ...")
                                            username = find_credentials(username)
                                            del_credentials(username)
                                            print(
                                                f"ACCOUNT {username.account} Deleted Successfully!!!")
                                        else:
                                            print('\n')
                                            # print("dcfailed")

                                    elif shortCode == "ex": 
                                        print('Goodbye,have a beautiful time!!!')
                                        break
                                    else:
                                        print("Invalid shortcode")

        elif shortCode == "ex":
            print("THANK YOU FOR CHOOSING FUTURE SAVER! GOODBYE")
            break
if __name__ == '__main__':
    main()     
  