import socket
import settings
import control
import signal
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = None
s.bind((settings.HOST, settings.PORT))
print "Listening on %s, port %s" % (settings.HOST, settings.PORT)
print "To quit, press CTRL+C"

def signal_handler(signal, frame):
    global s
    global client

    print "Exiting Gracefully"

    if client:
        client.close()
    if s:
        s.close()

    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while(1):
    s.listen(1)
    [client,addr] = s.accept()
    control.start_control(client)
s.close()

