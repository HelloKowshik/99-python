import logging;
import threading;
import multiprocessing;
import asyncio;
import random;

def display(msg):
    threadname = threading.current_thread().name;
    processname = multiprocessing.current_process().name;
    logging.info(f'{processname} \ {threadname} : {msg}');

async def work(name):
    display(name+' Started');
    await asyncio.sleep(random.randint(1, 10));
    display(name+' Finished');

async def run_async(max):
    tasks = [];
    for x in range(max):
        name = 'Item-' + str(x);
        tasks.append(asyncio.ensure_future(work(name)));
    await asyncio.gather(*tasks);    

def main():
    display('Main Started');
    loop = asyncio.get_event_loop();
    loop.run_until_complete(run_async(50));
    loop.close();
    display('Main Finished');

logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
if __name__ == '__main__':
    main();
