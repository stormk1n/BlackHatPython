import subprocess
import shlex
import argparse
import sys
import textwrap
import socket
import threading


def extCmd(cmd):
    cmd = cmd.strip()

    if not cmd:
        return
    
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()




def main():
    custom_formatter = lambda prog: argparse.HelpFormatter(prog, max_help_position=50, width=100)
    parser = argparse.ArgumentParser(
        description="Custom netcat tool",
        formatter_class=custom_formatter,
        epilog=textwrap.dedent('''EXAMPLE
            netcat.py -t 192.168.122.166 -p 5555 -l -c  # <-- Command shell
            netcat.py -t 192.168.122.166 -p 5555 -l -u=mytest.txt # <-- upload a file
            netcat.py -t 192.168.122.166 -p 5555 -l -e=\"cat /etc/passwd\" # <-- execute command
            echo "ABC" | ./netcat.py -t 192.168.122.166 -p 135 # <-- echo text to server port 135
        ''')
    )
    parser.add_argument("-c", '--command', action='store_true', help="command shell")
    parser.add_argument('-e', '--execute', help="execute specific command")
    parser.add_argument('-l', "--listen", action='store_true', help="listen")
    parser.add_argument("-t", '--target', default='0.0.0.0', help='specified ip address')
    parser.add_argument("-u", '--upload', help='upload a file')
    parser.add_argument('-p', '--port', type=int, default=5555, help='specified port')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()


if __name__ == "__main__":
    main()
