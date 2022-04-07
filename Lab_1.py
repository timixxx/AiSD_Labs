#----------task 1
print("Выберите тип множества для ввода (1 - числа, 2 - слова)")
type = int(input())

print("Введите элементы множества:")
a = set(input().split())
leng = 0
for num in a:
    leng += 1

def printsetnums (rset):
    print("Числовое множество:", *sorted(rset, key=int), "Длина множества:",leng)

def printset (rset):
    print("Буквенное множество:", rset, "Длина множества:",leng)
if type == 1:
    printsetnums(a)
elif type == 2:
    printset(a)
#-----------task 2
print("Введите два предложения для поиска общих слов:")
s3 = set()
s1 = set(input().split())
s2 = set(input().split())
for word1 in s1:
    for word2 in s2:
        if word1 == word2:
            s3.add(word1)

print(s3)

#----------task 3
print("Введите последовательность символов для разбиения на множества:")

eng = set('abcdefghijklmnopqrstuvwxyz')
rus = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
nums = set('1234567890')

S = set(input().lower())

print("Множество A:", S & rus)
print("Множество B", S & eng)
print("Множество C:", S & nums)