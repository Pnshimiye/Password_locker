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

    @classmethod
    def test_find_user(self):
            '''
            test to check if we can find a user by first name and password
            '''

            self.new_user.save_user()
            test_user: User("Carl","xyz")  
            test_user.save_user()

            current_user = User.find_user("Kami","xyz")

            self.assertEqual(current_user.first_name,test_user.first_name)

    





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

    def test_user_exists(self):
            '''
            test to check if we can return a Boolean  if we cannot find the user.
            '''

            self.new_user.save_user()
            test_user = User("Pauline","Nshimiye","ouliouli") 
            test_user.save_user()

            user_exists = User.user_exists("Pauline","ouliouli")

            self.assertTrue(user_exists)



 

if __name__ == '__main__':
  unittest.main()