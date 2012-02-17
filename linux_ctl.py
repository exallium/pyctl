import os
from subprocess import check_output
from settings import TAP_ACTIONS

def get_windowsize():
    dim = check_output(["/usr/bin/xdotool", "getdisplaygeometry"])
    return dim.split(' ')

def type_keys(string):
    os.system("xdotool type \"%s\"" % " ".join(string))

def click_mouse(button):
    os.system("xdotool click %s" % TAP_ACTIONS[int(button[0])])

size = get_windowsize()
def move_mouse(args):
    if args[0] == 'relative':
        comm = 'mousemove_relative'
    else:
        comm = 'mousemove'

    x = float(args[1]) * float(size[0])
    y = float(args[2]) * float(size[1])
    os.system('xdotool %s -- %s %s' % (comm, x, y))
