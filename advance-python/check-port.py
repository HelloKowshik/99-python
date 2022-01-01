import logging;
import socket;

def check_port(ip, port, timeout):
    returnedVal = False;
    logging.debug(f'Checking {ip}:{port}');

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        s.settimeout(timeout);
        conn = s.connect_ex((ip, port));
        logging.debug(f'Connection {ip}:{port} = {conn}');
        s.close();
        if conn == 0:
            returnedVal = False;
            logging.debug(f'In Use {ip}:{port}');
        else:
            returnedVal = True;
            logging.debug(f'Usable {ip}:{port}');    

    except Exception as ex:
        returnedVal = False;
        logging.debug(f'Error: {ip}:{port}={ex.msg}');

    finally:
        logging.debug(f'Result= {ip}:{port} = {returnedVal}');
        return returnedVal;    
            

def check_range(ip, scope):
    result = {};
    for p in scope:
        r = check_port(ip, p, 1.0);
        result[p] = r;
    return result;    


def main():
    # p = check_port('localhost', 5050, 2.0);
    # logging.info(f'Port 5050 Usable: {p}');
    ports = check_range('localhost', range(49667, 49672));
    for k,v in ports.items():
        logging.info(f'{k}: {v}');


logging.basicConfig(format='%(levelname)s-%(asctime)s-%(message)s', datefmt='%H:%M:%S', level=logging.DEBUG);
if __name__ == '__main__':
    main();    
