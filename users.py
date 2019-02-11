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


    
		