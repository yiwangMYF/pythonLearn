'''
装饰器：允许动态地修改函数或类的行为
- 接收一个函数作为参数并返回一个新的函数或修改原有函数

1.装饰器语法格式:
 def decorator_function(origin_function):
    def wrapper(*agrs,**kwargs):
        #调用函数前操作
        before_call()
        result=origin_function(*agrs,**kwargs)
        #调用函数后操作
        after_call
        return result
    return wrapper
注:*agrs和**kwargs时两种特殊的函数参数,它们允许函数接受任意数量
的位置参数或关键字参数
*args:用于接收任意数量的位置参数,会被收集到一个元组中
**kwargs:用于接收任意数量的关键字参数,会被收集到一个字典中,key是参数名

2.使用装饰器: 通过@符号应用在函数定义之前
@decorator_function
def target_function(arg1,arg2):
    pass

3.装饰器函数可以接收参数
'''
import time
#测试装饰器
#定义装饰器
def printLog(oriFunction):
    def log(*args,**kwargs):
        start=time.time()
        print('函数开始调用,startTime:',start)
        result=oriFunction(*args,**kwargs)
        end=time.time()
        print('函数调用结束,endTime:',end)
        print('函数调用总耗时:',end-start)
        return result
    return log

@printLog
def sum(*nums):
    print('nums:',nums)
    print('numsType:',type(nums))
    sum=0
    for i in nums[0]:
        print('i:',i)
        if (not isinstance(i,int)):
            raise Exception('非数字参数无法进行计算:',i)
        else:
            sum+=i
    return sum
tuple1=tuple(range(1,10))
print(sum(tuple1))
        
