'''
测试元组tuple
元组中的数据不能修改
'''

tuple1=('aaa','bbb','ccc','ddd')

print(type(tuple1))
print(tuple1)

#元组不用括号包裹也行
tuple2=2,3,4,5
print(type(tuple2))
print(tuple2)


print(tuple2[0])
#切片截取
print(tuple2[0:2])
#组合
print(tuple1+tuple2)

#获取元组中的最大值
print(max(tuple2))

#list转元组
list2=[9,8,7]
tuple3=tuple(list2)

print(type(tuple3))
print(tuple3)
