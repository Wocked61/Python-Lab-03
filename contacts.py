'''
Name: Dylan Phan
Date: 9/13/2024
File Purpose: putting contacts in a list and making it a program
'''
contacts = [] 
def print_list(contacts = []) :
    #this function prints out every contact in the list contacts
    print('''
================== CONTACT LIST ==================
Index   First Name            Last Name
======  ====================  ====================''')
    for i in range(len(contacts)) :
        print(f'{str(i):8}{contacts[i][0]:22}{contacts[i][1]:22}')

def add_contact(contacts, first_name=None, last_name=None) :
    #This function adds a contact to the list of contacts
    contacts.append([first_name,last_name])
    return True

def modify_contact(contacts, first_name=None, last_name=None, index=0) :
    #this function modifies the contacts list and changes it to the user's request
    if (index >= len(contacts) or index < 0):
        print('Invalid index number.')
        return False
    contacts[index] = [first_name,last_name]
    return True

def delete_contact(contacts, index=0) :
    #this function deletes a contact from the contact list
    if (index >= len(contacts) or index < 0):
        print('Invalid index number.')
        return False
    else :
        del contacts[index]
        return True

def sort_contacts(contacts, column=0) :
        contacts.sort(key=lambda contact: contact[column])
        return contacts