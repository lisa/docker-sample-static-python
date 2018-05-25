# os.execv example for Static Python Container

Dockerfile copies python parts, including the [entrypoint.py](./entrypoint.py) file to the image. Build this:

    docker build -t sample-python-app-execv:1.0.0 .

Run:

    # Run the pre-built
		docker run thedoh/sample-python-app-execv:1.0.0

    # Or the one you built yourself
    docker run sample-python-app-execv:1.0.0

## Program Flow

1. Docker starts this image
2. CMD calls `/python -s -S /entrypoint.py`
3. `entrypoint.py` uses `os.execv` to make `/python -s -S /myapp.py` the running process (See execv(2))
4. Execution begins from within `myapp.py`, being executed by `/python` (the static binary)
