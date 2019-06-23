import logging
from datetime import timedelta

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from pomodoro.ui import MainWindow


def get_logger():
    logger = logging.getLogger('pomodoro')
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


logger = get_logger()


def main():
    logger.info('Creating an intance of MainWindow')
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    logger.info('Launching')
    win.show_all()
    Gtk.main()
    logger.info('All done')