import random
def twodice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2
 
frequencies = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(1000):
    throw = twodice()
    frequencies[throw - 2] += 1
 
print("Throw\tFrequency")
for i in range(11):
    print(str(i + 2), "\t", frequencies[i] / 10, "%", sep="")
