import logging;
from threading import Thread;
import time;
import random;

def longTask(name):
    m = random.randrange(1, 10);
    logging.info(f'Task: {name} performing {str(m)} Times,,,');
    for x in range(m):
        logging.info(f'Task: {name} : {x}');
        time.sleep(random.randrange(1, 3));
    logging.info(f'Task: {name} Complete!');    

def main():
    logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
    logging.info('Starting...');
    # longTask('Main'); #Single Thread
    threads = [];
    for x in range(10):
        t = Thread(target=longTask, args=['thread-'+str(x)]);
        threads.append(t);
        t.start();
 
    for t in threads:
        t.join();

    logging.info('Finished All Thread...')

if __name__ == '__main__':
    main()    
