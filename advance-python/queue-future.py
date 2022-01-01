import logging;
import threading;
from threading import Thread;
from concurrent.futures import ThreadPoolExecutor;
from queue import Queue;
import time;
import random;

#Queues
def test_que(name, que):
    threadname = threading.current_thread().name;
    logging.info(f'Starting: {threadname}');
    time.sleep(random.randrange(1, 5));
    logging.info(f'Finished: {threadname}');
    msg = 'Hello ' + name + '. Your Id: '+ str(random.randrange(1, 100));
    que.put(msg);

def queued():
    que = Queue();
    t = Thread(target=test_que, args=['Kowshik', que]);
    t.start();
    logging.info('Do something on the main thread');
    t.join();
    retrn = que.get();
    logging.info(f'Returned: {retrn}');    

#Futures
def test_futures(name):
    threadname = threading.current_thread().name;
    logging.info(f'Starting: {threadname}');
    time.sleep(random.randrange(1, 5));
    logging.info(f'Finished: {threadname}');
    msg = 'Hello ' + name + '. Your Id: '+ str(random.randrange(1, 100));
    return msg;

def pooled():
    workers = 20;
    ret = [];
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers):
            v = random.randrange(1, 5);
            future = ex.submit(test_futures, 'anik' + str(x));
            ret.append(future);
    logging.info('Doing Something in the main Thread!');
    for r in ret:
        logging.info(f'Returned: {r.result()}');       


def main():
    logging.basicConfig(format='%(levelname)s-%(asctime)s.%(msecs)03d:%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
    logging.info('App Start');
    # queued();
    pooled();


if __name__ == '__main__':
    main();    
