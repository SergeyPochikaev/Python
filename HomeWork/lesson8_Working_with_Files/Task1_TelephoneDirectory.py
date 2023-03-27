# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и
# Вы должны реализовать функционал для изменения и удаления данных

import os
os.chdir('c:\WORK\STUDY\GeekBrains\Python\HomeWork\lesson8_Working_with_Files') # Смена текущей директории
# Примеры использования различных режимов в коде (например: а):

data = open('PhoneBook.txt', 'a', encoding='utf-8')
data.write('Фамилия: \n')
data.write('Имя: \n')
data.write('Номер телефона: \n')
data.write('Комментарий: \n')
data.close()


