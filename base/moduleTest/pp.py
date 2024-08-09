'''
测试模块
'''
__all__=['sum1']
def sum1(*nums):
    sum=0
    for i in nums:
        sum=sum+i
    return sum


