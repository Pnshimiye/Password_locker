#!/usr/bin/env python3.6
 

from users import User
from credentials import Credential

  
def create_user (first_name, second_name, password):

    '''
    Function to create a new user
    '''
    new_user = User(first_name, second_name, password)
    return new_user

def save_users(user):
    '''
    Function to save users
    '''
    user.save_users()
  
  # def find_user(first_name,password):
  #     '''
  #     Function that finds a user by name and password and returns the user
  #     '''
  #     return User.check_user(cls,first_name,password)

def check_existing_user(first_name,password):
    '''
    Function that check if a user  exists with a first name  and password  and return a Boolean
    '''
    return User.user_exists( first_name,password)


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


def save_credentials(credential):
    '''
    Function to save credentials
    '''
    Credential.save_credential()

def find_credential(website_name):
    '''
    Function that finds a credential using a website name
    '''
    return Credential.find_by_website_name(website_name)

def main():

      print("Hello Welcome to your credential locker")
      user_name = input()

      print(f"Hello {user_name}. what would you like to do?")
      print('\n')

      while True:
            print("Use these short codes : nac - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Contact")
                    print("-"*10)

                    print ("First name ....")
                    f_name = input()

                    print("Last name ...")
                    l_name = input()

                    print("Phone number ...")
                    p_number = input()

                    print("Email address ...")
                    e_address = input()


                    save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
                    print ('\n')
                    print(f"New Contact {f_name} {l_name} created")
                    print ('\n')

            elif short_code == 'dc':

                    if display_contacts():
                            print("Here is a list of all your contacts")
                            print('\n')

                            for contact in display_contacts():
                                    print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any contacts saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the number you want to search for")

                    search_number = input()
                    if check_existing_contacts(search_number):
                            search_contact = find_contact(search_number)
                            print(f"{search_contact.first_name} {search_contact.last_name}")
                            print('-' * 20)

                            print(f"Phone number.......{search_contact.phone_number}")
                            print(f"Email address.......{search_contact.email}")
                    else:
                            print("That contact does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()
