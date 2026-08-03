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

def tcpClient(host):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client.connect((host,80))
    data = (f"GET / HTTP 1.1 \r\n HOST: {host} \r\n\r\n").encode()
    client.send(data)
    
    print(client.recv(4096))
    client.close()

    return



def hndlCtrlC(signum, ctrlC):
    print("\nCTRL+C detected, closing cleanly")
    sys.exit(0)

signal.signal(signal.SIGINT, hndlCtrlC)




def main():
    parser = argparse.ArgumentParser(
        description = "TCP clinet",
        usage="tcpClient [host]"
    )

    parser.add_argument('host', help="Host to connect to")


    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    arg = parser.parse_args()

    tcpClient(arg.host)


if __name__ == "__main__":
    main()

