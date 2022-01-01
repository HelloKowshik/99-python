import logging;
import threading;
from threading import Thread, Timer;
from concurrent.futures import ThreadPoolExecutor;
import time;


def test():
    threadname = threading.current_thread().name;
    logging.info(f'Starting: {threadname}');
    for x in range(60):
        logging.info(f'Working: {threadname}');
        time.sleep(1);
    logging.info(f'Finished: {threadname}');    


def stop():
    logging.info('Exiting The App');
    exit(0);    


def main():
    logging.basicConfig(format='%(levelname)s-%(asctime)s.%(msecs)03d:%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
    logging.info('Main Thread Started');

    #stop in 3 sec.
    t = Timer(3, stop);
    t.start();

    #Run a thread
    # t1 = Thread(target=test, daemon=False);
    t1 = Thread(target=test, daemon=True);
    t1.start();

    logging.info('Main Thread Finished');


if __name__ == '__main__':
    main();    
