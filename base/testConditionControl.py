'''
测试python条件控制
1.if语句的关键字：if-elif-else,其中elif为其他语言中的“else if”
2.在python中没有switch...case语句，在python3.10添加了match...case替代
'''

set1={1,'a','b','c',(6,)}

nn=set1.pop()
if isinstance(nn,int):
    print(f'您抽到了一个数字：{nn}')
elif isinstance(nn,str):
    print(f'您抽到了一个字符：{nn}')
else:
    print(f'您抽到了一个元组：{nn}')


#测试match..case，当前版本3.11，_相当于java中的default
mm=set1.pop()
match mm:
    case 1:
        print(f'您抽到了一个数字：{mm}')
    case 'a'|'b'|'c':
        print(f'您抽到了一个字符：{mm}')
    case _:
        print("默认值")

