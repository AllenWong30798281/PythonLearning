# -*- coding: cp936 -*-
'''''
����һ��python server������ָ���˿ڣ�
����ö˿ڱ�Զ�����ӷ��ʣ����ȡԶ�����ӣ�Ȼ��������ݣ�
����������Ӧ������
'''
if __name__ == "__main__":
    import socket
print("Server is starting")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8001))  # ����soket����IP��ַ�Ͷ˿ں�
sock.listen(5)  # ������������������������Ӻ�server��ͨ����ѭFIFOԭ��
print("Server is listenting port 8001, with max connection 5")
while True:  # ѭ����ѯsocket״̬���ȴ�����

    connection, address = sock.accept()
    try:
        connection.settimeout(50)
        # ���һ�����ӣ�Ȼ��ʼѭ������������ӷ��͵���Ϣ
        ''''' 
        ���serverҪͬʱ���������ӣ������������Ӧ���ö��߳������� 
        ����server��ʼ�����������while�����ﱻ��һ��������ռ�ã� 
        �޷�ȥɨ�������������ˣ������̻߳�Ӱ�����ṹ�����Լǵ�������������1ʱ 
        ��������Ҫ��Ϊ���̼߳��ɡ� 
        '''
        while True:
            buf = connection.recv(1024).decode("utf-8")
            print("Get value " + buf)
            if buf == '1':
                print("send welcome")
                a="welcome to server"
                a=a.encode(encoding="utf-8")
                connection.send(a)
            elif buf != '0':
                print("send refuse")
                a= "please go out!"
                a=a.encode(encoding="utf-8")
                connection.send(a)
            else:
                print("close")
                break  # �˳����Ӽ���ѭ��
    except socket.timeout:  # ����������Ӻ󣬸��������趨��ʱ���������ݷ�������time out
        print('time out')

    print("closing one connection")  # ��һ�����Ӽ���ѭ���˳������ӿ��Թص�
    connection.close()