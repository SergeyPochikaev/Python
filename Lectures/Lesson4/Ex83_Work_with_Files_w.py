# Можно добавть кодировкку для записи:
encodin = 'uyf-8'
data = open('Ex81file.txt', 'a', encoding='utf-8')

# Ещё один способ записи данных в файл без процедуры закрывания  с модами "w":
with open('Ex81file.txt', 'w') as data:
 data.write('line 1\n')
 data.write('line 2\n')