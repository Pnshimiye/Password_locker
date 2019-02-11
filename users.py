class User:
	'''
	A class to create  application users accounts
	'''

	users_list = []

	def __init__(self,first_name,second_name,password):

		'''
		Method to define the properties for each user object will hold.
		'''

	 
		self.first_name = first_name
		self.second_name = second_name
		self.password = password

	def save_user(self):
		'''
		Function to save a newly created user instance
		'''
		User.users_list.append(self)

 

    
		 # # user_credentials_list= [] 
  # @classmethod
  # def check_user(self,first_name,password):
  #   '''
  #   Method that checks if the name and password entered match entries in the users_list
  #   '''
  #   current_user = ' '
  #   for user in User.users_list:
  #     if (user.first_name == first_name and user.password == password):
  #       current_user = user.first_name
  #       return current_user