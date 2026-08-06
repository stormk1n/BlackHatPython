import socket
import threading


ip="0.0.0.0"
port=9998

def main(ip, port):
    tcpSrvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # setting the server in listenning mode
    tcpSrvr.bind((ip, port))

    # setting a max back log request of 5
    tcpSrvr.listen(5)

    print(f"[+] Listening on {ip}:{port}")

    # Placing the server in listening loop
    while True:
        # client socket goes to tcpClnt varaible
        # remote connection details goes to addrs varaible
        tcpClnt, addrs = tcpSrvr.accept()
        
        print(f"Accepted connection from {addrs[0]}:{addrs[1]}")

        # creating new thread that points to hndlClnt
        # while passing clnt socket as argument
        clntHndler = threading.Thread(target=hndlClnt,args=(tcpClnt,))



