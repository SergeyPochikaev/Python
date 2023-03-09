# Создать телефонный справочник с возможностью импорта и экспорта данных вформате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1.  # Программа должна выводить данные
2.  # Программа должна сохранять данные в текстовом файле
3.  # Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
4.  # Использование функций. Ваша программа не должна быть линейной

# def search():
# data = open('Phonebook.csv', 'r', encoding = 'utf-8')
# flag = 1
# name = input('Введите данные для поиска: ')
# for line in data:
# if name in line:
# flag = 0
# print(line)
# if flag: print('no name given')
# print(search())


def поиск():
    data = open('Phonebook.csv', 'r', encoding='utf-8')
    flag = 1
    count = 0
    list1 = []
    name = input('Введите данные для поиска: ')
    for line in data:
        count += 1
        if name in line:
            flag = 0
            print(line)
            print(count)
            return count
    return


data = open('Phonebook.csv', 'r', encoding='utf-8')
list1 = []
for line in data:
    list1.append(line)
print(list1)

res = поиск()
print(res)
list2 = []

for i in range(len(list1)):
    if i != res:
        list2.append(list1[i])
print(list2)

with open('Phonebook.csv', 'w', encoding='utf-8') as data:
  # data.write(f'| Фамилия | Имя | Отчество | Номер телефона | Описание |\n')
    for i in range(len(list2)):
        data.write(list2[i])
    data.close()
