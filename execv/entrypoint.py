import sys
import os


os.chdir("/")

print "Passing off from %d" % os.getpid()

os.execv("/python", ["-s","-S","/myapp.py"])

print "This should never display (unless os.execv failed)"

