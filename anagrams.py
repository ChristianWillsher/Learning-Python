def anagram(s1, s2):
    list1 = []
    for letter in s1:
        list1.append(letter)
    list2 = []
    for letter in s2:
        list2.append(letter)
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
for pair in [["listen", "silent"], ["aab", "bba"], ["bob", "bob"], ["bob", "alice"], ["innn", "rain"], ["brain", "rain"]]:
    print(pair, anagram(pair[0],pair[1]))
 

