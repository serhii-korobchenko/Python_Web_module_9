# BOT assistent
# CLI - Command Line Interface
#              Architecture :
#                   - command`s parser
#                   - decorator --> Rise exceptions
#                   - command`s processing functions (Handlers):
#                           - hello_func                            --- first greeting
#                           - add_func         --> add_record       --- create new contact
#                           - change_func      --> edit_phone       --- change  telephone number for existed contact
#                           - phone_func                            --- show telephone number
#                           - show_func                             --- show all contacts (name telephone number)
# update+                   - see_func                              --- show n records (you could use this command several times)
#                           - addnum_func      --> add_phone        --- add aditional tel number for certain contact
#                           - del_func         --> del_phone        --- del tel number for certain contact
#                           - birth_func                            --- add date of birthday in data format
#                           - nextbirth_func   --> days_to_birthday --- show how many days left up to next birthday
#                           - help_func                             --- bot show commands explanations
#                           - save_func                             --- save data base in file: name (without extention)
#                           - load_func                                       --- load data base from file: name (without extention)
#                           - lookup_func                                     --- find text in records (no difference which case of characters)
#                           - good_buy_func                                   --- bot stops work and messege "Good bye!"
# new_func+                  - del_record_hand     --> del_record              --- delete record from AddressBook
# new_func+                  - add_email_head      --> add_email               --- add email to record (with regex check)
# new_func+                  - add_adress_head     --> add_adress              --- add adress to record
# new_func+                  - add_notes_head      --> add_notes               --- add notes to record
# new_func+                  - find_notes_by_tages_head --> find_notes_by_tages --- looking up notes by tages (#tage#)
# new_func+                  - sort_notes_by_tages_head --> sort_notes_by_tages --- sorting up notes by tages (#tage#)
# new_func+                  - del_notes_by_tages_head --> sort_notes_by_tages --- del notes by tages (#tage#)
# new_func+                  - change_notes_by_tages_head --> sort_notes_by_tages --- change notes by tages (#tage#)
# new_func+                  - sort_files                                       --- sort files in folder
# new_func+                  - guess_command                                    --- analizing taping and try to guess command
# new_func+                  - birthday_in_days_hand    --> birthday_in_days    --- display list of contacts, who have birthday in x days
#
#
#                   - request-answear loop

# Input - dict(name: telephone number)
# Requirements:
#              - telephone number format: 0675223345 - 10 digits;
#              - bot undestands commands:
#                          - "hello" - answear: "How can I help you?"
#                          - "add' name telephone number" - save new contact
#                          - "change' name telephone number" - change telephone number for existed contact
#                          - "phone' name" - show telephone number
#                          - "show all" - show all contacts (name telephone number)
#                          - "see' n" - show n records (you could use this command several times)
#                          - "addnum' name telephone number" - add aditional tel number for certain contact
#                          - "del' name telephone number" - del tel number for certain contact
#                          - "addbirth" name birthday - add date of birthday in data format
#                          - "nextbirth" name - show how many days left up to next birthday
#                          - "help" - bot show commands explanations
#                          - "save" name - save data base in file: name (without extention)
#                          - "load name" - load data base from file: name (without extention)
#                          - "lookup' text" - find text in records (no difference which case of characters)
# new+                      - "delrec' name" - delete record from AddressBook
# new+                      - "addemail' name email" - add email to record
# new+                      - "changeemail" name new_email - change all emails on new one
# new+                      - "addadress' name text" - add adress to record
# new+                      - "addnotes' name text" - add notes to record
# new+                      - "findtag' teg_text" - looking up notes by tages (#tage#)
# new+                      - "sortnotes' teg_text" - sorting up notes by tages (#tage#)
# new+                      - "delnotes' teg_text" - del notes by tages (#tage#)
# new+                      - "changenotes' teg_text" - change notes by tages (#tage#)
# new+                      - "sortfiles' folder_path" - sort files in folder
# new+                      - "guess'    - switch on guess mode ---> analizing taping and try to guess command
# new+                      - "checkbirth' days_number - display list of contacts, who have birthday in x days
#                           - "good bye" or "close" or "exit" - bot stops work and messege "Good bye!"
#
#
# Updated Class_structure:
#+---------------+
#|      ABC      |
#|---------------|
#|               |
#+---------------+
#       .          
#      /_\         
#       |          
#       |          
#       |          
#       |          
#       |          
#+----------------+
#|   Presenter    |
#|----------------|
#| see_iteration  |
#| show_all       |
#+----------------+
#       .                                     
#      /_\                                    
#       |                   [ Presenter ]     
#       |                         .           
#       |                        /_\          
#       |                         |           
#       |                         |           
#+----------------+       +------------------+
#| PresenterNotes |       | PresenterRecords |
#|----------------|       |------------------|
#| see_iteration  |       | see_iteration    |
#| show_all       |       | show_all         |
#+----------------+       +------------------+
         
         
         
         
#+-------+
#| Field |
#|-------|
#|       |
#+-------+
#   .
#  /_\
#   |              [ Field ]            [ Field ]          [ Field ]             [ Field ]
#   |                  .                    .                  .                     .
#   |                 /_\                  /_\                /_\                   /_\
#   |                  |                    |                  |                     |
#   |                  |                    |                  |                     |
#+-------+       +--------------+       +----------+       +----------+       +---------------+
#|  Name |       |    Email     |       |  Phone   |       | Birthday |       |     Adress    |
#|-------|       |--------------|       |----------|       |----------|       |---------------|
#| value |       | value        |       | __value  |       | __value  |       | value         |
#+-------+       |--------------|       | value    |       | value    |       |---------------|
#                | __init__     |       |----------|       |----------|       | __init__      |
#                | change_email |       | __init__ |       | __init__ |       | change_adress |
#                +--------------+       +----------+       +----------+       +---------------+
                       
                       
                       
                       
#+---------------------+
#|       UserDict      |
#|---------------------|
#|                     |
#+---------------------+
         #  .
         # /_\
#           |
#           |
#           |
#           |
#           |
# +---------------------+
# |     AddressBook     |
# |---------------------|
# | data                |  ---->  [ PresenterRecords ]
# | note                |  ---->  [ Record ]
# | notes_data          |
# | phone               |
# | presenter           |
# | tag                 |
# |---------------------|
# | __init__            |
# | add_notes           |
# | add_record          |
# | birthday_in_days    |
# | del_record          |
# | find_notes_by_tages |
# | iterator            |
# | sort_notes_by_tages |
# +---------------------+
#
#
#
#
# +-----------------------+
# |       Exception       |
# |-----------------------|
# |                       |
# +-----------------------+
#            .
#           /_\
#            |                             [ Exception ]                          [ Exception ]                 [ Exception ]
#            |                                   .                                      .                             .
#            |                                  /_\                                    /_\                           /_\
#            |                                   |                                      |                             |
#            |                                   |                                      |                             |
# +-----------------------+       +--------------------------------+       +---------------------------+       +---------------+
# | NameDoesNotExistError |       | BirthdayDoesNotMathFormatError |       | TelDoesNotMathFormatError |       | TryAgainError |
# |-----------------------|       |--------------------------------|       |---------------------------|       |---------------|
# | status                |       | status                         |       | status                    |       | status        |
# +-----------------------+       +--------------------------------+       +---------------------------+       +---------------+
#
#
#
#
# +--------------+                                  +------------------+
# |    Notes     |                                  |      Record      |
# |--------------|                                  |------------------|
# | note         |  ---->  [ PresenterNotes ]       | adress           |  ---->  [ Adress ]
# | presenter    |                                  | email            |  ---->  [ Email ]
# | result       |                                  | name             |  ---->  [ Name ]
# | tag          |                                  | phone            |  ---->  [ Phone ]
# |--------------|                                  | record_dict      |
# | __init__     |                                  |------------------|
# | change_notes |                                  | __init__         |
# | del_notes    |                                  | add_adress       |
# +--------------+                                  | add_email        |
#                                                   | add_phone        |
#                                                   | days_to_birthday |
#                                                   | del_phone        |
#                                                   | edit_phone       |
#                                                   +------------------+

#


import os
from ast import List
from multiprocessing.sharedctypes import Value
import re
from collections import UserDict
from datetime import datetime
import pickle
from copy import copy, deepcopy
import csv
from pathlib import Path
#from pynput import keyboard
import shutil
from abc import abstractmethod, ABC


# GLOBALS

x = 0
page = 1
command_list = []


class AddressBook (UserDict):

    def __init__(self):
        UserDict.__init__(self)
        self.notes_data = {}
        self.presenter = PresenterRecords()
        


    def add_record(self, name, phone):

        self.phone = phone
        Name.value = name
        self.data[name] = Record()

    def iterator(self):

        global x
        global page

        while x <= len(self.data):

            for key_in, value_in in self.data[list(self.data)[x]].record_dict.items():

                if value_in:
                    if isinstance(value_in, list):
                        print(
                            f"{key_in} : {', '.join(map(str, value_in))} | ", end=" ")
                    else:
                        print(f"{key_in} : { value_in} | ", end=" ")

            x += 1
            page += 1
            yield x

    def del_record(self, name):
        del self.data[name]

    def add_notes(self, name, phone):  # name=tag phone=note

        self.tag = name
        self.note = phone
        #self.notes_data = {}
        self.notes_data.update({self.tag: self.note})

        if(os.path.exists('notes.csv') and os.path.isfile('notes.csv')):
            with open('notes.csv', 'a', newline='') as fh:
                field_names = ['tag', 'note']
                writer = csv.DictWriter(fh, fieldnames=field_names)
                writer.writerow({'tag': self.tag, 'note': self.note})

        else:
            with open('notes.csv', 'w', newline='') as fh:
                field_names = ['tag', 'note']
                writer = csv.DictWriter(fh, fieldnames=field_names)
                writer.writeheader()
                writer.writerow({'tag': self.tag, 'note': self.note})

        
        return self.tag

    def find_notes_by_tages(self, name):  # name=tag

        self.tag = name

        with open('notes.csv', newline='') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                if row['tag'] == self.tag:
                    result = row['tag'] + ' ' + row['note']
                    break
                else:
                    result = ''
        if result == '':
            print(f'Nothing found by tag {self.tag}')
        else:
            print(result)

    def sort_notes_by_tages(self):

        with open('notes.csv', newline='') as fh:
            result = {}
            reader = csv.DictReader(fh)
            for row in reader:
                result.update({row['tag']: row['note']})

        for k in sorted(result):
            print(k, result[k])
##################################################################

    def birthday_in_days(self, number_days):
        
        checked_date = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day + int(number_days))
        flag_birth = 0
        for key, value in add_book.items():
            record_date = datetime(year=datetime.now().year, month=add_book.data[key].record_dict['Birthday'].month, day=add_book.data[key].record_dict['Birthday'].day)
            if checked_date == record_date:
                print (f'{key} has birthday in {number_days} days! ')
                flag_birth +=1

            
        if flag_birth == 0:
            print (f'No one  has birthday in {number_days} days!')
                   

class Field:
    pass


class Name (Field):

    value = None


class Phone (Field):

    def __init__(self, value) -> None:
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):

        if re.match(r"^[0-9]{10,10}$", new_value):

            #print ('Number format has been checked successfully!')
            self.__value = new_value

        else:
            print('Telephone number does not match format!')

class Notes:

    def __init__(self):
        self.presenter = PresenterNotes()

    def change_notes(self, name, phone):  # name=tag phone=note
        self.tag = name
        self.note = phone
        self.result = {}

        with open('notes.csv', newline='') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                self.result.update({row['tag']: row['note']})
        self.result.pop(self.tag)
        self.result.update({self.tag: self.note})

        counter = 0
        for k, v in self.result.items():
            if counter == 0:
                with open('notes.csv', 'w', newline='') as fh:
                    field_names = ['tag', 'note']
                    writer = csv.DictWriter(fh, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerow({'tag': k, 'note': v})
            else:
                with open('notes.csv', 'a', newline='') as fh:
                    field_names = ['tag', 'note']
                    writer = csv.DictWriter(fh, fieldnames=field_names)
                    # writer.writeheader()
                    writer.writerow({'tag': k, 'note': v})
            counter += 1
        print(f'Note with tag {self.tag} updated')

    def del_notes(self, name):  # name=tag
        self.tag = name
        self.result = {}
        with open('notes.csv', newline='') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                self.result.update({row['tag']: row['note']})
        self.result.pop(self.tag)

        counter = 0
        for k, v in self.result.items():
            if counter == 0:
                with open('notes.csv', 'w', newline='') as fh:
                    field_names = ['tag', 'note']
                    writer = csv.DictWriter(fh, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerow({'tag': k, 'note': v})
            else:
                with open('notes.csv', 'a', newline='') as fh:
                    field_names = ['tag', 'note']
                    writer = csv.DictWriter(fh, fieldnames=field_names)
                    # writer.writeheader()
                    writer.writerow({'tag': k, 'note': v})
            counter += 1
        print(f'Note with tag {self.tag} deleted')


##########################################################


class Email (Field):

    def __init__(self) -> None:
        self.value = None

    def change_email(self, name, new_email):
        add_book.data[name].record_dict['Email'].clear()
        add_book.data[name].record_dict['Email'].append(new_email)


class Adress (Field):

    def __init__(self) -> None:
        self.value = None

    def change_adress(self):
        pass

class Birthday (Field):

    def __init__(self, value=None) -> None:
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):

        try:

            if re.match(r"\d{2}.\d{2}.\d{4}", new_value):

                birthday_data_list = new_value.split('.')

                birthday_datatime = datetime(year=int(birthday_data_list[2]), month=int(
                    birthday_data_list[1]), day=int(birthday_data_list[0])).date()

                self.__value = birthday_datatime
                print('Birthday date has been added successfully!')

            else:
                raise BirthdayDoesNotMathFormatError

        except BirthdayDoesNotMathFormatError:

            print("You have to set date in next format: dd.mm.yyyy! ")
            BirthdayDoesNotMathFormatError.status = 1

        except KeyError:
            print("This contact does not exist! First - set up appropriate contact")
            TryAgainError.status = 1

        except ValueError:
            print("You have to set date in next format: 1-31.1-12.0000-9999!")
            TryAgainError.status = 1
class Record:

    def __init__(self) -> None:

        self.name = Name()
        self.phone = Phone(add_book.phone)
        self.email = Email()
        self.adress = Adress()
        self.record_dict = {
            'Name': self.name.value,
            'Phone': [self.phone.value],
            'Birthday': None,
            'Email': None,
            'Adress': None
        }

    def add_phone(self, name, phone):
        # add_book.data[name].append(phone)
        add_book.data[name].record_dict['Phone'].append(phone)

    def del_phone(self, name, phone):
        add_book.data[name].record_dict['Phone'].remove(phone)

    def edit_phone(self, name, new_phone):
        add_book.data[name].record_dict['Phone'].clear()
        add_book.data[name].record_dict['Phone'].append(new_phone)

    def days_to_birthday(self, name):
        next_year_birthday = datetime(year=datetime.now(
        ).year + 1, month=add_book.data[name].record_dict['Birthday'].month, day=add_book.data[name].record_dict['Birthday'].day)
        this_year_birthday = datetime(year=datetime.now(
        ).year, month=add_book.data[name].record_dict['Birthday'].month, day=add_book.data[name].record_dict['Birthday'].day)
        if this_year_birthday <= datetime.now():
            difference = next_year_birthday - datetime.now()
        else:
            difference = this_year_birthday - datetime.now()

        print(f'{name} should wait {difference.days} days until next birthday!')

    def add_email(self, name, email):

        if add_book.data[name].record_dict['Email']:
            add_book.data[name].record_dict['Email'].append(email)
        else:
            add_book.data[name].record_dict['Email'] = []
            add_book.data[name].record_dict['Email'].append(email)

    def add_adress(self, name, adress):
        add_book.data[name].record_dict['Adress'] = adress

class TelDoesNotMathFormatError(Exception):
    status = 0

class BirthdayDoesNotMathFormatError(Exception):
    status = 0

class NameDoesNotExistError(Exception):
    status = 0

class TryAgainError(Exception):
    status = 0


class Presenter(ABC):

    @abstractmethod
    def see_iteration():
        pass

    @abstractmethod
    def show_all():
        pass


class PresenterRecords(Presenter): 

    def see_iteration(self, n):
        try:
            global x
            global page

            if len(add_book.data) - (x + 1) >= 0:
                print(f'Page #: {page}. ')
            else:
                print('Stop listing!')
            record_generator = add_book.iterator()
            for x in range(x, x + int(n)):
                next(record_generator)

        except IndexError:

            print(f"Sorry, no more records! Use 'show all' command!")

    def show_all(self):
        global x
        global page

        if len(add_book.data) == 0:
            print('Data Base is empty yet. Please add someone!')
        else:
            print('Data Base contains next contacts:')

            x = 0
            page = 1

            for key, value in add_book.data.items():

                for key_in, value_in in value.record_dict.items():

                    if value_in:
                        if isinstance(value_in, list):
                            print(
                                f"{key_in} : {', '.join(map(str, value_in))} | ", end=" ")
                        else:
                            print(f"{key_in} : {value_in} | ", end=" ")
                print('')


class PresenterNotes(Presenter):

    def see_iteration(self, n):
        pass

    def show_all(self):
        print('')
        print('EXISTED NOTES:')
        for key, value in add_book.notes_data.items():
            print(f"Tag: {key} | Note: {value}  ")

            print('')


def command_parser(command):  # command`s parser
    command_id = ''
    name = ''
    phone = ''

    parsered_list = command.split(" ")

    if len(parsered_list) == 1:
        command_id = parsered_list[0].lower()  # make all letters small

    elif len(parsered_list) == 2:
        command_id = parsered_list[0].lower()
        name = parsered_list[1]
    elif len(parsered_list) == 3:
        command_id = parsered_list[0].lower()
        name = parsered_list[1]
        phone = parsered_list[2]
    elif len(parsered_list) > 3:
        command_id = parsered_list[0].lower()
        name = parsered_list[1]
        slice_parser = parsered_list[2:]
        phone = ' '.join(map(str, slice_parser))
        # phone = parsered_list[2]
    else:
        print("Number of arguments do not fit to reqirements. Please try again!")

    return command_id, name, phone



# Decorator
def input_error(func):  # decorator

    def inner(*args, **kwargs):

        func(*args, **kwargs)

        if TelDoesNotMathFormatError.status == 1:  # added functional zone
            print('Format does not match')
            TelDoesNotMathFormatError.status = 0
        elif NameDoesNotExistError.status == 1:
            print('Enter user name please')
            NameDoesNotExistError.status = 0
        elif TryAgainError.status == 1:
            print('Please, Try again!')
            TryAgainError.status = 0
        elif BirthdayDoesNotMathFormatError.status == 1:
            print('Please, Try again!')
            BirthdayDoesNotMathFormatError.status = 0

    return inner

# Handlers:
def hello_func():
    print('How can I help you?')

@input_error
def add_func(name, phone):  # 1&2

    try:
        if re.match(r"^[0-9]{10,10}$", phone):

            add_book.add_record(name, phone)  # 2

            print('Information has been added successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:

        print("Telephone number does not match format - should be 10 digits")
        TelDoesNotMathFormatError.status = 1

@input_error
def change_func(name, phone):  # 1&2

    try:
        if name in add_book.data:
            if re.match(r"^[0-9]{10,10}$", phone):

                Record().edit_phone(name, phone)  # 2

                print('Phone number has been changed successfully!')
            else:
                raise TelDoesNotMathFormatError

        else:
            raise NameDoesNotExistError

    except TelDoesNotMathFormatError:

        print("Telephone number does not match format - should be 10 digits")
        TelDoesNotMathFormatError.status = 1

    except NameDoesNotExistError:

        print('Name does not exist')
        NameDoesNotExistError.status = 1

@input_error
def phone_func(name):  # 1&2

    try:

        if name in add_book.data:  # 2

            mystring = ', '.join(
                map(str, add_book.data[name].record_dict['Phone']))

            print(f'Phone number assigned for requested name is: {mystring}')

        else:
            raise NameDoesNotExistError

    except NameDoesNotExistError:

        print('Name does not exist.')  # - decorator
        NameDoesNotExistError.status = 1

def show_func():

    add_book.presenter.show_all()
    Notes().presenter.show_all()

@input_error
def see_func(n):


    add_book.presenter.see_iteration(n)





@input_error
def addnum_func(name, phone):  # 1&2

    try:
        if re.match(r"^[0-9]{10,10}$", phone):

            Record().add_phone(name, phone)  # 2

            print('Information has been added successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:

        print("Telephone number does not match format - should be 10 digits")
        TelDoesNotMathFormatError.status = 1

@input_error
def del_func(name, phone):  # 1&2

    try:
        if re.match(r"^[0-9]{10,10}$", phone):

            Record().del_phone(name, phone)  # 2

            print('Telephone number has been deleted successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:

        print("Telephone number does not match format - should be 10 digits")
        TelDoesNotMathFormatError.status = 1

    except ValueError:
        print("Number assigned for deletion does not exist!")
        TryAgainError.status = 1

@input_error
def birth_func(name, birthday):  # 1&2

    add_book.data[name].record_dict['Birthday'] = Birthday(birthday).value

@input_error
def nextbirth_func(name):  # 1&2

    try:

        Record().days_to_birthday(name)  # 2

    except KeyError:
        print("This contact does not exist! First - set up appropriate contact")
        TryAgainError.status = 1

    except AttributeError:
        print("You have to add your birthday before this operation!")
        TryAgainError.status = 1

def help_func():
    print(' Bot undestands next commands:\n'
          '- "hello" - answear: "How can I help you?"\n'
          '- "add" name telephone number" - save new contact\n'
          '- "change" name telephone number" - save new telephone number for existed contact\n'
          '- "phone" name" - show telephone number\n'
          '- "show all" - show all contacts (name telephone number)\n'
          '- "see" n" - show n records (you could use this command several times)\n'
          '- "addnum" name telephone number" - add aditional tel number for certain contact\n'
          '- "del" name telephone number" - del tel number for certain contact\n'
          '- "addbirth" name birthday - add date of birthday in data format\n'
          '- "nextbirth" name - show how many days left up to next birthday\n'
          '- "help" - bot show commands explanations\n'
          '- "save" name - save data base in file: name (without extention) \n'
          '- "load name" - load data base from file (without extention) \n'
          '- "lookup" text" - find text in records (no difference which case of characters)\n'
          '- "delrec" name" - delete record from AddressBook \n'
          '- "addemail" name email" - add email to record \n'
          '- "changeemail" name new_email" - change all emails on new one \n'
          '- "addnotes" name text" - add notes to record \n'
          '- "addadress" name text" - add adress to record \n'
          '- "findtag" teg_text" - looking up notes by tages \n'
          '- "delnotes" teg_text" - del notes by tages \n'
          '- "changenotes" teg_text" - change notes by tages \n'
          '- "sortnotes" teg_text" - sorting up notes by tages \n'
          '- "guess" - switch on off guess mode ---> analizing taping and try to guess command \n'
          '- "checkbirth" days_number - display list of contacts, who have birthday in x days \n'
          '- "good bye" or "close" or "exit" - bot stops work and messege "Good bye!" ')

def save_func(name):

    with open(name + '.obj', 'wb') as report:
        pickle.dump(add_book.data, report)

    with open(name + '.txt', 'w') as report:

        for key, value in add_book.data.items():

            for key_in, value_in in value.record_dict.items():

                if value_in:
                    if isinstance(value_in, list):
                        report.write(
                            f"{key_in} : {', '.join(map(str, value_in))} | ")
                    else:
                        report.write(f"{key_in} : { value_in} | ")
            report.write('\n')
        
        print('Data base has been saved successfully!')

def load_func(name):
    try:
        add_book.add_record('load', '0000000000')
        add_book.add_notes('load', '0000000000')
        
        with open(name + '.obj', 'rb') as report:
            add_book.data = pickle.load(report)
            
        with open('notes.csv', newline='') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                add_book.notes_data[row['tag']] = row['note']
                
            print('Data base has been loaded successfully!')

    except FileNotFoundError:
        print(
            "File not found! Please, make sure file is exist or name was written correctly!")

def lookup_func(text):
    if len(add_book.data) == 0:
        print('Data Base is empty yet. Please add someone!')
    else:
        flag_found = 0
        for key, value in add_book.data.items():
            dict_for_lookup = deepcopy(value.record_dict)
            if value.record_dict['Birthday']:
                datetimestring = copy(value.record_dict['Birthday'])
                dict_for_lookup['Birthday'] = datetimestring.strftime(
                    '%A %d %B %Y')
            else:
                dict_for_lookup['Birthday'] = ''

            dict_for_lookup['Phone'] = list_string(value.record_dict['Phone'])

            dict_for_lookup['Email'] = list_string(value.record_dict['Email'])
            dict_for_lookup['Adress'] = list_string(
                value.record_dict['Adress'])

            for key_in, value_in in dict_for_lookup.items():
                if value_in.lower().find(text.lower()) >= 0:
                    print(
                        f'Looked up text was found in "{key}" Record, in "{key_in}" Field. in next text: "{value_in}" ')
                    flag_found += 1

    # Add lookup by Notes
    if len(add_book.notes_data) == 0:
        print('There is not any notes yet. Please add something!')
    else:
        for key, value in add_book.notes_data.items():
            if key.lower().find(text.lower()) >= 0:
                print(f'Looked up text was found in tag :"{key}" for next Note: "{value}"')
                flag_found += 1
            if value.lower().find(text.lower()) >= 0:
                print(f'Looked up text was found in Notes :"{value}" with next tags: "{key}"')
                flag_found += 1
             
    if flag_found != 0:
        print(f'Summary: There were found {flag_found} results')
    else:
        print('No information was found')
        
@input_error
def del_record_hand(name):  # ---- !!!!!
    try:

        if name in add_book.data:

            add_book.del_record(name)

            print(f'Record :{name} has been deleted successfully!')

        else:
            raise NameDoesNotExistError

    except NameDoesNotExistError:

        print('Record does not exist.')
        NameDoesNotExistError.status = 1

@input_error
def add_email_head(name, email):

    try:
        if re.match(r"[a-z0-9]+@[a-z]+\.[a-z]{2,3}", email):

            Record().add_email(name, email)  # 2

            print('Email has been added successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:

        print("Email does not match format - should be 1@1.1")
        TelDoesNotMathFormatError.status = 1

@input_error
def change_email_head(name, email):

    try:
        if re.match(r"[a-z0-9]+@[a-z]+\.[a-z]{2,3}", email):

            Email().change_email(name, email)  # 2

            print('Email has been changed successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:

        print("Email does not match format - should be 1@1.1")
        TelDoesNotMathFormatError.status = 1

@input_error
def add_adress_head(name, adress):
    try:
        Record().add_adress(name, adress)  # 2
        print('Adress has been added successfully!')

    except:

        print("Adress format problem")

def add_notes_head(name, phone):  # name=tag phone=note
    tag = add_book.add_notes(name, phone)
    print(f"Note with tag {tag} added")


def find_notes_by_tages_head(name):  # name=tag
    add_book.find_notes_by_tages(name)


def sort_notes_by_tages_head():
    add_book.sort_notes_by_tages()


def del_notes_by_tages_head(name):  # name=tag
    try:
        Notes().del_notes(name)
    except KeyError:
        print(f"Tag {name} not found")

def change_notes_by_tages_head(name, phone):  # name=tag phone=note
    try:
        Notes().change_notes(name, phone)
    except KeyError:
        print(f"Tag {name} not found")

@input_error
def sort_files(path):
    main_sort_files (Path(path).resolve())
    print('Files have been sorted successfully!')


def guess_command():
    pass

@input_error
def birthday_in_days_hand(number_days):
    try:
        add_book.birthday_in_days(number_days)

    except AttributeError:

        print ('It seems you do not added birthday yet for that contact!')


def list_string(list):  # servise function for lookup function
    if list is List:
        return ', '.join(map(str, list))
    else:
        return str(list)


def good_buy_func():
    print('Good bye!')
    return 'stop'

# ENDLESS TYPING
#def on_press(key):
    
    
#    global main_list_guess
#    global join_command_list
    
#    try:
#        if key == keyboard.Key.esc:
        
        # Stop listener
#            return False

#        elif key == keyboard.Key.enter:
            #print('')
            #print(''.join(map(str, main_list_guess)), end='\r', flush=True)
#            return False

            

#        elif key == keyboard.Key.shift:
#            pass

#        elif key == keyboard.Key.space:
#            main_list_guess.append(' ')

#        elif key == keyboard.Key.backspace:

#            if len(main_list_guess) >= 0:
#                main_list_guess.pop()
#                print('                                                                                     ', end='\r')
#                print(''.join(map(str, main_list_guess)), end='\r', flush=True)

#        else:
#            main_list_guess.append(key.char)
#            for command in command_list:
                                              
#                if len(main_list_guess) == 1 and command[0] == main_list_guess[0]:
#            
#                    join_command_list.append(command)

#                elif len(main_list_guess) == 2 and command[0] == main_list_guess[0] and command[1] == main_list_guess[1]:

#                    join_command_list.append(command)

#                elif len(main_list_guess) == 3 and command[0] == main_list_guess[0] and command[1] == main_list_guess[1] and command[2] == main_list_guess[2]:

#                    join_command_list.append(command)

#                elif len(main_list_guess) == 4 and command[0] == main_list_guess[0] and command[1] == main_list_guess[1] and command[2] == main_list_guess[2] and command[3] == main_list_guess[3]:

#                    join_command_list.append(command)

#            print('                                                                                    ', end='\r')
#            print(''.join(map(str, main_list_guess)), end='\r\t\t\t\t', flush=True)
#            print(', '.join(map(str, join_command_list)), end='\r', flush=True)
#            join_command_list.clear()

#    except AttributeError:
#        print('special key {0} pressed'.format(
#            key))

#    except IndexError:
#        print('', end='')

def main_guess(command_list):
    pass 
    	

    
#    global main_list_guess
#    global join_command_list
   
#    main_list_guess = []
#    join_command_list = []


    # Collect events until released
#    with keyboard.Listener(on_press=on_press) as listener:   #on_release=on_release
#        listener.join()
        
    # ...or, in a non-blocking fashion:
#    listener = keyboard.Listener(on_press=on_press)   #on_release=on_release
#    listener.start()
#    listener.stop()

#    return ''.join(map(str, main_list_guess))


# SORT FILES

### NORMILIZE
CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def normalize(name: str):
    t_name = name.translate(TRANS)
    t_name = re.sub(r'\W', '_', t_name)
    return t_name

### FILES PARSER
JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
MY_OTHER = []
ARCHIVES = []

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'ZIP': ARCHIVES
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()

def get_extension(filename: str):
    return Path(filename).suffix[1:].upper()


def scan(folder: Path) :
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue

        ext = get_extension(item.name)  
        fullname = folder / item.name  
        if not ext: 
            MY_OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                MY_OTHER.append(fullname)







def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / normalize(filename.name))


def handle_archive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(filename.name.replace(filename.suffix, ''))

    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'This is not archive {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Error deleted {folder}')


def main_sort_files(folder: Path):
    scan(folder)
    for file in JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')
    for file in MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')

    for file in MY_OTHER:
        handle_other(file, folder / 'MY_OTHER')
    for file in ARCHIVES:
        handle_archive(file, folder / 'archives')

    for folder in FOLDERS[::-1]:
        handle_folder(folder)

# MAIN BODY FUNCTION


def main():

    global add_book
    add_book = AddressBook()
    
    ### Reading existed notes
    if(os.path.exists('notes.csv') and os.path.isfile('notes.csv')):
            with open('notes.csv', newline='') as fh:
                reader = csv.DictReader(fh)
                for row in reader:
                    add_book.notes_data[row['tag']] = row['note']


    commands_dict = {'hello': hello_func, 'add': add_func, 'change': change_func,
                     'phone': phone_func, 'show': show_func, 'good': good_buy_func,
                     'close': good_buy_func, 'exit': good_buy_func, 'addnum': addnum_func, 'del': del_func,
                     'addbirth': birth_func, 'nextbirth': nextbirth_func, 'see': see_func, 'help': help_func,
                     'save': save_func, 'load': load_func, 'lookup': lookup_func,

                     'delrec': del_record_hand, 'addemail': add_email_head, 'addnotes': add_notes_head,
                     'addadress': add_adress_head, 'findtag': find_notes_by_tages_head, 'sortnotes': sort_notes_by_tages_head,
                     'sortfiles': sort_files, 'guess': guess_command, 'checkbirth': birthday_in_days_hand,
                     'changeemail': change_email_head, 'delnotes': del_notes_by_tages_head, 'changenotes': change_notes_by_tages_head
                     }

    stop_flag = ''

    print("Bot has been started!\nFor additional information enter 'help'")
    while True:
        try:

            print('')
            command = input("Please, put you command in Command line! (from 1 to 3 arguments): ")   
#            if command == 'guess':
#               for key in  commands_dict:
#                    command_list.append(key)           
                
#                main_guess(command_list)  
            
            command_id, name, phone = command_parser(command)  # passing vars to another func
            for key, value in commands_dict.items():
                if command_id == key and name == '' and phone == '':
                    res = value()
                    stop_flag = res

                elif command_id == key and name.lower() == 'bay' and phone == '':
                    res = value()
                    stop_flag = res

                elif command_id == key and name.lower() == 'all' and phone == '':
                    res = value()

                elif command_id == key and name != '' and phone == '':
                    res = value(name)

                elif command_id == key and name != '' and phone != '':
                    res = value(name, phone)

            if command_id not in commands_dict:
                print('I do not know this command!')

            if stop_flag == 'stop':
                break

        except TypeError:
            print('Unsuccessful operation. Please, try again')
            
        except EOFError as e:
            print(e)


if __name__ == '__main__':
    main()
