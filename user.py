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