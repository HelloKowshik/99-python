import logging;
import socket;

def server(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    address = (ip, port);
    logging.info(f'Bind: {ip}:{port}');
    s.bind(address);
    logging.info('Listening...');
    s.listen(1);

    conn, addr = s.accept();
    logging.info(f'Connecting: {addr}');
    while True:
        data = conn.recv(1024);
        if len(data) == 0:
            logging.info('Exiting...');
            conn.close();
            break;
        logging.info(f'Data: {data}');
    logging.info('Closing The server...');
    s.close();        


def main():
    server('localhost', 2607);


logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
if __name__ == '__main__':
    main();    
