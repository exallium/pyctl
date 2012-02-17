import socket
import settings
import control

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((settings.HOST, settings.PORT))

s.listen(1)
[client,addr] = s.accept()

control.start_control(client)

s.close()
