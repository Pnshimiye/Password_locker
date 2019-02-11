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


    def delete_credential(self):

        '''
        delete_contact method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self