# Владимир Каменских: Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 
# Output: 1 3 3 3 1

def swapMark(arr):
    max = arr[0]
    min = arr[0]
    for i in range(1, len(arr)):
        if max < arr[i]:
            max = arr[i]
        if min > arr[i]:
            min = arr[i]
    for i in range(len(arr)):
        if arr[i] == max:
            arr[i] = min
    print(arr)
arr = [1, 3, 3, 5, 4, 5, 5,]
swapMark(arr)