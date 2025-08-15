import  math
#求解方程 ax^2+bx+c=0
# def quadratic(a,b,c):
#     x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
#     x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
#     return x1,x2
# print('quadratic(2,3,1) =',quadratic(2,3,1))
# print('quadratic(1,3,-4) =',quadratic(1,3,-4))
#默认参数，函数定义中指定默认参数，当大于2时，参数n为传入得值  否则默认为n为2
# def power(x,n=2):
#     s=1
#     while n>0:
#         n=n-1
#         s=s*x
#     return s
# print('power(5) =',power(5,3))
def mul(*args):
    s=1
    if(len(args)==0):
        raise TypeError
    for i in args:
        s=s*i
    return s
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')