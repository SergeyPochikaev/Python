# Функция с возращением нескольких аргументов
def sumNumbers(n, y = 'Hello'):
  print(y)
  summa = 0
  for i in range(1, n + 1):
    summa += i
  return summa
print(sumNumbers(5))
# другая форма записи
def sumNumbers(n, y = 'Hello'):
  print(y)
  summa = 0
  for i in range(1, n + 1):
    summa += i
  return summa
a = sumNumbers(5, 'qwert')
print(a)

# принятия множества аргументов
def sum_str(*args):
  res = ''
  for i in args:
    res += i
  return res

print(sum_str('q','e','t'))
print(sum_str('q','e','t','r','f'))
print(sum_str(str(1),str(2),str(3)))