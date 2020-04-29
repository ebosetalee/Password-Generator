import random

alpha = "abcdefghijklmnopqrstuvwxyz"
capAlpha = str.swapcase(alpha)
numerals = "0123456789"
# print(numerals)
symbols = """!@#%'^&*()-_{+}[],.:;"="""
characters = alpha + capAlpha + numerals + symbols
# print(characters)

Num_of_password = int(input("What length of Password do you need? "))
# symbs = input("Do you want Symbols such as @, &, *, [ etc: ")
# numbers = input("Do you want Numbers such as 1, 2, 3, 9 etc: ")
strength = input("Do you want the password to be weak or strong? ")
if strength == "weak" or strength == "Weak":
  numbers = input("Do you want Numbers such as 1, 2, 3, 9 etc: ")

password = ""

while len(password) < Num_of_password:
  if strength == "strong" or strength == "Strong":
    password += random.choice(characters)
  elif strength == "weak" or strength == "Weak":
    if numbers == "yes" or numbers == "Yes":
      password += random.choice(alpha + numerals + capAlpha)
    else:
      password += random.choice(capAlpha + alpha)
  else:
    password += random.choice(alpha + capAlpha)
print(password, len(password))  
