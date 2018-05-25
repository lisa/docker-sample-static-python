# Sample Python Apps for Static Python Image

Various ways to use the [static python container](https://github.com/lisa/static-binaries/tree/update-python-version/python). The base image expects the user to provide a file called `entrypoint.py` to be called by the Docker `CMD`. This repository provides some examples of how to use that interface.

## os.execv style
See the [execv](./execv) directory for components and usage notes.

This uses the `os.execv` Python method to access the underlying [execv(3)](https://linux.die.net/man/3/execv) syscall with the goal of the actual program running with pid 1.

## subprocess style
See the [subprocess](./subprocess) directory for components  and usage notes.

In this example, however, the [subprocess Python module](https://docs.python.org/2/library/subprocess.html) is used to create a subprocess for the actual program, usually running as pid 5 as a child of pid 1.


## factory style
See the [factor](./factoru) directory for compnents and usage notes.

The "factory" example is more complete and representative of a "real" Flask application. This example makes use of the [psutil](https://github.com/giampaolo/psutil) Python module that has been compiled into the base image's Python binary (and library .zip file). The example uses a `requirements.txt` file and [pip](https://pip.pypa.io/en/stable/) to install Flask.

The base image _does not_ have the `pip` binary because the goal is to be minimal, so how is `pip install` done? It is done by using an intermediate Python image which comes with `pip`.

The `entrypoint.py` (loosely) uses a factory pattern to create an object for the Flask application prior to running it.
