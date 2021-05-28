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
        self.new_user= User("natcase","chebichii1") # new user created

    def test__init(self):
        '''
        to test if the object has been initialized
        '''
        self.assertEqual(self.new_user.username, "natcase")
        self.assertEqual(self.new_user.password, "chebichii1")


if __name__ == '__main__':
    unittest.main()        

