'''
测试函数
1.python函数格式如下：
    def 函数名（参数列表）:
        函数体
2.在python中字符串、数字、和元素是不可变对象，list、dict等是可变对象
函数的参数传递：
    可变对象：引用传递
    不可变对象：值传递
3.id()函数可查看内存地址
'''
#测试函数定义及调用

def log(str):
    print(str)

log('good good')

#测试函数的参数传递
def testImmutable(a):
    a=201
    print(id(a))
a=200
print('first:',id(a))
testImmutable(a)

print('----------------------------------------')
def testUnImmutable(b):
    b[0]=4
    print(id(b))
b=list(range(1,3))
print('firstbbb:',id(b))
testUnImmutable(b)


#必须参数：调用时必须以正确的顺序传入函数，且数量也要一致，否则会报错
#log()
#关键字参数：函数调用时通过使用关键字来确定传入的参数值；使用关键字参数来调用时可以不用按照函数定义时的参数顺序
def printUser(name,age):
    print(f'name:{name};age:{age}')
    return
printUser(age=100,name='myf')

#默认参数：函数定义时，可以给参数默认值,当没有传入参数值时，使用默认的参数值
def printUser2(name,age=1000):
    print(f'name:{name};age:{age}')
    return
printUser2(name='myfff')

#不定长参数：在参数前加*号表示不定长参数，不定长参数会以元组的形式传入

def printAll(*name):
    print('不定长参数类型:',type(name))
    print(name)

printAll('经常','每天','无时无刻')


