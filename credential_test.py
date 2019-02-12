import unittest 
from credentials import Credential
 
class TestCredential(unittest.TestCase):

    """
    Test class that defines test cases for the credential class behaviours.

    Arguments:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Carl","Twitter","carl","xyz")

    def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''
            self.assertEqual(self.new_credential.first_name,"Carl")
            self.assertEqual(self.new_credential.website_name,"Twitter")
            self.assertEqual(self.new_credential.login_name,"carl")
            self.assertEqual(self.new_credential.password,"xyz")

    def test_save_credential(self):
            '''
            test_save_credential checks if the user instance is being saved to the user list
            '''
            self.new_credential.save_credential() 
            self.assertEqual(len(Credential.credentials_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credentials_list = []

    def test_save_multiple_credentials(self):

            '''
            test_save_multiple_credentials tests if we can save more than one users on our user list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Carl","Twitter","carl","xyz") 
            test_credential.save_credential()
            self.assertEqual(len(Credential.credentials_list),2)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all  credentials saved
        '''

        self.assertEqual(Credential.display_credential(),Credential.credentials_list)

   
    # def test_find_credential(self):
    #         '''
    #         test to check if we can find a credential by webisite name
    #         '''                    
    #         for credential in self.credentials_list:
    #           if credential.site_name == site_name:
    #             return credential

    #         # self.new_credential.save_credential()
    #         # test_credential = Credential("Max","Facebook","max","abc")  
    #         # test_credential.save_credential()

    #         # found_credential = Credential.find_credential("Facebook")

    #         # self.assertEqual(found_credental.website_name,test_credential.website_name)

    def test_delete_credential(self):
            '''
            To test if we can remove a credential from our credentials list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Carl","Twitter","carl","xyz")  
            test_credential.save_credential()

            self.new_credential.delete_credential() 
            self.assertEqual(len(Credential.credentials_list),1)

    def test_display_all_credentials(self):
            '''
            method that returns a list of all credentials  saved
            '''
            self.assertEqual(Credential.display_credentials(self),Credential.credentials_list)
      
    def test_find_by_website_name(self):
            '''
            test to check if we can find a  credential by using a website name
            '''

            self.new_credential.save_credential()
            test_credential = Credential("Carl","Twitter","carl","xyz")
            test_credential.save_credential()

            found_credential = Credential.find_by_website_name("Twitter")

            self.assertEqual(found_credential.website_name,test_credential.website_name)
        
if __name__ == '__main__':
  unittest.main() 