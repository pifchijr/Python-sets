Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l1 = []
n = int(input())
for i in range(n):
  a = int(input())
  l1.append(a)
l2 = []
k = int(input())
for i in range(k):
  a = int(input())
  l2.append(a)
l3 = l1 + l2
l3 = list(set(l3))
print(str(l3))