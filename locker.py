#!/usr/bin/env python3.6
 

from users import User
from credentials import Credential
 


  
def create_user (first_name, second_name, password):

    '''
    Function to create a new user
    '''
    new_user = User(first_name, second_name, password)
    return new_user

def save_user(user):
    '''
    Function to save users
    '''
    user.save_user()
  
  # def find_user(first_name,password):
  #     '''
  #     Function that finds a user by name and password and returns the user
  #     '''
  #     return User.check_user(cls,first_name,password)

def check_existing_user(first_name,password):
    '''
    Function that check if a user  exists with a first name  and password  and return a Boolean
    '''
    return User.user_exists(first_name,password)


def create_credential(first_name,website_name,login_name,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(first_name,website_name,login_name,password)
    return new_credential

def generate_password():
    '''
    Function to generate a password automatically
    '''
    gen_pass = Credential.generate_password()
    return gen_pass


def save_credential(self):
    '''
    Function to save credentials
    '''
    Credential.save_credential(self)

def find_credential(website_name):
    '''
    Function that finds a credential using a website name
    '''
    return Credential.find_by_website_name(website_name)

def display_credentials(data):
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials(data)

def main():

      print("Hello!! Welcome to your credential locker")
      print("Please would you Please tell us your name?")
      
      user_name = input()

      print(f"Hello {user_name}. what would you like to do?")
      print('\n')
      while True:
        print("Use these short codes : cuc - create a user account, del- delete credential lgn -log into the locker,cc - create a new credential, dc - display credentials, ex -exit")
        short_code = input().lower()

        if short_code == 'ex':
		              	break

        elif short_code == 'cuc':
                print("Welcome ,New User!!!")
                print("Proceed to creating your account ")
                print("-"*10)

                print ("First name:..")
                first_name = input()

                print("Last name:..")
                second_name = input()

                print("password:..")
                password = input()                 


                save_user(create_user(first_name, second_name, password)) 
                new_user = User(first_name,second_name, password) 
                print ('\n')
                print(f"New user {first_name} {second_name} has been created")
                print ('\n')

                
                print("Welcome again!! Time to start storing your credentials! shall we?")

        elif short_code == 'lgn':

                print("Please enter your first name and password to log into your credential list")

                print("First name: ")
                first_name = input()
                print ("Password: ")
                password = input()

                if  check_existing_user(first_name,password):
                  search_user = User(first_name,second_name,password)
                  print(f"{search_user.first_name} {search_user.password}")
                  print('-' * 20)

                  print(f"welcome {search_user.first_name} choose a suitable short code for you to continue   " )
                    
                else:
                  print("Sorry you do not seem to have an account here. to create this account choose the cuc optin in the short codes")


        elif short_code == 'cc':

    
                    print("New credential")
                    print("-"*10)

                    print ("First name ....")
                    first_name = input()

                    print("Website Name")
                    website_name = input() 

                    print("login Name...")
                    login_name = input()
                #     while True
                    
                    print("Please choose an option for entering a password: ep-enter existing password, gp-generate a password")
                    psw_choice = input("Enter an option:").lower().strip()
                    print("-"*8)
                    if psw_choice == 'ep':
                          print("")
                          password = input('Enter your password: ').strip() 
                          # break
                    elif  psw_choice == 'gp':
                          password = generate_password()
                          
                          print("password...")
                          password = input()
                          new_credential= Credential(first_name,website_name,login_name,password)
                          new_credential.save_credential() # create and save new contact.
                          print ('\n')
                          print(f"New credential {login_name} {password} created")
                          print ('\n')
                          print("what would like to do next? chose the relecant short code")

if __name__ == '__main__':
        main()