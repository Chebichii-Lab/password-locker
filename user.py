class User :
    '''
    class that generates new instances of user
    '''
    user_list = [] 
    def __init__(self, username, password):
        self.username = username
        self.password = password

    
    
    def save_user(self):
        '''
        save user method  saves user objects in the user list
        '''  
        User.user_list.append(self)

    @classmethod
    def user_exist(cls,username,password):    
        '''
        method that checks if users and password exists
        '''
        for user in cls.user_list:
            if{user.username == username and user.password == password}:
                return True

        return False