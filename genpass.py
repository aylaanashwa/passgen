import random

chars = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""

for i in range(10):
    password += random.choice(chars)
    # password = password + random.choice(chars)
print(password)
