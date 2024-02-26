from collections import UserDict, UserList

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
class Name(Field):
    def __init__(self, value):
        if value[0].isupper():
            self.value = value
        else:
            raise ValueError("Incorect Name")
class Phone(Field):
    def __init__(self, value):
        if len(value) == 10:
            self.value = value
        else:
            raise ValueError ("Incorect Phone")

 
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
            
    def remove_phone(self, phone):
        p = self.find_phone(phone)
        self.phones.remove(p)
            
    def edit_phone(self, old_phone, new_phone):
        # self.phones = [Phone(phone) if p != Phone(phone) else p for p in self.phones]
        number = self.find_phone(old_phone)
        if number:
            self.add_phone(new_phone)
            self.remove_phone(old_phone)
        else:
            raise ValueError

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"    

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        for names, record in self.data.items():
            if name in names:
                return self.data[name]
            
    def delete(self, name):
        user = self.find(name)
        del user
    
# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
     
# Створення нової адресної книги
book = AddressBook()

# Додавання запису John до адресної книги               
book.add_record(john_record)
    
    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)


#     # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")   

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

     # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

   # Видалення запису Jane
book.delete("Jane")




