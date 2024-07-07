from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    def __init__(self, number):
        if len(number) != 10:
            print(f"Number: {number} was too short, should be 10 digits, bye!")
            exit()
        super().__init__(number)

    def __str__(self):
        return str(self.value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def edit_phone(self, old_num, new_num):
        self.phones = book.data[str(self.name)].phones
        for p in self.phones:
            if p.value == old_num:
                id = self.phones.index(p)
                self.phones.pop(id)
                self.phones.insert(id, Phone(new_num))

    def find_phone(self, num: str):
        self.phones = book.data[str(self.name)].phones
        for p in self.phones:
            if p.value == num:
                return num

    def remove_phone(self, phone: str):
        for p in self.phones:
            if p.value == phone:
                id = self.phones.index(p)
                self.phones.pop(id)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, search_name: str):
        for record in book.data.items():
            if search_name == str(record[0]):
                return record[1]

    def delete(self, del_name):
        for name, record in book.data.items():
            if name == del_name:
                return book.pop(name)


# # Створення нової адресної книги
book = AddressBook()

#     # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")


#     # Додавання запису John до адресної книги
book.add_record(john_record)
#
# test line for Record.remove_phone()
john_record.remove_phone("1234567890")


#     # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# #     # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# #     # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
# #
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

#     # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

#     # Видалення запису Jane
book.delete("Jane")
