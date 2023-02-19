import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()[]-_+=\|/"
len = 20

empty = ""
pw = empty.join(random.sample(chars, len))
print(pw)
