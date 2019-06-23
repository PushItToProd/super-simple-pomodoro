super-simple-pomodoro
=====================

A very simple pomodoro timer built with Python and GTK.

Install
-------

Only tested under Ubuntu 18.04.

### System Dependencies

I don't actually know for sure which of these are needed because I didn't pay 
enough attention during setup. However, I'm pretty confident the following are
sufficient:

* Python 3.6 or better
* [PyGObject](https://pygobject.readthedocs.io/en/latest/getting_started.html#ubuntu-getting-started)
  * Outside of a virtualenv, `sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0`
  * In a virtualenv, `sudo apt install libgirepository1.0-dev gcc libcairo2-dev pkg-config python3-dev gir1.2-gtk-3.0`
