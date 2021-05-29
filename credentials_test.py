import unittest 
from credentials import Credentials # importing the credentials class

class TestCredentials(unittest.TestCase):
    '''
    test class defines test cases for the credentials 
    '''
    def setUp(self):
        '''
        set up method runs before other cases
        '''
        self.new_credentials = Credentials("You Tube","natcase","chebichii1")

    def test_init(self):
        self.assertEqual(self.new_credentials.account,"You Tube") 
        self.assertEqual(self.new_credentials.username,"natcase")
        self.assertEqual(self.new_credentials.password,"chebichii1")


    def test_save_credentials(self):
        '''
        test case to test if credentials is saved into the credentials list
        '''
        self.new_credentials.save_credentials() # saving new credentails
        self.assertEqual(len(Credentials.credentials_list), 1)
        



if __name__ == '__main__':
    unittest.main()        