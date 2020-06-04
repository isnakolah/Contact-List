#!/usr/bin/env python3.8

from contact import Contact
import pyperclip

def create_contact(fname, lname, phone, email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(fname, lname, phone, email)
    return new_contact


def save_contacts(contact):
    '''
    Function to save contact.
    '''
    contact.save_contact()


def del_contact(contact):
    '''
    Function to delete a contact.
    '''
    contact.delete_contact()


def find_contact(number):
    '''
    Function that finds a contact by number and returns the contact.
    '''
    return Contact.find_by_number(number)


def check_existing_contacts(number):
    '''
    Function that checks if a contact with that number and return a Boolean
    '''
    return Contact.contact_exist(number)


def display_contacts():
    '''
    Function that returns all the saved contacts.
    '''
    return Contact.display_contacts()

def copy_email(number):
    '''
    Method that handles the behavior of copying the email to the clipboard
    '''
    return Contact.copy_email(number)
    
def main():
    print('Hello Welcome to your contact list. What is your name?')
    user_name = input()
    print(f'Hello {user_name}. What would you like to do?\n')

    while True:
        print('Use these short codes : cc - create new contact, dc - display contacts, fc - find a contact, ex - exit the contact list, dl - delete a contact copy - cp a contact')

        short_code = input().lower()

        if short_code == 'cc':
            print('New Contact')
            print('-'*10)

            print('First name: ')
            f_name = input()

            print('Last name: ')
            l_name = input()

            print('Phone number: ')
            p_number = input()

            print('Email address: ')
            e_address = input()

            save_contacts(create_contact(f_name, l_name, p_number, e_address))
            print('\n')
            print(f'New Contact {f_name} {l_name} created.\n')

        elif short_code == 'dc':
            if display_contacts():
                print('Here is a list of all your contacts\n')

                for contact in display_contacts():
                    print(f'{contact.first_name} {contact.last_name} {contact.phone_number}\n')

            else:
                print('\nYou don\'t seem to have any contacts saved yet\n')

        elif short_code == 'fc':
            print('Enter the number you want to search for')

            search_number = input()
            if check_existing_contacts(search_number):
                search_contact = find_contact(search_number)
                print(f'{search_contact.first_name} {search_contact.last_name}')
                print('-' * 20)

                print(f'Phone number: {search_contact.phone_number}')
                print(f'Email address: {search_contact.email}')
            else:
                print('That contact does not exist')
        
        elif short_code == 'dl':
            print('Enter the number of the contact you want to delete: ')
            del_contact = input()
            del_contact(find_contact(del_contact))

        elif short_code == 'cp':
            print('Enter the number of the contact email you want to copy: ')
            copy_contact = input()
            copy_email(copy_contact)

        elif short_code == 'ex':
            print('Bye.')
            break
        else:
            print('I really didn\'t get that please use the short codes')


if __name__ == "__main__":
    main()