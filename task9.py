Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
letters = {"e", "t", "a", "s", "r"}
words = ["rat", "star", "art", "set", "rest", "tea"]
lst = []
for i in words:
 if set(i).difference(letters):
    pass
 else:
    lst.append(i)
my_set = set(lst)
print(my_set)