import logging;
import time;
import multiprocessing;
from multiprocessing.context import Process;

def work(msg, max):
    name = multiprocessing.current_process().name;
    logging.info(f'{name} Started!');
    for x in range(max):
        logging.info(f'{name} {msg}');
        # print(f'{name} {msg}')
        time.sleep(1);
    logging.info(f'{name} Finished!');    

def main():
    logging.info('App Started');
    max = 20;
    worker = Process(target=work, args=['Working', max], daemon=True, name='Worker');
    worker.start();
    time.sleep(5);

    if worker.is_alive:
        worker.terminate();
    worker.join();
    logging.info(f'Finished: {worker.exitcode}');    


logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
if __name__ == '__main__':
    main();            
