# -*- coding: cp936 -*-
if __name__ == "__main__":
    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8001))
    import time

    flag = '1'
    while True:
        time.sleep(1)
        flag = '1'
        print('send to server with value: ' + flag)
        flag = flag.encode(encoding="utf-8")
        sock.send(flag)
        print(sock.recv(1024))
        flag = '2'
        print('send to server with value: ' + flag)
        flag = flag.encode(encoding="utf-8")
        sock.send(flag)
        print(sock.recv(1024))
        #flag = (flag == '1') and '2' or '1'  # change to another type of value each time

    sock.close()