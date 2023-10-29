from collections import UserDict

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "The number must consist of 10 digits."
    return inner

def record_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "This number is not in the list"
    return inner

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

@input_error
class Phone(Field):
    def __init__(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError
        super().__init__(value)

@record_error
class Record:
    def __init__(self, name, old_phones = []):
        self.name = str(Name(name))
        self.phones = []
        self.old_phones = old_phones

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(self.phones)}"
        
    def add_phone(self, phone):
        self.phones.append(str(Phone(phone)))

    def edit_phone(self, old_phone, new_phone):
        self.phones = self.old_phones
        print(f"old_phone {old_phone}")
        print(f"new_phone {new_phone}")
        i = 0
        for num in self.phones:
            (print(num))
            if num == old_phone:
                self.phones[i] = new_phone
            i +=1
        print(f"self.phones {self.phones}")

    def find_phone(self, s_phone):
        for phone in self.phones:
            if phone == s_phone:
                return phone
        return "There is no such phone"
    
    def remove_phone(self, s_phone):
        self.phones.remove(s_phone)
        

class AddressBook(UserDict):
    def add_record(self, record):
        self[record.name] = record.phones

    def find(self, s_name):
        for name, phones in self.items():
            if name == s_name:
                return Record(name, phones)
            else:
                return "There is no such record"

    def delete(self, name):
            del self[name]