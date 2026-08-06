"""
# simple UDP client
import socket

target_host = "127.0.0.1"
target_port = 9997

# creating the socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data
client.sendto(b"AABBBCCC",(target_host,target_port))

# Recieve our data back
data, addr = client.recvfrom(4096)

print(data.decode())

client.close()
"""

import sys
import socket
import argparse


def udpClient(host, port):
    try:
        udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        udpClient.sendto(b"AAABBBCCC",(host,port))

        udpClient.settimeout(5)

        data, addr = udpClient.recvfrom(4096)
        
        print("[+]",data.decode())
        return True

    except Exception as err:
        print(f"[-] {err}")
        return False
    
    except KeyboardInterrupt:
        print("\n[-] KeyboardInterrupt detected, closing cleanly")
        return False

    finally:
        udpClient.close()




def udpMain():
    parser = argparse.ArgumentParser(
        description="UDP client",
        usage="udpClient [Rhost] [Rport]"
    )

    parser.add_argument('host', help="UDP Host to connect to")
    parser.add_argument('port', help="Port to connect on")

    if len(sys.argv) == 1 or len(sys.argv) == 2:
        parser.print_help()
        sys.exit(0)
    
    args = parser.parse_args()

    udpClient(args.host, int(args.port))

    return True




if __name__ == "__main__":
    udpMain()