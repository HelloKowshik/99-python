import logging;
import socket;
import select;

#Block Socket
def create_blocking(host, ip):
    logging.info('Blocking - Creating Socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    logging.info('Blocking - Connecting')
    s.connect((host, ip));
    logging.info('Blocking - Connected');
    logging.info('Blocking - Sending...');
    s.send(b'Hello From Blocking\r\n');
    logging.info('Blocking - Waiting...');
    data = s.recv(1024);
    logging.info(f'Blocking - Data={len(data)}');
    s.close();


def create_non_blocking(host, ip):
    logging.info('Non Blocking - Creating Socket');
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    logging.info('Non Blocking - Connecting');
    returnedVal = s.connect_ex((host, ip)); #Although it's Blocking!

    if returnedVal != 0:
        logging.info('Non Blocking - Failed to Connect');
        return;
    
    logging.info('Non Blocking - Connected');
    s.setblocking(False);

    inputs = [s];
    output = [s];

    while inputs:
        logging.info('Non Blocking - waiting...');
        readable, writable, exceptional = select.select(inputs, output, inputs, 0.5);

        for s in writable:
            logging.info('Non Blocking - Sending...')
            data = s.send(b'Hello From Non-Blocking\r\n');
            logging.info(f'Non Blocking - sent:{data}');
            output.remove(s);

        for s in readable:
            logging.info('Non Blocking - reading...')
            data = s.recv(1024);
            logging.info(f'Non Blocking - data:{len(data)}');
            logging.info('Non Blocking - Closing...');
            s.close();
            inputs.remove(s);

        for s in exceptional:
            logging.info('Non Blocking - error') ;
            inputs.remove(s);
            output.remove(s);  
            break;     


def main():
    # create_blocking('voidrealms.com', 80);
    create_non_blocking('voidrealms.com', 80);


logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
if __name__ == '__main__':
    main();   
