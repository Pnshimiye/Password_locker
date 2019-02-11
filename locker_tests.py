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
            test_usert.save_user()
            self.assertEqual(len(User.user_list),2)






class TestCredentials(unittest.TestCase):
              

  if __name__ == '__main__':
      unittest.main()