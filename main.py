'''
# Name: Dylan Phan
# Date: 9/13/2024
# File Purpose: contacts program main
'''

from contacts import *

contacts_list = []
in_index_first = None
in_index_last = None

while True:
    inp1 = input('''
        *** TUFFY TITAN CONTACT MAIN MENU

1. Print list
2. Add contact
3. Modify contact
4. Delete contact
5. Exit the program
6. Sort list by last name
7. Exit the program
                 
Enter menu choice: ''')
    if (inp1 == '1') :
        print_list(contacts_list)
    if (inp1 == '2') :
        in_index_first = input('Enter first name: ')
        in_index_last = input('Enter last name: ')
        add_contact(contacts_list, first_name=in_index_first , last_name=in_index_last)
    if (inp1 == '3'):
        in_index = int(input('\nEnter the index number: '))
        in_index_first= input('Enter first name: ')
        in_index_last = input('Enter last name: ')
        modify_contact(contacts_list, index=in_index, first_name=in_index_first, last_name=in_index_last)
    if (inp1 == '4') :
        in_index = int(input('\nEnter the index number: '))
        delete_contact(contacts_list, index=in_index)
    if (inp1 == '5') :
        sort_contacts(contacts_list, column=0)
    if (inp1 == '6') :
        sort_contacts(contacts_list, column=1)
    if (inp1 == '7') :
        break