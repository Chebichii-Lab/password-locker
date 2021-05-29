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

    def del_credentials(self):
        '''
        delete_credentials method deletes a saved credential from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        method that takes in a username and returns a credential that matches the username
        '''
        for credentials in cls.credentials_list:
            if credentials.username == username:
                return credentials  

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credentials_list

    @classmethod
    def credentials_exist(cls, username):
        '''
        method that checks if a credential exists
        '''
        for credentials in cls.credentials_list:
            if credentials.username == username:
                return True

        return False

    