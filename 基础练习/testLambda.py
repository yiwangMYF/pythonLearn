'''
匿名函数：使用lambda创建匿名函数
lambda函数只有一个语句，语法格式：
lambda arguments: expression

lambda是 Python 的关键字，用于定义 lambda 函数。
arguments 是参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定。
expression 是一个表达式，用于计算并返回函数的结果。
'''
#测试lambda函数
sum=lambda n1,n2:n1+n2
print(sum(1,2))