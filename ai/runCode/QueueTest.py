import time
import multiprocessing as mp
#生产者
def produce(q):
    _time=100
    while(_time>0):
        print('生产了'+str(_time))
        q.put(str(_time))
        time.sleep(2<<(100-_time))
        _time-=1

def consume(q):
    while(True):
        print('消费数据：'+q.get())



if __name__ == '__main__':
    # 创建队列
    q = mp.Queue(10)
    # 创建进程
    pp = mp.Process(target=produce, args=(q,))
    cc = mp.Process(target=consume, args=(q,))
    cc.start()
    pp.start()
