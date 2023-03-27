import os
# os.chdir('c:/WORK/STUDY/GeekBreans/Python/HomeWork/lesson8') 
version = "v.1.3"
markup = "=" * 40
markup2 = "-" * 40


def welcome():
    print("=== PhoneBook", version, "===")
    print(markup)


def menu():
    print("Режимы работы: \n"
          "1. Вывести телефонный справочник на экран \n"
          "2. Добавить запись \n"
          "3. Редактировать запись \n"
          "4. Удалить запись \n"
          "5. Сохранить в файл \n"
          "0. БАН (Закрыть программу)")
    print(markup)

def menu2():
    print("Редактировать запись: \n"
          "1. По фамилии \n"
          "2. По телефону")
    print(markup2)


def show(phone_book):
    os.chdir('C:\WORK\STUDY\GeekBrains\Python\HomeWork\lesson8') 
    # os.system('cls')
    print("=== Телефонный справочник ===")
    open('PhoneBook.csv', 'a', encoding='utf-8')
    for tel in phone_book:
        value = phone_book[tel]
        temp = value[0] + " " + value[1] + " " + value[2] + ", " + value[3]
        print(tel, ':', temp)
        print(markup)
    


def input_data():
    temp = []

    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    second_name = input("Введите отчество: ")
    address = input("Введите адрес: ")
    temp.append(last_name)
    temp.append(first_name)
    temp.append(second_name)
    temp.append(address)
    return temp


def input_record(phone_book):
    tel = input("Введите номер телефона: ")
    # for i in tel:
    #     if i not in '+()0123456789 ':
    #         tel = input(f'Номер введен не верно (символ ({i})). Повторите ввод: ')
    if tel in phone_book:
        print("Такой номер уже существует")
    else:
        value = input_data()
        phone_book[tel] = value
        print("### Запись успешно добавлена ###")


def edit_record(phone_book):
    menu2()
    choice = int(input("Ваш выбор: "))
    if choice == 1:
        fio = input("Введите Фамилию: ")
        if tel in phone_book:
            temp = input_data()
            phone_book[tel] = temp
        else:
            print("Введенного номера не существует")
    if choice == 2:
        tel = input("Введите номер телефона: ")
        if tel in phone_book:
            temp = input_data()
            phone_book[tel] = temp
        else:
            print("Введенного номера не существует")


def delete_record():
    os.chdir('C:\WORK\STUDY\GeekBrains\Python\HomeWork\lesson8')
    data = open('PhoneBook.csv', 'r+', encoding = 'utf-8')
    tel = input("Введите номер телефона для удаления: ")
    phone_book = {k for i in data for k, v in data.items() if i in v}
    print(phone_book)
    # for var in data:
    #     if tel in var:
    #         del phone_book[tel]
    #     print(f"### Запись {tel} удалена ###")
    # else:
    #     print("Введенного номера не существует")


def export_to_file(phone_book):
    os.chdir('C:\WORK\STUDY\GeekBrains\Python\HomeWork\lesson8')
    with open('PhoneBook.csv', 'a', encoding='utf-8') as file:
        for tel in phone_book:
            value = phone_book[tel]
            file.write(tel + ";" +
                       value[0] +";" +
                       value[1] + ";" +
                       value[2] + ";" +
                       value[3] + "\n")