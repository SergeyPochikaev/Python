# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количство повторов добавляется
# к символом с помощью постфикса формата _n.

chr = 'aaabcaadcdd'
dict = {}
chr_n = []
for i in chr:
    if i in dict:
       chr_n.append(i + '_' + str(dict[i]))
       dict[i] = dict[i] + 1
    else:
        chr_n.append(i)
        dict[i] = 1
print(dict)
print(*chr_n)