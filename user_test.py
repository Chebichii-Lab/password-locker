import unittest 
from user import User 

class TestUser(unittest.TestCase):
    '''
    test class that defines cases for the user class
    '''
    def setUp(self):
        '''
         set up method to be run before each test case
        '''
        self.new_user= User("natcase",)