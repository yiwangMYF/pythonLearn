'''
测试循环
1.python中循环有for和while两种
2.while循环语法格式：
while condition:
    trueStatement
else:
    falseStatement
#当while的condition为false时执行else后面的语句
3.for循环语句格式：
for value in 可迭代对象:
    statement
else:
    循环完毕后执行语句
'''

#测试while循环
list1=[1,2,3,4,5,6,7,8,9]

index=0
length=len(list1)
while index<length:
    mm=list1[index]
    print(f'遍历取值：{mm}')
    if mm>7:
        print('由于取的值大于7,提前结束循环')
        break
    index=index+1
else:
    print('结束遍历了')


#测试for循环

for val in list1:
    print(f'列表值：{val}')
else:
    print('完成for循环遍历')


#使用range函数生成可遍历的数列
for i in range(10):
    print(i)
else:
    print('------------------------------------------')
#range(startNum,endNum,step),不包含endNUm,step:步长
for j in range(0,10,2):
    print(j)


#python 中pass是空语句，用于占位
for k in range(10):
    mm=k%2
    if mm==0:
        print(f'{k}是10以内的偶数')
    else:
        pass
