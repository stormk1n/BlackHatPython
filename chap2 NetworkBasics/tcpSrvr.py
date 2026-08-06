import sys
import socket
import argparse
import threading

"""
ip="0.0.0.0"
port=9998
"""

# Recvs and sends simple message back to clnt
def hndlClnt(clntSckt):
    with clntSckt as sock:
        request = sock.recv(1024)
        
        print(f"[*] Recieved: {request.decode('utf-8')}")
        sock.send(b'ACK')


def mainSrvr(Lhost, Lport):
    try:
        tcpSrvr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # setting the server in listenning mode
        tcpSrvr.bind((Lhost, Lport))
        
        # setting a max back log request of 5
        tcpSrvr.listen(5)
        
        print(f"[+] Listening on {Lhost}:{Lport}")
        
        # Placing the server in listening loop
        
        while True:
            # client socket goes to tcpClnt varaible
            # remote connection details goes to addrs varaible
            tcpClnt, addrs = tcpSrvr.accept()
            
            print(f"Accepted connection from {addrs[0]}:{addrs[1]}")
            
            # creating new thread that points to hndlClnt
            # while passing clnt socket as argument
            
            clntHndler = threading.Thread(target=hndlClnt,args=(tcpClnt,))
            clntHndler.start()

        return True

    except Exception as err:
        print(f"{err}")
        return False

    except KeyboardInterrupt:
        print("\n[-] KeyboardInterrupt detected, closing cleanly")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="TCP Server",
        usage="tcpSrvr [Lhost] [Lport]"
    )

    parser.add_argument('Lhost', help="Host to listen for connections on (localhsot)")
    parser.add_argument('Lport', help="Port to listen for connections on")

    if len(sys.argv) == 1 or len(sys.argv) == 2:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    mainSrvr(args.Lhost, int(args.Lport))



if __name__ == "__main__":
    main()


