"""
# simple TCP client
import socket

target_host = "www.google.com"
target_port = 80

#Creating a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the client
client.connect((target_host,target_port))

#send data with the client
client.send(b"GET / HTTP / 1.1\r\nHOST:google.com\r\n\r\n")

#Client recieves response
response = client.recv(4096)

print(response)

client.close()
"""

import sys
import socket
import signal
import argparse

def tcpClient(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client.connect((host,port))
    data = (f"GET / HTTP 1.1 \r\n HOST: {host} \r\n\r\n").encode()
    client.send(data)
    
    print(client.recv(4096).decode())
    client.close()

    return



def hndlCtrlC(signum, ctrlC):
    print("\nCTRL+C detected, closing cleanly")
    sys.exit(0)

signal.signal(signal.SIGINT, hndlCtrlC)




def main():
    parser = argparse.ArgumentParser(
        description = "TCP client",
        usage="tcpClient [host] [port]"
    )

    parser.add_argument('host', help="Host to connect to")
    parser.add_argument('port', help='Port to connect on')


    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()

    tcpClient(args.host, int(args.port))


if __name__ == "__main__":
    main()

