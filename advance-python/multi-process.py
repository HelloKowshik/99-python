import logging;
import time;
import multiprocessing;
from multiprocessing import process;

def run(num):
    processname = process.current_process().name;
    logging.info(f'Running {processname} as {__name__}');
    time.sleep(num * 2);
    logging.info(f'Finished {processname}');

def main():
    # logging.basicConfig(format='%(levelname)s-%(asctime)s.%(msecs)03d:%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
    processname = process.current_process().name;
    logging.info(f'Running {processname} as {__name__}');
    processes = [];
    for x in range(5):
        p = multiprocessing.Process(target=run, args=[x], daemon=True);
        processes.append(p);
        p.start();

    for p in processes:
        p.join();    

    logging.info(f'Finished {processname}');


logging.basicConfig(format='%(levelname)s-%(asctime)s.%(msecs)03d:%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
if __name__ == '__main__':
    main()
