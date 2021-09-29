number = int(600851475143)
count = 2
while number != 1:
    if number % count == 0:
        print(count)
        number = number / count
        count = 2
    else:
        count = count + 1
