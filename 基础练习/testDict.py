'''
字典是一种可变容器模型
字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中
'''
#创建空字典
dict1={}
dict2=dict()

print(dict1)
print(dict2)

print(type(dict1))
print(len(dict1))

#往字典里添加值,字典里的key必须为不可变对象(数字、字符串、元组)
tuple1=(1,2,3)
print(tuple1)
dict1['name']='myf'
dict1['age']=100
dict1[tuple1]='good'
print(dict1)

#删除字典里的值
del dict1[tuple1]
print(dict1)

print(len(dict1))
print(str(dict1))
print('------------------------------------')
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print('------------------------------------')

for k in dict1.keys():
    print(f'k:{k},v:{dict1[k]}')