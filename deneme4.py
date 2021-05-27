import random as rd 
num = rd.randint(1, 10 )
while True : 
    tahmin =int(input("1 ile 10 arası sayı giriniz : "))
    if tahmin == num :
        print("Doğru Bildiniz -> ", tahmin)
        break 
    else :
        print("Yanlış bildiniz -> ", tahmin)