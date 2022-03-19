"""
Entrypoint for the app. Handles options and starts the GUI.
"""
import logging
import os

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from pomodoro.ui import MainWindow
from pomodoro.options import PomodoroOptions, defaults


DESCRIPTION = 'A simple Pomodoro timer.'
DEFAULT_WORK_DURATION = \
    os.environ.get('POMODORO_WORK_DURATION', defaults.WORK_DURATION)
DEFAULT_BREAK_DURATION = \
    os.environ.get('POMODORO_BREAK_DURATION', defaults.BREAK_DURATION)
DEFAULT_LONG_BREAK_DURATION = \
    os.environ.get('POMODORO_LONG_BREAK_DURATION', defaults.LONG_BREAK_DURATION)
LOG_LEVEL = getattr(logging, os.environ.get('LOG_LEVEL', default='ERROR').upper())


def get_logger():
    """
    Generate root logger for pomodoro.
    """
    logger = logging.getLogger('pomodoro')
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    return logger


def main():
    """Entrypoint for the application."""
    # set up root logger
    _ = get_logger()
    logger = logging.getLogger(__name__)

    options = PomodoroOptions()
    logger.debug('Starting with options %s', options)

    logger.info('Creating an instance of MainWindow')
    win = MainWindow(options)
    win.connect("destroy", Gtk.main_quit)

    logger.info('Launching')
    win.show_all()
    Gtk.main()

    logger.info('All done')
