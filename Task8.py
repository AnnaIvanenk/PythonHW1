# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать 
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

length = int(input("Введите длину шоколадки: "))
width = int(input("Введите ширину шоколадки: "))
slice = int(input("Сколько долек хотите отломить? "))
if (slice < length*width and (slice%length==0 or slice%width==0)):
    print('Yes')
else:
    print('No')