# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

numTicket = int(input("Ввуедите номер билета "))
firstTroika = int(numTicket/1000)
secondTroika = int(numTicket%1000)
n1 = firstTroika//100
n2 = (firstTroika - n1*100) //10
n3 = firstTroika % 10
sum1 = n1 + n2 + n3
n4 = secondTroika//100
n5 = (secondTroika - n4*100) //10
n6 = secondTroika % 10
sum2 = n4 + n5 + n6
# print(firstTroika)
# print(secondTroika)
# print(sum1, sum2)
if (sum1 == sum2) :
    print('yes')
else :
    print('no')