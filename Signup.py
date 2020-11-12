import os
import socket
import hashlib
import argparse

authcheck = socket.socket()

parser = argparse.ArgumentParser()
parser.add_argument('-http', '-site', '-s', help='Site To Connect To', required=True)
parser.add_argument('--auth', help='Enter Authentication Key', required=True)
parser.add_argument('--authfile', help='Enter File With Auth Key', required=True)
parser.add_argument('--authserver', help='Enter Authentication Server', required=True)
args = parser.parse_args()

site = args.http

hostname = socket.gethostname()
auth = args.auth
authfile = args.authfile
authserv = args.authserver

print("Hostname : " + hostname)
print('Connecting to secure server')
print('Securing Hash')
try:
    try:
        print('Authing Ngrock, and checking Server, connecting to ' + str(authserv))
        authcheck.settimeout(5)
        authcheck.connect((str(authserv), 80))
        print('Connection Stable, Connecting!')
    except:
        print('Connection Failed')
        exit()
    print('Authenticating Key: ' + auth)
    hosttosock = hashlib.md5(auth.encode("UTF-8")).hexdigest()
    with open(str(authfile), 'r') as f:
        hashsocket = f.read()
    hashsock2 = hashlib.md5(hashsocket.encode("UTF-8")).hexdigest()
    if hashsock2 != hosttosock:
        print('Failed To Authenticate')
    else:
        print('Connecting!')
        print('Connecting To ' + site)
        os.system('firefox ' + str(site) + '--tab')
        os.system('firefox ' + str(site) + '--tab')
except:
    print('Failed to secure connection, terminating so data is not compromised')