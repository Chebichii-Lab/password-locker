class Credentials :
    '''
    class that gets new instances for credentials
    '''
    credentials_list = []
    def __init__(self,account,username,password):
        self.account = account
        self.username = username
        self.password = password   