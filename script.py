import sys

def lock():
    print ("Locking translations")


def unlock():
    print ("Unlocking translations")

if sys.argv[1] == 'lock':
    lock()
elif sys.argv[1] == 'unlock':
    unlock()
