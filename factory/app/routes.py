import os

from app import app
import psutil


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World from pid %d\n" % os.getpid()


@app.route('/cpus')
def cpus():
    return "Demonstrating psutil (which is statically compiled into the python binary) by running with %d CPUs!\n" % psutil.cpu_count()
