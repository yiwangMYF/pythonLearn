'''
测试set集合：无序,不重复
使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合
创建空集合不能使用{}(创建的是字典)，而应该使用set()
'''
#创建空集合
set1=set()
print(set1)
print(len(set1))

#创建非空集合
set2={'a','b','c'}
print(set2)
print(len(set2))

list1=[1,2,3,4]
set3=set(list1)
print(set3)
print(len(set3))

set4=set('9876543210')
print(set4)
print(len(set4))

#添加元素
set1.add('good')
set1.add(3)
print(set1)
print(len(set1))

#批量添加元素
set1.update((9,8,7))
print(set1)
print(len(set1))

'''
移除元素
#remove方法若要移除的元素不存在则报错
#discard方法，要移除的元素不存在不会报错
#pop方法，随机从集合中删除一个元素
'''
set1.remove(3)
set1.discard(10)
set1.pop()
print(f'set1:{set1}')
print(len(set1))

#清空集合
set4.clear()
print(set4)
print(len(set4))

#判断元素是否在集合中：x in set
if 7 in set1 :
    print("7 在set1集合中")
else :
    print("7 不在set1集合中")


