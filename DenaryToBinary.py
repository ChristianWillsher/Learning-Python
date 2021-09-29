Num = int(input("Please input a denary number"))
binary = []
while Num != 0:
  if Num % 2 == 0:
    Num = Num / 2
    binary.insert(0,0)
  else:
    Num = (Num - 1) / 2
    binary.insert(0,1)

print(binary)
