import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file: 
        data = file.readlines()

        for contact in data:
            print(contact, end='')
    
    input('\npress any key')


def add_contact(file_name):
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = ''
        res += input('Input a surname of contact: ').title() + ' '
        res += input('Input a name of contact: ').title() + ' '
        res += input('Input a phone number of contact: ')

        file.write('\n'+ res)
    
    input('Contact was successfully added! Press any key for return')


def search_contact(file_name):
    os.system('CLS')
    target = input('Input a name of contact for searching: ').title()

    with open(file_name, 'r') as file: 
        contacts = file.readlines()

        for contact in contacts:                
            if target in contact:
                print(contact)
                break
        else :
            print('there is no contacts with this name.')
    input('press any key')  


def delete_contact(file_name):
    os.system('CLS')
    target = input('Input a name of the contact to delete: ').title()
    found = False

    with open(file_name, 'r') as file:
        contacts = file.readlines()

    with open(file_name, 'w') as file:
        for contact in contacts:
            if target in contact:
                print(contact)
                found = True
                print('number deleted')
            else:
                file.write(contact)      
        if not found:
            print('there is no contacts with this name.')
    input('press any key')


def rename_contact(file_name):
    os.system('CLS')
    target = input('Input a name of contact for searching: ').title()

    with open(file_name, 'r') as file:
        contacts = file.readlines()

    for i, contact in enumerate(contacts):
        if target in contact:
            print(contact)
            while True:
                rename_word = input('Input data to change: ').title()
                if ' ' not in rename_word:
                    break
                else:
                    print('Input correct data! ')
            if rename_word in contact:
                new_word = input('Input new data to change: ').title()
                contacts[i] = contact.replace(rename_word, new_word)
                with open(file_name, 'w') as file:
                    file.writelines(contacts)
            else:
                print('Data to change not found!')
            break
    else:
        print('there is no contacts with this name.')
    input('press any key')


def drawing():
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - search contact')
    print('4 - delete contact')
    print('5 - rename contact')
    print('6 - exit')

def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input("Input a number from 1 to 6: "))

        if user_choice == 1 :
            show_contacts(file_name)
        elif user_choice == 2 :
            add_contact(file_name)
        elif user_choice == 3 :
            search_contact(file_name)
        elif user_choice == 4 :
            delete_contact(file_name)
        elif user_choice == 5 :
            rename_contact(file_name)
        elif user_choice == 6 :
            print('Have a nice day!')
            return 

main('phonebook.txt')

