'''
1.模块是包含所有函数和变量的py文件,可以被别的程序引入和使用
2.引入模块：
    import moduleName1,moduleName2...    #引入多个模块全部内容
    from moduleName import part1,part2... #引入指定模块指定内容
    from moduleName import *             #引入指定模块全部内容（由单一下划线开头的函数和变量不会被引入,即）
3.一个模块只会被引入一次，无论import了多少次
4.python通过搜索路径搜索要引入的模块，搜索路径的值存储在sys模块中的path变量
5.一个模块被另一个模块第一次会执行主程序，若想模块中的代码块在被引入时不执行，使用__name__属性来使该程序块仅在该模块自身运行时执行
每个模块都有一个__name__属性，其值为'__main__'表示该模块自身在运行，否则是被引入的
6.内置的dir函数可以返回模块内定义的所有名称，以字符串列表展示
7.包是一种管理python模块命名空间的形式，采用'点模块名称'，如A.B表示A包下的B模块。
   在导入包时python会根据搜索路径（sys.path）搜索该目录下的子目录，若子目录中包含一个__init__.py的文件，则认为当前目录是一个包，
   __init__.py可以为空文件，也可以包含一些初始化代码及为__all__赋值
8.若模块中有__all__变量，则‘from moduleName import *’只会导入__all__变量中的值
'''

from pp import sum1
import sys


if __name__=='__main__':
    print('sum1+1:',sum1(1,1,2,2,3,3))
    print('sum module:',dir(sum1))
    print('sys module:',dir(sys))
else:
    print('I am imported')