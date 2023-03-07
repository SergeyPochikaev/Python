# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в
# его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе
# стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух
# вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и
# “Пам парам”, если с ритмом все не в порядке

def analis(word,letters):
    dic = {}
    for j in range(len(word)):
        count = 0
        for i in word[j]:
            for k in letters:
                if i == k:
                    count += 1
                    dic[j] = count
    return max(dic.values(), key=lambda x: x) == min(dic.values(), key=lambda x: x)

vowel_letters = 'аиеёоуыэюя'
unevirsalWord = list(input('Введите стих : ').lower().split())
# text = []
# for i in range(len(unevirsalWord)):
#     count = 0
#     for j in unevirsalWord[i]:
#         x = text.append(list(filter(lambda x: x == j, vowel_letters)))
# print(text)

if analis(unevirsalWord,vowel_letters):
    print('Парам пам-пам')
else:
    print('Пам парам')
