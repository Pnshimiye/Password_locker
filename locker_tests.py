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
          
