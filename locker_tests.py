import unittest
from users import User
 # Importing the users class

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

            self.assertEqual(self.new_user.first_name,"James")
            self.assertEqual(self.new_user.second_name,"Muriuki")
            self.assertEqual(self.new_contact.phone_number,"0712345678")
          
