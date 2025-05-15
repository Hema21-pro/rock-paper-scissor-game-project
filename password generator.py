import random
big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_letters = "abcdefghijklnopqrstuvwxyz"
symbol = "@#_&();!{}[]"
number = "0123456789"
all = big_letters+small_letters+symbol+number
length = 10
password = ''.join(random.sample(all,length))
print("the generated password is:",password)