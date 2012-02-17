# PyCTL -- Mouse Control via Python for Linux

## USAGE:

:::shell
$ python2 pyctl.py

## Click Commands

* All generalized to one function called click\_mouse
* Simply put, the only argument in the list is which button was
* pressed.  Currently this is a raw number, but will eventually be defined in a
  dict where we send the key and the script knows what value to use.


## Movement commands

* Movement can either be relative or absolute given the first argument in the
  function.
* this argument MUST be present but will default to absolute if not relative.
