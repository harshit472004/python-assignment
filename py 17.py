import random
li = ['r','s','p']
a = random.choice(li)
while True:
  u = input("Your Choice:")
  if a == 'r':
    if u == "p":
       print("You won")
    elif u == "s":
      print('computer Won')
    elif u == 'r':
      print("Tied")
    else:
      print("Enter Valid Data")
  if a == 's':
    if u == "r":
      print("You won")
    elif u == "p":
      print('computer Won')
    elif u == 's':
      print("Tied")
    else:
      print("Enter Valid Data")
  if a == 'p':
    if u == "s":
      print("You won")
    elif u == "r":
      print('computer Won')
    elif u == 'p':
      print("Tied")
    else:
      print("Enter Valid Data")
  y = input("Enter to play more or e for Exit:")
  if y == "":
    continue
  elif y == "e":
    break
