# Factory pattern example for Static Python Container

Dockerfile copies python parts, including the [entrypoint.py](./entrypoint.py) file to the image. Build this:

    docker build -t sample-python-app-factory:1.0.0 .

Run:

    # Prebuilt

    docker run -p 5000:5000 thedoh/sample-python-app-factory:1.0.0

    # The one built above

    docker run -p 5000:50000 -i sample-python-app-factory:1.0.0

In another terminal:

    curl http://localhost:5000/
    curl http://localhost:5000/cpus

## Program Flow

1. Docker starts this image
2. CMD calls `/python -s -S /entrypoint.py`
3. `entrypoint.py` imports the `app` local module to create an instance of a Flask application and then starts a webserver running on port 5000 backed by the `app` code module.
4. [app/routes.py](app/routes.py) installs three routes (`/`, `/index`, `/cpus`), each of which demonstrate a different thing.

### Routes

Each route shows off a different part of the demo to differentiate from other demos ([execv](../execv) and [subprocess](../subprocess)).

#### `/index` and `/`

The `/index` route (aka `/`) demonstrates that the process serving the result is different than the main webserver process. Note that upon startup the container will print its pid (aka `pid` 1). The HTTP response body from this route will print `pid` 5 (or something else). This is to highlight that this demo is not the same as the `execv` demo.

### `/cpus`

This route highlights that a third-party module (in this case, [psutil](https://github.com/giampaolo/psutil)) can be compiled into the base Python image. This is important because the `psutil` module comes with C code that would normally be compiled into a shared object library which the (`psutil`) Python code will `import` from within its source directory.

The module, version `5.4.5`, has been modified to support this (See the documentation in the static python base image).

The route returns the number of CPUs present for the container.

