import logging;
import time;
import random;
import multiprocessing;
from multiprocessing.context import Process;

def work(item, count):
    name = multiprocessing.current_process().name;
    logging.info(f'{name} Started : {item}')
    for x in range(count):
        logging.info(f'{name} : {item} = {x}');
        time.sleep(1);
    logging.info(f'{name} Finished!');
    return item + ' is Finished.';       

def proc_result(result):
    print(f'Result = {result}');

def main():
    logging.info('App Started');
    max = 5;
    pool = multiprocessing.Pool(max);
    results = [];
    for x in range(max):
        item = 'Item-'+ str(x);
        count = random.randrange(1, 5);
        r = pool.apply_async(work, [item, count], callback=proc_result);
        results.append(r);
    for r in results:
        r.wait();
    pool.close();       
    pool.join();
    logging.info('Finished');        

logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
if __name__ == '__main__':
    main();
