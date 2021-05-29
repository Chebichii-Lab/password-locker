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

    def tearDown(self):
        '''
        tear down method does clean up after each test case has been run
        '''
        Credentials.credentials_list =[]

    def test_save_multiple_credentials(self):
        '''
        test to check if we can save multiple credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","papa","guks001")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_del_credentials(self):
        '''
        test to see if we can remove a credential from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","papa","guks001")
        test_credentials.save_credentials()
        self.new_credentials.del_credentials() # deleting credentials object
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credentials_by_username(self):
        '''
        test to see if we can find credentials by username and display information
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","papa","guks001") # new credential
        test_credentials.save_credentials()
        found_credentials = Credentials.find_by_username("papa")
        self.assertEqual(found_credentials.password, test_credentials.password) 

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list) 

    def test_exists_credentials(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credential.save_credential()
        test_credentials = Credentials("Twitter","papa", "guks001") # new contact
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("papa")

        self.assertTrue(credentials_exists)   

   
if __name__ == '__main__':
    unittest.main()        