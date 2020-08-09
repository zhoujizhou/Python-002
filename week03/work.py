import sys
import os
import socket
import multiprocessing as mp
from multiprocessing import Pool

arg_list = set(['-n', '-f', '-ip', '-w'])

def Ping(ip):
    Return = os.system('ping %s' %ip)
    if Return:
        print(f'ping {ip} 不通！')
    else:
        print(f'ping {ip} 成功！')

def TCP(ip):

    port_list = []
    for port in range(1, 1025):
        try:
            link = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            link.connect((ip, port))
            port_list.append(port)
            print(f"tcp sucess. port %d is open" %port)
        except:
            print(f"port %d is closed!" %port)
        finally:
            link.close()

if __name__ == '__main__':
    arg_n=None
    arg_f=None
    lock = mp.Manager().RLock()

    arg_list = sys.argv[1:]
    for i in arg_list:
        if i.startswith('-') and i not in arg_list:
            print("" + i)
        elif i == '-n':
            arg_n = int(arg_list[arg_list.index('-n') + 1])
        elif i == '-f':
            arg_f = arg_list[arg_list.index('-f') + 1]
        elif i == '-ip':
            arg_ip = arg_list[arg_list.index('-ip') + 1]
            ip_list = arg_ip.split('-')
        elif i == '-w':
            arg_w = arg_list[arg_list.index('-w') + 1]

    pool = Pool(arg_n)
    if arg_f == 'ping':
        ip_s = ip_list[0].split('.')
        ip_e = ip_list[1].split('.')
        ip3 = ip_list[0][:ip_list[0].rfind('.') + 1]
        if ip_s[0] != ip_e[0] or ip_s[1] != ip_e[1] or ip_s[2] != ip_e[2] or ip_s[3] == ip_e[3]:
            print('IP范围不正确！')
        for i in range(int(ip_s[-1]), int(ip_e[-1]) + 1):
            ip = ip3 + str(i)
            pool.apply_async(Ping, args=(ip,))
    elif arg_f == 'tcp':
        ip = arg_ip
        pool.apply_async(TCP, args=(ip,))

    pool.close()
    pool.join()
