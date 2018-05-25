import sys
import os

# Add our application's path to Python's seach path so that it can find 
# `app` and `flask`.
sys.path.append("/usr/src/app")

# Change run directory (from `/`) to where our app lives `/usr/src/app` 
os.chdir("/usr/src/app")

from app import app

print "Running Flask with pid %d" % os.getpid()
app.run(
    debug=True,
    host='0.0.0.0'
    )

print "Resuming entrypoint.py with pid %d" % os.getpid()
