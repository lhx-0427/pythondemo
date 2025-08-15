# l=list(range(100))
# new_l=l[-99]
# print(new_l)

# def trim(s):
#     if len(s)==0:
#         return s
#     while len(s)>0 and s[0]==' ':
#         s=s[1:]
#     while len(s)>0 and s[-1]==' ':
#         s=s[:-1]
#     return s
# # 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')
#迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key,v in d.items():
    print(f"{key}:::{ v}")
b=["a","b","c"]
for i,v in enumerate(d):
    print(i,v)

def findMinAndMax(L):
    if len(L)==0:
        return (None, None)
    min=L[0]
    max=L[0]
    for i in L:
        if i<min:
            min=i
        if i>max:
            max=i
    return (min, max)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if isinstance(s,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')