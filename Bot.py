from AddressBook import *
from abc import ABC, abstractmethod

class AbstractUserInterface(ABC):

    @abstractmethod
    def display_commands(self, commands):
        pass

    @abstractmethod
    def display_contacts(self,contacts):
        pass


class ConsoleUI(AbstractUserInterface):
    def display_contacts(self, contacts):
        result = []
        for account in contacts:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
            else:
                birth = ''
            if account['phones']:
                new_value = []
                for phone in account['phones']:
                    if phone:
                        new_value.append(phone)
                phone = ', '.join(new_value)
            else:
                phone = ''
            result.append(
                "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {phone} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50 + '\n')
        print('\n'.join(result))

    def display_commands(self, commands):
        format_str = str('{:%s%d}' % ('^', 20))
        for command in commands:
            print(format_str.format(command))


class Bot:
    def __init__(self):
        self.book = AddressBook()

    def handle(self, action):
        if action == 'add':
            name = Name(input("Name: ")).value.strip()
            phones = Phone().value
            birth = Birthday().value
            email = Email().value.strip()
            status = Status().value.strip()
            note = Note(input("Note: ")).value
            record = Record(name, phones, birth, email, status, note)
            return self.book.add(record)
        elif action == 'search':
            print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
            category = input('Search category: ')
            pattern = input('Search pattern: ')
            result = (self.book.search(pattern, category))
            for account in result:
                if account['birthday']:
                    birth = account['birthday'].strftime("%d/%m/%Y")
                    result = "_" * 50 + "\n" + f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                    print(result)
        elif action == 'edit':
            contact_name = input('Contact name: ')
            parameter = input('Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
            new_value = input("New Value: ")
            return self.book.edit(contact_name, parameter, new_value)
        elif action == 'remove':
            pattern = input("Remove (contact name or phone): ")
            return self.book.remove(pattern)
        elif action == 'save':
            file_name = input("File name: ")
            return self.book.save(file_name)
        elif action == 'load':
            file_name = input("File name: ")
            return self.book.load(file_name)
        elif action == 'congratulate':
            print(self.book.congratulate())
        elif action == 'view':
            print(self.book)
        elif action == 'exit':
            pass
        else:
            print("There is no such command!")
