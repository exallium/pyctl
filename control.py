import os
from subprocess import check_output

def get_windowsize():
    dim = check_output(["/usr/bin/xdotool", "getdisplaygeometry"])
    return dim.split(' ')

def type_keys(string):
    os.system("xdotool type \"%s\"" % " ".join(string))

def click_mouse(button):
    os.system("xdotool click %s" % button[0])

size = get_windowsize()
def move_mouse(args):
    if args[0] == 'relative':
        comm = 'mousemove_relative'
    else:
        comm = 'mousemove'

    x = float(args[1]) * float(size[0])
    y = float(args[2]) * float(size[1])
    print x, y
    os.system('xdotool %s -- %s %s' % (comm, x, y))

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
