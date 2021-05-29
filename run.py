#!/usr/bin/env python3.8

from credentials import Credentials
from user import User 
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
    credentials.delete_credentials()

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


def main():
    print("Hello, Welcome to FUTURE SAVER!. Create an account to save your passwords.")
    print('Enter your username')
    username = input()
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
                print(f'Congratulations 🎉, New Account has been created for: {username} using password: {password}')
                print("Proceed to login")
                print("username")
                entered_username= input()
                print("your password")
                entered_password = input()

    while entered_username != username or entered_password != password:
                print("Invalid username or password")
                print('username')
                entered_username = input()
                print("Your password")
                entered_password = input()
    else:                
        
                print(f'Welcome back  {entered_username} 😍. please choose an option to continue')


if __name__ == '__main__':
    main()     
  