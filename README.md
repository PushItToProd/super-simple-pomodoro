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
    python3.7-dev gir1.2-gtk-3.0
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

License
-------

super-simple-pomodoro  
Copyright (C) 2019 pushittoprod.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.