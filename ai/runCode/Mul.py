import multiprocessing
import time

class MyProcess(multiprocessing.Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s进程开始执行'%self.name)
        _time=10
        while(_time>0):
            print('---牛马工作中---')
            print('_time:%d'%_time)
            time.sleep(2<<(10-_time))
            _time -=1
        print('%s进程结束'%self.name)


if __name__ == '__main__':
    myP1 = MyProcess('自定义进程1')
    myP1.start()
    if not myP1.is_alive:
        print('校验一下进程状态:False')
    else:
        print('校验一下进程状态:True')

