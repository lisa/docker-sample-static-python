import sys
import os


os.chdir("/")
import subprocess

print "Passing off from %d" % os.getpid()

subprocess.call(["/python", "-s","-S","/myapp.py"])

print "Subprocess.call finished executing. Resuming execution with pid=%d" % os.getpid()

