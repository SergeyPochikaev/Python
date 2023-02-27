# Функция действия 
def sumNumbers(n):
  summa = 0
  for i in range(1, n + 1):
    summa += i
  print(summa)

# Функция с возращением аргумента
def sumNumbers(n):
  summa = 0
  for i in range(1, n + 1):
    summa += i
  return summa
print(sumNumbers(5))