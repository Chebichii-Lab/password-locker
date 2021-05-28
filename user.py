class User :
    '''
    class that generates new instances of user
    '''
    user_list = [] 
    def __init__(self, username, password):
        self.username = username
        self.password = password