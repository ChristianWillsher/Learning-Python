def insertionsort(values):
  print("...sorting...")
  for i in range(1, len(values)): 
        key = values[i] 
        Q = i-1
        while Q >=0 and key < values[Q] : 
                values[Q+1] = values[Q] 
                Q -= 1
        values[Q+1] = key 

# test program
values = [4, 7, 2, 9, 5, 1, 8, 6, 3]

print("Unsorted:", values)

insertionsort(values)

print("Sorted:  ", values)
