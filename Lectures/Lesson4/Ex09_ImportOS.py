# Модуль os - это множество функция для работы с операционной системы (не зависит от ОС)
# Базовые функции модуля OS:
1. # Cмена текущей директории - os.chdir(path)
# import os
# os.chdir('C:/Users/79190/PycharmProjects/GB')
2. # Получить путь к рабочей директории - os.getcwd()
import os
print(os.getcwd())
3. # Базовое имя пути - os.path.basename(path)
print(os.path.basename('C:/WORK/STUDY/GeekBreans/Python'))
4. # Возвращение нормализованного абсолютного пути - os.path.abspath(path)
print(os.path.abspath('Python'))
5. # 