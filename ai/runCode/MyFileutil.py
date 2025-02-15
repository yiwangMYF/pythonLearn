import multiprocessing as mp
import os
import shutil

'''
使用多进程进行文件的复制
'''
class MyFileutil(object):

    def __init__(self,num):
        self.__pool=mp.Pool(num)

    def copyFile(self,src,dst):
        #判断源文件和目标路径是否存在
        if not os.path.exists(src):
            raise FileNotFoundError(src)
        if not os.path.exists(dst):
            os.makedirs(dst)

        if os.path.isfile(src):
            shutil.copyfile(src, dst)
        else:
            results=[]
            for file in os.listdir(src):
                print('file: ',file)
                '''
                file只是相对路径，需要转为全路径才能进行文件判断和复制
                '''
                _src = os.path.join(src, file)
                _dst = os.path.join(dst, file)
                print(_src,_dst)
                if os.path.isfile(_src):
                    results.append(self.__pool.apply_async(shutil.copyfile,args=(_src,_dst)))
                else:
                    results.append(self.__pool.apply_async(shutil.copytree,(_src,_dst),{'dirs_exist_ok': True}))
            #阻塞等待获取结果
            for r in results:
                print('-'*10)
                r.get()

    def close(self):
        '''
        close() 会关闭进程池，使其不再接受新任务，
        而 join() 会等待所有进程执行完毕。如果没有 join()，程序可能会提前退出，导致某些任务未完成
        :return:
        '''
        self.__pool.close()
        self.__pool.join()



if __name__ == '__main__':
    fu=MyFileutil(10)
    fu.copyFile('E:\\java\\book','E:\\java\\book2')
    fu.close()

