super-simple-pomodoro
=====================

A very simple pomodoro timer built with Python and GTK.

Install
-------

Only tested under Ubuntu 18.04.

### System Dependencies

Because the sounds used are hard-coded, this only works under Ubuntu at the
moment.

I don't actually know for sure which of these are needed because I didn't pay
enough attention during setup. However, I'm pretty confident the following are
sufficient:

* Python 3.6 or better
* [PyGObject](https://pygobject.readthedocs.io/en/latest/getting_started.html#ubuntu-getting-started)

### Install steps (development)

* Make sure the system dependencies are installed for virtualenv support.

  ```
  sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config \
    python3-dev gir1.2-gtk-3.0
  ```

* Create and activate a virtualenv with Python 3.6.

  ```
  python3.6 -m venv venv && source venv/bin/activate
  ```

* Install the package into the virtualenv.

  ```
  python setup.py install -e .
  ```

* Now the `pomodoro` command line script should be on your path. If you run it, 
  the Pomodoro Timer app should launch.

### Make `pomodoro` available everywhere

Create a symlink to the `pomodoro` script in a location that's on your path.
For example:

```
ln -sT /home/myuser/projects/super-simple-pomodoro/venv/bin/pomodoro ~/bin/pomodoro
```