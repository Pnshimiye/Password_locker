class Credential:
	'''
	Class to create  account credentials 
	''' 
 
	# credentials_list = []
  
  user_credentials_list = []



	@classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user

	def __init__(self,user_fname,website_name,login_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables

		self.user_fname = user_fname
		self.website_name = website_name
		self.login_name = login_name
		self.password = password