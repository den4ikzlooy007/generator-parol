import random

storage = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

a = input('Введите нужную длину пароля: ')
password = ''


for i in range(int(n)):
    element = random.choice(storage)
    password += element

print(password)
