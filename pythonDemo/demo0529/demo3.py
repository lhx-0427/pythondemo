"""
它以键值对（键和值的组合）的方式把数据组织到一起，我们可以通过键找到与之对应的值并进行操作。就像《新华字典》中，
每个字（键）都有与它对应的解释（值）一样，
每个字和它的解释合在一起就是字典中的一个条目，而字典中通常包含了很多个这样的条目。
"""
person=dict(name='Bob',age=20,gender='male')#字典的创建
print(person)

# 可以通过Python内置函数zip压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '12345'))
print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
"""
可以通过pop或popitem方法从字典中删除元素，前者会返回（获得）键对应的值
，但是如果字典中不存在指定的键，会引发KeyError错误；后者在删除元素时，会返回（获得）键和值组成的二元组。字典的clear方法会清空字典中所有的键值对
"""
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.pop('age'))  # 25
print(person)             # {'name': '王大锤', 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.popitem())   # ('addr', '成都市武侯区科华北路62号1栋101')
print(person)             # {'name': '王大锤', 'height': 178}
person.clear()
print(person)             # {}
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
del person['age']
del person['addr']
print(person)  # {'name': '王大锤', 'height': 178}

"""
允许我们以键值对的形式保存数据，再通过键访问对应的值。字典是一种非常有利于数据检索的数据类型
，但是需要再次提醒大家，字典中的键必须是不可变类型，列表、集合、字典等类型的数据都不能作为字典的键
"""