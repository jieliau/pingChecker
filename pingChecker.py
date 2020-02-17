import getopt
import sys
import platform
import subprocess
import threading
import time

def usage():
    print(
    '''
Usage: pingChecker.py -f [text file]
or use pingChecker.py -h ot --help to print this message
''')

args = sys.argv[1:]

# '-h -o file --help --output=out file1 file2'
# opts = [('-h', ''), ('-c', 'file'), ('--help', ''), ('--output', 'out')]
# args = ['file1', 'file2']

try:
    opts, args = getopt.getopt(args, 'hf:', ['help'])
except getopt.GetoptError:
    usage()
    sys.exit(1)

if not opts:
    usage()
    sys.exit(1)

for opt, arg in opts:
    if opt in ('-h', '--help'):
        usage()
        sys.exit(1)
    if opt in ('-f'):
        ipfile = arg

def ping(host):
    '''
    Return True if host (str) responds to a ping request.
    '''
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    if subprocess.call(command, stdout=open('/dev/null', 'w'), stderr=open('/dev/null', 'w')) == 0:
        print(host.strip("\n") + "\tis ok")
    else:
        print(host.strip("\n") + "\tis unreachable")
    #return subprocess.call(command, stdout=open('/dev/null', 'w'), stderr=open('/dev/null', 'w')) == 0

def main():
    ips = list()
    #fp = open(ipfile, 'r')
    #for line in iter(fp):
    #    ips.append(line)
    #fp.close()
    with open(ipfile, "r") as fp:
        ips.append(fp.readlines())

    threads = list()
    for i in range(len(ips[0])):
        threads.append(threading.Thread(target = ping, args = (ips[0][i], )))
        threads[i].start()
    for i in range(len(ips)):
        threads[i].join()
    
    #for ip in ips:
    #    ping(ip)
    #    print(ip.strip('\n') + "\tis unreachable") if ping(ip) == 0 else print(ip.strip('\n') + "\tis ok")

if __name__ == '__main__':
    main()

