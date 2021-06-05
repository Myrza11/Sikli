'''# первая проблема
lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
    if lang1 == i:
        print('this languages is in list')





# вторая проблема
w = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
d = "php"
i=0
while w[i] != d:
    print(w[i])
    i+=1


text = 'qwerty'
print(text[1])



# третья проблема
a = 7
i=0
while i < 5:
    a = a * 7
    print(a)
    i+=1
        


# четвёртая проблема
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in range(0,6):
    print(i, languages[i])





# пятая проблема
i = -10
for i in range(i,10):
    if i < 10: 
        print(i)
        i+=1





# шестая проблема
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
i = 2
while i < 12:
    print(names[i])
    i+=2







# седьмая проблема
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
i = 1
while i < 12:
    print(names[i])
    i+=2



# восьмая проблема
a = int(input("введите число"))
if a > 99 and a < 1000:
    print("трехзначное число")
else:
    print("не трёхзначное")
if a > 0:
    print("положительное")
else:
    print("отрицательное")
if a % 2 == 0:
    print("четное")
else: 
    print("не чётное")
if a % 31 == 0:
    print("делится на 31 без остатка")
else:
    print("не делится на 31")
if (a > 100) and (a % 17 == 0 and a > 150 and a == 13 ** 2):
    print(a)
    '''
# восьмая проблема
i=-100
while i < 100:
    print(i)
    if (i % 13 == 0) and (i % 2 == 0):
        b = i ** 2
        print(b)
    i+=1        
a=-100
while a < 100:
    if a % 2 == 0:
        print(a)
    a+=7



