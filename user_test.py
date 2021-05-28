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

    def test_save_user(self):
        '''
        test to save user details in the user list
        '''
        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.user_list), 1)







        

if __name__ == '__main__':
    unittest.main()        

