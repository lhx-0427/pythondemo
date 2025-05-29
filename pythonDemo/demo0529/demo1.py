#字符串的定义： 有0个或者有限个字符组成的序列
#转义字符 \
print("\n")#表示换行
print("\\n")#输出\和n这2个字符
#我们可以使用+运算符来实现字符串的拼接，可以使用*运算符来重复一个字符串的内容，
# 可以使用in和not in来判断一个字符串是否包含另外一个字符串，我们也可以用[]和[:]运算符从字符串取出某个字符或某些字符。
s1="hello"+","+"world"
print(s1)
s2="!"*3
print(s2)
#字符串的比较
#先比第一个字符  如果一样 就一直往下比字符
s1 = 'hello, world!'
# 字符串首字母大写
print(s1.capitalize())  # Hello, world!
# 字符串每个单词首字母大写
print(s1.title())       # Hello, World!
# 字符串变大写
print(s1.upper())       # HELLO, WORLD!
s2 = 'GOODBYE'
# 字符串变小写
print(s2.lower())       # goodbye
# 检查s1和s2的值
print(s1)               # hello, world
print(s2)               # GOODBYE
#查找
s = 'hello world!'
print(s.find('o'))       # 4
print(s.rfind('o'))      # 7
print(s.rindex('o'))     # 7
# print(s.rindex('o', 8))  # ValueError: substring not found
#判断 性质
s1 = 'hello, world!'
print(s1.startswith('He'))   # False
print(s1.startswith('hel'))  # True
print(s1.endswith('!'))      # True
s2 = 'abc123456'
print(s2.isdigit())  # False
print(s2.isalpha())  # False
print(s2.isalnum())  # True
#上面的isdigit用来判断字符串是不是完全由数字构成的，isalpha用来判断字符串是不是完全由字母构成的
# 这里的字母指的是 Unicode 字符但不包含 Emoji 字符，isalnum用来判断字符串是不是由字母和数字构成的。