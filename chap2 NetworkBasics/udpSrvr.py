import sys
import socket
import argparse
import threading


def hndlClnt(clntSckt, addrs, udpSrvr):    
        request = clntSckt
        print(f"[*] Recieved:\n{request.decode('utf-8')}")
           
        response = 'ACK'
        udpSrvr.sendto(response.encode('utf-8'), addrs)

def mainSrvr(Lhost, Lport):
    udpSrvr = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udpSrvr.bind((Lhost, Lport))

    print(f"[+] UDP srvr Listening on {Lhost}:{Lport}")

    try:
        while True:
            udpClntMsg, addrs = udpSrvr.recvfrom(1024)

            clntHndler = threading.Thread(target=hndlClnt, args=(udpClntMsg, addrs, udpSrvr))
            clntHndler.start()
        
        return True

    except Exception as err:
        print(f"{err}")
        return False

    except KeyboardInterrupt:
        print("\n[-] KeyboardInterrupt detected, closing cleanly")
        return False
    
    finally:
        udpSrvr.close()




def main():
    parser = argparse.ArgumentParser(
        description="TCP Server",
        usage="udpSrvr [Lhost] [Lport]"
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

