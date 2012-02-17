#!/usr/bin/python2
# PyCTL Settings Config
import os
import sys

# Server Settings
HOST='0.0.0.0'
PORT=48000

# Mouse buttons
LEFT=1
MIDDLE=2
RIGHT=3
SCROLLUP=4
SCROLLDOWN=5

if os.name == "posix":
    if sys.platform == "linux":
        TAP_ACTIONS = (
                None,
                LEFT,
                RIGHT,
                MIDDLE,
            )
    elif sys.platform == "darwin":
        from Quartz.CoreGraphics import kCGMouseButtonLeft
        from Quartz.CoreGraphics import kCGMouseButtonRight
        TAP_ACTIONS = (
                None,
                kCGMouseButtonLeft,
                kCGMouseButtonRight,
                None,
            )


