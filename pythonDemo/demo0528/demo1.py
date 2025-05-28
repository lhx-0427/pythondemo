#通过内置函数type()可以获取变量的类型
a=97
print(type(a))
b=9.09
print(type(b))
c="hello world"
print(type(c))
d=True
print(type(d))

#通过一些内置的函数来实现变量的类型转换
print(float(a))#int ->float  可以指定进制
print(int(b))#float ->int
print(str(a))#int ->str   可以指定编码格式
print(chr(a))#int ->chr
print(ord('a'))#chr ->int  （将一个字符转成对于ascll码值）
#使用变量来保存数据，变量有不同的类型，常用的类型有int、float、str和bool。在有需要的情况下，可以通过 Python 内置的函数对变量进行类型转换