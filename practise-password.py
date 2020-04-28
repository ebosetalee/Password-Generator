import random
a = [1,2,3]
b =["a","b","c"]

for x in a:
  print(x)
  for y in b:
    print(y)

for x in range(len(a)):
  print(a[x],b[x])


alpha = "abcdefghijklmnopqrstuvwxyz"
capAlpha = str.swapcase(alpha)
numerals = [x for x in range(0, 10)]
symbols = "!", "@", "#", "%", "'", "^", "&",
"*", "(", ")", "-", "_", "+", "{", "}", "[", "]",
",", ".", ":", ";", "=", '"'
symbols = list(symbols)
print(random.choice(symbols))
print(random.choice(numerals))
print(alpha)
print(capAlpha)
print(random.choice(capAlpha))

# a = random.sample(range(len(alpha)), 10)
# print(a)

Num_of_password = int(input("What length of Password do you need? "))
# symbs = input("Do you want Symbols such as @, &, *, [ etc: ")
# numbers = input("Do you want Numbers such as 1, 2, 3, 9 etc: ")
strength = input("Do you want the password to be weak or strong? ")

password = []
count = 0
while count <= Num_of_password:
  list(alpha)
  password == random.choice(capAlpha)
  count += 1
  if strength == "strong" or "Strong":
    # password.append(random.choice(alpha))
    # password.append(random.choice(capAlpha))
    # password.append(random.choice((numerals)))
    # password.append(random.choice(alpha))
    # password.append(random.choice(symbols))
    strong_password = random.choice(alpha) + random.choice(
        capAlpha) + random.choice(str(numerals)) + random.choice(str(symbols))
    # print(random.choice(strong_password + str(password)))
    print(strong_password)
    count += 4
  elif strength == "weak" or "Weak":
    numbers = input("Do you want Numbers such as 1, 2, 3, 9 etc: ")
    # symbs = input("Do you want Symbols such as @, &, *, [ etc: ")
    if numbers == "yes" or "Yes":
      # second = password.append(random.choice(numbers))
      # if symbs == "no" or "No":
      weak_password = numerals + capAlpha

  # elif numbers == "yes" or "yes":
  # print(password)
  # count += 3
# password = x.rstrip(",")for x in password
# print(password)
# password = str(password)
# print(password)
# print(x.rstrip("'")for x in password)
