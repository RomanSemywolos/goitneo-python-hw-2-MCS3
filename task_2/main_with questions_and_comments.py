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
    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів. 
    def __init__(self, name, old_phones = []):
        self.name = str(Name(name))
        self.phones = []
        self.old_phones = old_phones

    def __str__(self):
        # щоб правильно виводило результат
        return f"Contact name: {self.name}, phones: {'; '.join(self.phones)}"
        
    def add_phone(self, phone):
        # Додавання телефонів.
        self.phones.append(str(Phone(phone)))

    def edit_phone(self, old_phone, new_phone):
        # Редагування телефонів.
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
        # Пошук телефону (не знаю навіщо це).
        for phone in self.phones:
            if phone == s_phone:
                return phone
        return "There is no such phone"
    
    def remove_phone(self, s_phone):
        # Видалення телефону.
        self.phones.remove(s_phone)
        

class AddressBook(UserDict):
        # Додавання записів з підготовлених у Record.
    def add_record(self, record):
        self[record.name] = record.phones

    def find(self, s_name):
        # Пошук записів за іменем, створення об'єкта класу Record.
        for name, phones in self.items():
            if name == s_name:
                return Record(name, phones)
            else:
                return "There is no such record"

    def delete(self, name):
        # Видалення записів за іменем.
            del self[name]


    # Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
print(john_record)
john_record.add_phone("1234567890")
print(john_record)
john_record.add_phone("5555555555")
print(john_record)

print()

# Додавання запису John до адресної книги
book.add_record(john_record)
print(book)

print()

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
print(jane_record)
jane_record.add_phone("9876543210")
print(jane_record)
book.add_record(jane_record)
print(book)

print()

# Виведення всіх записів у книзі (Тобто тільки номерів... У завданні не було прикладу що має вивести консоль,
#                                 але хіба значеннями словника AddressBook мають бути інші словники?)
for name, record in book.data.items():
    print(record)

print()

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)

print()

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555 (Куди мала подітися "{john.name}: "?)

print()

print(book)
# Видалення запису Jane
book.delete("Jane")
print(book)