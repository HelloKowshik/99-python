import logging;
import socket;
import threading;
import multiprocessing;
import time;
import sys;

def make_socket(ip='localhost', port=2637, sender=False):
    proc = multiprocessing.current_process().name;
    logging.info(f'{proc} Starting...');
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
    if sender:
        logging.info(f'{proc} starting to SEND');
    else:    
        logging.info(f'{proc} binding to PORT');
        s.bind((ip, port));
    with s:
        while True:
            if sender:
                logging.info(f'{proc} sending...');
                s.sendto(b'Hello From UDP', (ip, port));
                time.sleep(1);
            else:
                data, addr = s.recvfrom(1024);    
                logging.info(f'{proc}: from {addr} = {data}');


def main():
    broadcaster = multiprocessing.Process(target=make_socket, kwargs={'sender': True}, daemon=True,name='Broadcaster');
    listener = multiprocessing.Process(target=make_socket, kwargs={'sender': False}, daemon=True,name='Listener');
    broadcaster.start();
    listener.start();

    timer = threading.Timer(5, sys.exit, [0]);
    timer.start();


logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
if __name__ == '__main__':
    main();   
