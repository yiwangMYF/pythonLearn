
'''
1.列表中的元素是可变的(字符串元组中的元素不可变)
'''


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

#在末尾添加列表值
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

#extend(L):添加指定列表的元素到当前列表
list11=[1,2]
list12=[3]
list12.extend(list11)
print('list12:',list12)
print(len(list12))

#insert(index,value):在列表指定索引(index)之前插入值value
#insert(0,value):在列表前插入值
list12.insert(0,100)
print('list12插入index0前:',list12)
#insert(len(L),value):等同于append(value)
list12.insert(len(list12),10000)
print('list12插入index末尾:',list12)

#remove(x):删除列表中值为x的第一个元素,若没有这样的元素会返回一个错误
try:
    list12.remove(999)
except:
    print('remove999错误')