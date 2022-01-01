import logging;
import socket;

def download(server, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    address = (server, port);
    logging.info(f'Connecting to {server}:{port}');

    s.connect(address);
    logging.info('Connected');
    logging.info('Sending...');
    s.send(b'Hello\r\n');

    logging.info('Receive');
    data = s.recv(1024);

    logging.info('Closing...');
    s.close();
    logging.info(f'Data: {data}');



def main():
    download('voidrealms.com', 80);
    # download('react-meetup2021.netlify.app', 80);


logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
if __name__ == '__main__':
    main();    
