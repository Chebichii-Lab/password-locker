class Credentials :
    '''
    class that gets new instances for credentials
    '''
    credentials_list = []
    def __init__(self,account,username,password):
        self.account = account
        self.username = username
        self.password = password  

    def save_credentials(self):
        '''
        save method saves contact objects into credentials_list
        '''
        Credentials.credentials_list.append(self)    