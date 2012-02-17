import os

def click_mouse(button):
    os.system("xdotool click %s" % button[0])

def move_mouse(args):
    if args[0] == 'relative':
        comm = 'mousemove_relative'
    else:
        comm = 'mousemove'
    os.system('xdotool %s -- %s %s' % (comm, args[1], args[2]))

def start_control(client):
    comm = { 'click': click_mouse, 
             'move' : move_mouse }

    data = ['']
    while(data[0] != 'exit'):
        data = client.recv(1024).split(' ')
        if len(data) > 1:
            comm[data[0]](data[1:len(data)])
    return
