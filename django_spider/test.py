import time
from multiprocessing import Process
def a():
    print('a')
    time.sleep(2)
def b():
    print('b')
    time.sleep(2)
if __name__=='__main__':
    p= Process(target=a,args=())
    p.start()

    p1=Process(target=b)
    p1.start()

