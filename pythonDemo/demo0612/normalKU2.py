# 这个模块我们之前已经用过很多次了，生成随机数、实现随机乱序和随机抽样，下面是常用函数的列表。
#
# getrandbits(k)：返回具有k个随机比特位的整数。
# randrange(start, stop[, step])：从range(start, stop, step) 返回一个随机选择的元素，但实际上并没有构建一个range对象。
# randint(a, b)：返回随机整数N满足a <= N <= b，相当于randrange(a, b+1)。
# choice(seq)：从非空序列seq返回一个随机元素。 如果seq为空，则引发IndexError。
# choices(population, weight=None, *, cum_weights=None, k=1)：从population中选择替换，返回大小为k的元素列表。 如果population为空，则引发IndexError。
# shuffle(x[, random])：将序列x随机打乱位置。
# sample(population, k)：返回从总体序列或集合中选择k个不重复元素构造的列表，用于无重复的随机抽样。
# random()：返回[0.0, 1.0)范围内的下一个随机浮点数。
# expovariate(lambd)：指数分布。
# gammavariate(alpha, beta)：伽玛分布。
# gauss(mu, sigma) / normalvariate(mu, sigma)：正态分布。
# paretovariate(alpha)：帕累托分布。
# weibullvariate(alpha, beta)：威布尔分布。
# os.path - 路径操作相关模块
# os.path模块封装了操作路径的工具函数，如果程序中需要对文件路径做拼接、拆分、获取以及获取文件的存在性和其他属性，这个模块将会非常有帮助，下面为大家罗列一些常用的函数。
#
# dirname(path)：返回路径path的目录名称。
# exists(path)：如果path指向一个已存在的路径或已打开的文件描述符，返回 True。
# getatime(path) / getmtime(path) / getctime(path)：返回path的最后访问时间/最后修改时间/创建时间。
# getsize(path)：返回path的大小，以字节为单位。如果该文件不存在或不可访问，则抛出OSError异常。
# isfile(path)：如果path是普通文件，则返回 True。
# isdir(path)：如果path是目录（文件夹），则返回True。
# join(path, *paths)：合理地拼接一个或多个路径部分。返回值是path和paths所有值的连接，每个非空部分后面都紧跟一个目录分隔符 (os.sep)，除了最后一部分。这意味着如果最后一部分为空，则结果将以分隔符结尾。如果参数中某个部分是绝对路径，则绝对路径前的路径都将被丢弃，并从绝对路径部分开始连接。
# splitext(path)：将路径path拆分为一对，即(root, ext)，使得root + ext == path，其中ext为空或以英文句点开头，且最多包含一个句点。
# uuid - UUID生成模块
# uuid模块可以帮助我们生成全局唯一标识符（Universal Unique IDentity）。该模块提供了四个用于生成UUID的函数，分别是：
#
# uuid1()：由MAC地址、当前时间戳、随机数生成，可以保证全球范围内的唯一性。
# uuid3(namespace, name)：通过计算命名空间和名字的MD5哈希摘要（“指纹”）值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，但同一命名空间的同一名字会生成相同的UUID。
# uuid4()：由伪随机数生成UUID，有一定的重复概率，该概率可以计算出来。
# uuid5()：算法与uuid3相同，只不过哈希函数用SHA-1取代了MD5。
# 由于uuid4存在概率型重复，那么在真正需要全局唯一标识符的地方最好不用使用它。在分布式环境下，uuid1是很好的选择，因为它能够保证生成ID的全局唯一性。下面是在Python交互式环境中使用uuid1函数生成全局唯一标识符的例子。

import uuid
uid=uuid.uuid1().hex
print(uid)
