import logging;
import socket;
import select;
import multiprocessing;


#create server

def chatserver(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
    logging.info(f'Binding to {ip}:{port}');
    server.bind((ip, port));
    server.setblocking(False);
    server.listen(100);
    logging.info(f'Listening on {ip}:{port}');

    readers = [server];

    while True:
        readable, writable, errors = select.select(readers, [], [], 0.5);

        for s in readable:
            try:
                if s == server:
                    client, address = s.accept();
                    client.setblocking(False);
                    readers.append(client);
                    logging.info(f'Connection: {address}');
                else:
                    data = s.recv(1024);
                    if data:
                        logging.info(f'Echo: {data}');
                        s.send(data);
                    else:
                        logging.info(f'Remove: {s}');
                        s.close();   
                        readers.remove(s);  

            except Exception as err:
                logging.warning(err.args);

            finally:
                pass        



def main():
    svr = multiprocessing.Process(target=chatserver, args=['localhost', 2607], daemon=True, name='Server');
    while True:
        command = input('Enter Command(start, stop)');
        if command == 'start':
            logging.info('Starting The Server.');
            svr.start();
        if command == 'stop':
            logging.info('Stopping the Server.');
            svr.terminate();
            svr.join();
            svr.close();
            logging.info('Server Stopped!');
            break;
    logging.info('App Finished!');         


logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
if __name__ == '__main__':
    main();  
