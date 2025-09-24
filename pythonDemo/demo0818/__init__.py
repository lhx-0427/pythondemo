#生成器
def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))]

d=triangles()
for i in range(5):
    print(next(d))