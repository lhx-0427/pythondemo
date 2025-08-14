# print("n\nnn")
# print("n\ttn")
# print(r'n\nnn')
# a=72
# b=85
# r=(b-a)/a
# print(f"提升为：{r:.1f}")

#
# args = ['gcc', 'hello.c', 'world.c']
# # args = ['clean']
# # args = ['gcc']
#
# match args:
#     # 如果仅出现gcc，报错:
#     case ['gcc']:
#         print('gcc: missing source file(s).')
#     # 出现gcc，且至少指定了一个文件:
#     case ['gcc', file1, *files]:
#         print('gcc compile: ' + file1 + ', ' + ', '.join(files))
#     # 仅出现clean:
#     case ['clean']:
#         print('clean')
#     case _:
#         print('invalid command.')
# L = ['Bart', 'Lisa', 'Adam']1
# for i in L:
#     print('Hello,', i)
dict1={'name':'Bart','age':7,'sex':'male'}
dict1.setdefault('name','Bart1')
print(dict1.get('name1',"没有这玩意儿"))
print(dict1)