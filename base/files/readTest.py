'''
文件读写
1.打开文件：open(fileName,mode,encoding='utf-8')
fileName:文件名url
mode:文件访问模式，只读，写入，追加等
encoding:编码

常用模式：
w:打开一个文件用于写入，若文件不存在则创建，从头开始写，会覆盖原有内容
a:打开一个文件用于写入，若文件不存在则创建，追加写
r:只读方式打开文件，从头开始读，默认模式
w+:w+读功能
a+:a+读功能
r+：r+写功能

2.文件读取
文件对象.read(num)  读取指定字节的数据，若未传入num，则读取当前文件的全部数据;若返回数据长度为0则说明文件数据已读取完
文件对象.readlines() 读取文件中所有行，返回一个列表，每行内容作为一个元素
文件对象.readline() 读取文件中的一行内容

3.文件关闭
文件对象.close()

'''

fileName=".\README.md"

def testReadNum():
    f=open(fileName,'r',encoding='utf-8')
    loop=0
    while True:
        loop+=1
        print('loop1:',loop)
        content=f.read(1)
        if len(content)==0:
            break
        else:
            print(content)
    f.close

def testReadWithOutNum():
    f=open(fileName,'r',encoding='utf-8')
    loop=0
    while True:
        loop+=1
        print('loop2:',loop)
        content=f.read()
        if len(content)==0:
            break
        else:
            print(content)
    f.close()

#按行全部读取
def testReadLines():
    f=open(fileName,'r',encoding='utf-8')
    loop=0
    while True:
        loop+=1
        print('loop3:',loop)
        content=f.readlines()
        if len(content)==0:
            break
        else:
            print(content)
    f.close()

#按行读取
def testReadLine():
    f=open(fileName,'r',encoding='utf-8')
    loop=0
    while True:
        loop+=1
        print('loop3:',loop)
        content=f.readline()
        if len(content)==0:
            break
        else:
            print(content)
    f.close()

if __name__=='__main__':
    testReadNum()
    testReadWithOutNum()
    testReadLines()
    testReadLine()
       

    