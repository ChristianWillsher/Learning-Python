def bubblesort(values):
  print("...sorting...")
  n = len(values)
  swapped = True
  while swapped == True:
    swapped = False
    for i in range(1,n):
      if values[i-1] > values[i]:
        temp = values [i]
        values[i] = values[i - 1]
        values[i-1] = temp
        swapped = True


# test program
values = [6, 2, 8, 4, 5, 1, 9, 3, 7]

print("Unsorted:", values)

bubblesort(values)

print("Sorted:  ", values)