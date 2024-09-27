Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l = []
n = int(input())
for i in range(n):
  a = int(input())
  l.append(a)
l = list(set(l))
print(str(l))