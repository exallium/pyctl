import os
import sys

from subprocess import check_output
from settings import TAP_ACTIONS

if sys.platform == 'linux':
    from linux_ctl import *
elif sys.platform == 'darwin':
    from mac_ctl import *
else:
    from win_ctl import *

def start_control(client):
    comm = { 'click': click_mouse, 
             'move' : move_mouse,
             'type' : type_keys,}

    data = ['']
    while(data[0] != 'exit'):
        data = client.recv(1024).split(' ')
        if len(data) > 1:
            try:
                comm[data[0]](data[1:len(data)])
            except:
                pass
    return
