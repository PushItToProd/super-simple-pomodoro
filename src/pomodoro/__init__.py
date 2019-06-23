"""
pomodoro is a super simple pomodoro timer.
"""
import logging
from datetime import timedelta

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from pomodoro.ui import MainWindow


def get_logger():
    """
    Generate root logger for pomodoro.
    """
    logger = logging.getLogger('pomodoro')
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


def main():
    """Entrypoint for the application."""
    logger = get_logger()
    logger.info('Creating an intance of MainWindow')
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    logger.info('Launching')
    win.show_all()
    Gtk.main()
    logger.info('All done')
