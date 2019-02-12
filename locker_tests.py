import unittest
from users import User
from credentials import Credential
 
  

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviours.

    Arguments:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
            '''
            Set up method to run before each test cases.
            '''
            self.new_user = User("Pauline","Nshimiye","ouliouli")
    def test_init(self):
            '''
            test_init test case to test if the object is initialized properly
            '''

            self.assertEqual(self.new_user.first_name,"Pauline")
            self.assertEqual(self.new_user.second_name,"Nshimiye")
            self.assertEqual(self.new_user.password,"ouliouli")


    def test_save_user(self):
            '''
            test_save_user checks if the user instance is being saved to the user list
            '''
            self.new_user.save_user() 
            self.assertEqual(len(User.users_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.users_list = []


    def test_save_multiple_users(self):
            '''
           test_save_multiple_users tests if we can save more than one users on our user list
            '''
            self.new_user.save_user()
            test_user = User("Alice","Umulisa","aliumu") 
            test_user.save_user()
            self.assertEqual(len(User.users_list),2)

    # @classmethod
    # def test_find_user(self):
    #         '''
    #         test to check if we can find a user by first name and password
    #         '''

    #         self.new_user.save_user()
    #         test_user: User("Carl","xyz")  
    #         test_user.save_user()

    #         current_user = User.find_user("Kami","xyz")

    #         self.assertEqual(current_user.first_name,test_user.first_name)

    





    def test_check_user(self):
            '''
            Function to test whether the login in function check_user works as expected
            '''
            self.new_user = User("carl","Kami", "xyz")
            self.new_user.save_user()
            user_x = User("carl","koy","xyz")
            user_x.save_user()

            for user in User.users_list:
              if user.first_name == user_x.first_name and user.password == user_x.password:
                current_user = user.first_name
            return current_user

            self.assertEqual(current_user,Credential.check_user(user_x.password,user_x.first_name))



    # if __name__ == '__main__':
  
    #   unittest.main()

 
 
# class TestCredentials(unittest.TestCase):

#     '''
#     Test class that defines test cases for the credential class behaviours.

#     Arguments:
#         unittest.TestCase: TestCase class that helps in creating test cases

#     '''
#     def setUp(self):
#             '''
#             Set up method to run before each test cases.
#             '''
#             self.new_credential = Credential("Carl","Twitter","Carl","xyz")

#     def test_init(self):
#             '''
#             test_init test case to test if the object is initialized properly
#             '''

#             self.assertEqual(self.new_credential.first_name,"Carl")
#             self.assertEqual(self.new_user.website_name,"Twitter")
#             self.assertEqual(self.new_user.login_name,"carl")
#             self.assertEqual(self.new_user.password,"xyz")


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
        self.new_credential = Credential("Carl", "Twitter","Carl","xyz")

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

    def test_save_multiple_users(self):

            '''
            test_save_multiple_credentials tests if we can save more than one users on our user list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Carl","Twitter","carl","xyz") 
            test_credential.save_credential()
            self.assertEqual(len(Credential.credentials_list),2)

    @classmethod
    def test_find_credential(self):
            '''
            test to check if we can find a credential by webisite name
            '''
            self.new_credential.save_credential()
            test_credential = credential("Max","Facebook","max","abc")  
            test_credential.save_credential()

            found_credential = Credential.find_credential("Facebook")

            self.assertEqual(found_credental.website_name,test_credential.website_name)

    def test_delete_credential(self):
            '''
            To test if we can remove a credential from our credential list
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
            self.assertEqual(Credential.display_credentials(),Credential.credentials_list)
      
    def test_find_by_website_name(self):
            '''
            Test to check if the find_by_website_name method returns the correct credential
            '''
            self.new_credential.save_credential()
            twitter = Credential('Jane','Twitter','maryjoe','pswd100')
            twitter.save_credentials()
            credential_exists = Credential.find_by_site_name('Twitter')
            self.assertEqual(credential_exists,twitter)
 

    if __name__ == '__main__':
      unittest.main()