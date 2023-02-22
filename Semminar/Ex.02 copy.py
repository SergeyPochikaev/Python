n = str(float(input("Введите число: ")))
for i in range(len(n)):
  if n[i] == '.':
     print(n[i+1])