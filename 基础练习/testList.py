list=["a","b","c"]

#打印
print(list)
#取第一个值
print(list[0])
#截取字符
print(list[0:3])

#删除list中的索引为的数据
del list[2]

print(list)

#添加列表值
list.append("good")

print(list)

list2=['d','e','f']
#列表合并
print(list+list2)
#获取列表长度
print(len(list))

#嵌套列表
list[0]=["a1",'a2']
print(list)

print(list[0][1])