vowel_letters = 'аиеёоуыэюя'
unevirsalWord = list(input('Введите стих : ').lower().split())
text = []
for i in range(len(unevirsalWord)):
    for j in unevirsalWord[i]:
        x = text.append(list(filter(lambda x: x == j, vowel_letters)))
print(text)

# for i in range(len(unevirsalWord)):
#     f=''
#     for j in unevirsalWord[i]:
#         f+= j if j in vowel_letters else ''
#     s[i]=f
# print(s)