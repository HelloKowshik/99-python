import logging;
import threading;
from concurrent.futures import ThreadPoolExecutor;
import time;
import random;


counter = 0;

def test(count):
    global counter;
    threadname = threading.current_thread().name;
    logging.info(f'Starting: {threadname}');
    for x in range(count):
        logging.info(f'Count: {threadname} += {count}');
        # counter += 1;
        #lock = threading.Lock();
        #lock.acquire();
        #lock.acquire(); #deadlock
        #try:
        #    counter += 1;
        #finally:
        #    lock.release()  

        #Locking Simplified
        lock = threading.Lock();
        with lock:
            logging.info(f'Locked: {threadname}');
            counter += 1;
            time.sleep(2);  

    logging.info(f'Finished: {threadname}');

def main():
    logging.basicConfig(format='%(levelname)s-%(asctime)s.%(msecs)03d:%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
    logging.info('Script Start');

    workers = 2;
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers * 2):
            v = random.randrange(1, 5);
            ex.submit(test, v);

    print(f'Counter = {counter}');        
    logging.info('Script Finished');


if __name__ == '__main__':
    main();        
