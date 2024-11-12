import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sifre = ""
uzunluk = int(input("Şifre uzunluğunu girin : "))

for i in range(uzunluk):
    sifre += random.choice(karakterler)

print(sifre)
