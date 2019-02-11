class Credential:
    '''
    Class to create  account credentials 
    ''' 
    pass

    Credentials_list = []

    
    def __init__(self,user_fname,website_name,login_name,password):
        '''
        Method to define the properties for each user object will hold. 
        '''

        self.user_fname = user_fname
        self.website_name = website_name
        self.login_name = login_name
        self.password = password