import multiprocessing;
import logging;
import time;
from multiprocessing import process;
from multiprocessing.context import Process;
from multiprocessing.connection import Listener, Client;


def proc(server='localhost', port=5000, password=b'password'):
    name = process.current_process().name;
    logging.info(f'{name} Started');
    address = (server, port);
    listener = Listener(address, authkey=password);
    conn = listener.accept();
    logging.info(f'{name} : connection from {listener.last_accepted}');
    while True:
        msg = conn.recv();
        logging.info(f'{name} data in: {msg}');
        if msg == 'quit':
            conn.close();
            break;
    listener.close(); #server down        
    logging.info(f'{name} Finished');

def main():
    name = process.current_process().name;
    logging.info(f'{name} Started');
    address = 'localhost';
    port = 2823;
    password = b'password';
    p = Process(target=proc,args=[address,port,password],daemon=True,name='Worker');
    p.start();
    logging.info(f'{name} waiting on the working...');
    time.sleep(1);

    dest = (address, port);
    conn = Client(dest, authkey=password);

    while True:
        command = input('\n type your command or quit: \n').strip();
        logging.info(f'{name} command: {command}');
        conn.send(command);
        if command == 'quit':
            break;

    if p.is_alive:
        logging.info(f'{name} is terminating worker...');
        conn.close();
        time.sleep(1);
        p.terminate();
    p.join();        

    logging.info(f'{name} Finished');


logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
if __name__ == '__main__':
    main();
