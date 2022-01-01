import logging;
import time;
import random;
import multiprocessing;
import threading;
from threading import Thread;
from queue import Queue;

def display(msg):
    threadname = threading.current_thread().name;
    processname = multiprocessing.current_process().name;
    logging.info(f'{processname} \ {threadname} : {msg}');

#Producer
def create_work(queue, finished, max):
    finished.put(False);
    for x in range(max):
        v = random.randint(1, 100);
        queue.put(v);
        display(f'Producing {x}:{v}');
    finished.put(True);
    display('Finished');

#Consumer
def perform_work(work, finished):
    counter = 0;
    while True:
        if not work.empty():
            v = work.get();
            display(f'Consuming {counter} : {v}');
            counter += 1;
        else:
            v = finished.get();
            if v == True:
                break;
            display('Finished');    


def main():
    work = Queue();
    finished = Queue();
    max = 50;
    producer = Thread(target=create_work, args=[work, finished, max], daemon=True);
    consumer = Thread(target=perform_work, args=[work, finished], daemon=True);

    producer.start();
    consumer.start();

    producer.join();
    display('producer has finished');

    consumer.join();
    display('Consumer has finished');
    display('Finished')

logging.basicConfig(format='%(levelname)s-%(asctime)s.%(msecs)03d:%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
if __name__ == '__main__':
    main();    
