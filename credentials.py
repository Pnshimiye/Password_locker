class Credential:
    '''
    Class to create  account credentials 
    ''' 
    pass

    Credentials_list = []

    
    def __init__(self,website_name,login_name,password):
        '''
        Method to define the properties for each credential object will hold. 
        '''     
        
      
        self.website_name = website_name       
        self.login_name = login_name
        self.password = password

    def save_credential(self):
        '''
        Function to save a newly created credential instance
        '''
        Credential.credentials_list.append(self)

    
    def generate_password(size=6, char= string.ascii_lowercase+string.digits):
        '''
        Function to generate a 6 character password for a credential
        '''
        gen_pass=''.join(random.choice(char) for _ in range(size))
        return gen_pass

    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
	  def find_by_website_name(self, website_name):
        '''
        Method that takes in a website_name and returns a credential that matches that website_name.
        '''
        for credential in cls.credentials_list:
          if credential.website_name == website_name:
            return credential
