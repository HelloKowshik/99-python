import time
import threading

# print(time.ctime(1000000000))
# print(time.time())
# print(time.ctime(time.time()))

# time_obj = time.localtime()
# local_time = time.strftime('%B %d %Y %H:%M:%S', time_obj)
# print(local_time)


def task1():
    time.sleep(3)
    print('Task-1 Completed!')

def task2():
    time.sleep(4)
    print('Task-2 Completed!')

def task3():
    time.sleep(4)
    print('Task-3 Completed!')        

t1 = threading.Thread(target=task1, args=())
t1.start()
t2 = threading.Thread(target=task2, args=())
t2.start()
t3 = threading.Thread(target=task3, args=())
t3.start()

# task1()
# task2()
# task3()

print(threading.active_count())
print(threading.enumerate())
