'''
测试推导式
1.python中的list、set、tuple、dict都支持推导式
2.列表推导式格式：
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]
或者 
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
out_exp_res：列表生成元素表达式，可以是有返回值的函数。
for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
if condition：条件语句，可以过滤列表中不符合条件的值

3.字典推导式格式：
{ key_expr: value_expr for value in collection }
或
{ key_expr: value_expr for value in collection if condition }
key_expr：key处理表达式
value_expr：value处理表达式

4.集合推导式格式：
{ expression for item in Sequence }
或
{ expression for item in Sequence if conditional }

5.元组推导式格式：
(expression for item in Sequence )
或
(expression for item in Sequence if conditional )

'''

list1=[1,2,3,4,5]
list2=[num+1 for num in list1]
print(list1)
print(list2)

#测试if condition
list3=[num*2 for num in list1 if num>3]
print(list3)

print('---------------------------测试字典推导式-----------------------------------')
#测试字典推导式
dict1={'name':'素还真'}
dict1['age']=2000
dict2={key+'<>good':value+100 for key,value in dict1.items() if isinstance(value,int)}
print(dict1)
print(dict2)

print('---------------------------测试集合推导式-----------------------------------')
#测试集合推导式
set1=set()
set1.add('a')
set1.add(1000)
set2={num**2 for num in set1 if isinstance(num,int)}
print(set1)
print(set2)

print('---------------------------测试元组推导式-----------------------------------')
#测试元组推导式
tuple1=tuple(list1)
tuple2=tuple((num ** 2 for num in tuple1))
tuple3=tuple((num ** 2 for num in range(1,8,2)))
print(tuple1)
print(tuple2)
print(tuple3)