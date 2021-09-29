def factors(n):
    factorlist = []
    for f in range(1, n + 1):
        if n % f == 0:
            factorlist.append(f)
    return factorlist
 
for value in [3, 12, 49, 100, -1]:
    print(value, "\t", factors(value))
