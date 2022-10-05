########################################################
# TRAINING
# https://www.youtube.com/watch?v=7utwZYKweho
# 1:42:18 - Sockets
# Further reading:
# Kali Linux
# Netcat
# For app below nc -nvlp 7777 --> opening up a listner on a port
# See below for some fun exercises & documentation
########################################################


########################################################
print("\n" + "### Sockets ###" + "\n")
import socket
HOST = '127.0.01' #my local machine
#TCP - 65,535 available ports
#common ports and protocols - 80 web server over http, 443 https, 21 ftp
PORT = 7777 #non-common (non-standard) port for connection test
#af_inet is ipv4 and sock_stream is a port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #variable because we do not want to type this all the time
s.connect((HOST,PORT))