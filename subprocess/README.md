# subprocess.call example for Static Python Container

Dockerfile copies python parts, including the [entrypoint.py](./entrypoint.py) file to the image. Build this:

    docker build -t sample-python-app-subprocess:1.0.0 .

Run:

    # Prebuilt version

    docker run thedoh/sample-python-app-subprocess:1.0.0

    # Build it yourself version

    docker run sample-python-app-subprocess:1.0.0

## Program Flow

1. Docker starts this image
2. CMD calls `/python -s -S /entrypoint.py`
3. `entrypoint.py` uses `subprocess.call to call `/python -s -S /myapp.py` as a sub-process (ie, child process of pid 1)
4. Execution begins from within `myapp.py`, being executed by `/python` (the static binary)
5. When `myapp.py` finishes running then execution is returned to `entrypoint.py` just after the `subprocess.call` line.
