#可以导入time库  来实现线程休眠
import random
import  time
from random import Random

# for i in range(3600):
#     print(i)
#     time.sleep(1)
#range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
#range(1, 101)：可以用来产生1到100范围的整数，相当于是左闭右开的设定，即[1, 101)。
#range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长（跨度），即每次递增的值，101取不到。
#range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长（跨度），即每次递减的值，0取不到。
# for i in range(100,  0, -2):
#     print(i)
# print(sum(range(2,101,2)))
# total=0
# i=2
# while True:
#     total+=i
#     i+=2
#     if i>100:
#         break #跳出循环
# print(total)
#
#
# total = 0
# for i in range(1, 101):
#     if i % 2 != 0:
#         continue#跳过当前的循环
#     total += i
# print(total)
# num=random.randint(1,100)#在一定区间内 随机一个数
# end=int(num**0.5)
# is_prime=True
# for i in range(2,end+1):
#     if num%i==0:
#         is_prime=False
#         break
# if is_prime:
#     print('%d是素数'%num)
# else:
#     print('%d不是素数'%num)
x=6
y=12
for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print(f'最大公约数: {i}')
        break
#如果事先知道循环结构重复的次数，我们通常使用for循环；如果循环结构的重复次数不能确定，可以用while循环。此外，我们可以在循环结构中使用break终止循环，也可以在循环结构中使用continue关键字让循环结构直接进入下一轮次。