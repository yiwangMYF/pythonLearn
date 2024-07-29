'''
测试迭代器
1.迭代器是一个可以记录遍历的位置的对象，从第一个元素开始访问，知道所有元素访问结束，迭代器只能往前不会后退
迭代器的两个基本方法：
iter():创建迭代器对象
netx():获取下一个元素
2.可创建迭代器的对象：字符串、列表、元组和类中实现两个方法 __iter__() 与 __next__()的对象
3.StopIteration 异常标识迭代的完成
'''

#测试迭代器
list1=list(range(1,10))

print('list:',list1)
tt=iter(list1)
while True:
    try:
        print(next(tt))
    except StopIteration:
        print('迭代完成')
        break
print('----------------------结束---------------------')