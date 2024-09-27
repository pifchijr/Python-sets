Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
text1 = "The quick brown fox jumps over the lazy dog"
text2 = "The slow turtle jumps under the energetic dog"
print((set(text1.split())) ^ (set(text2.split())))
print((set(text1.split())) & (set(text2.split())))