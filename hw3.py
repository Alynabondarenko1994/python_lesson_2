# Задача №3:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

n=float(input('Введите число N:'))
while n<=0 :
     n=float(input('Число должно быть больше 0:' ))
k=0
list=[]
while 2**k<=n:
    list.append(2**k)
    k+=1 
print (f'Целые степени двойки, не превосходящие числа N={n}, следующие:{list}')