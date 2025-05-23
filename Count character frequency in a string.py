#Count character frequency in a string
# from collections import Counter
# string1 = "google.com"
# count = Counter(string1)
# print(count)
string = input("Enter string name")
char_count = {}
for char in string:
    if char in char_count:
        char_count[char] +=1 
    else:
        char_count[char] = 1 
print(char_count)
