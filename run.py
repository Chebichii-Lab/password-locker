#!/usr/bin/env python3.8

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
        
    else:
                save_user(create_user(username, password))
                print(f'Congratulations 🎉, New Account has been created for: {username} using password: {password}')
                print("Proceed to login")
                print("username")
                entered_first_name = input()
                print("your password")
                entered_password = input()




if __name__ == '__main__':
    main()     
  