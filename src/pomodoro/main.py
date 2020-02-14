"""
Entrypoint for the app. Handles options and starts the GUI.
"""
import argparse
import logging
import os

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from pomodoro import defaults
from pomodoro.ui import MainWindow
from pomodoro.options import PomodoroOptions


DESCRIPTION = 'A simple Pomodoro timer.'
DEFAULT_WORK_DURATION = \
    os.environ.get('POMODORO_WORK_DURATION', defaults.WORK_DURATION)
DEFAULT_BREAK_DURATION = \
    os.environ.get('POMODORO_BREAK_DURATION', defaults.BREAK_DURATION)
DEFAULT_LONG_BREAK_DURATION = \
    os.environ.get('POMODORO_LONG_BREAK_DURATION', defaults.LONG_BREAK_DURATION)
LOG_LEVEL = getattr(logging, os.environ.get('LOG_LEVEL', default='ERROR'))


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


def get_parser():
    """
    Generate command line argument parser.
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        '-w', '--work-duration', '--work', type=int,
        default=DEFAULT_WORK_DURATION,
        help='Duration of work intervals in minutes',
    )
    parser.add_argument(
        '-b', '--break-duration', '--break', type=int,
        default=DEFAULT_BREAK_DURATION,
        help='Duration of normal breaks in minutes',
    )
    parser.add_argument(
        '-l', '--long-break-duration', '--long-break', type=int,
        default=DEFAULT_LONG_BREAK_DURATION,
        help='Duration of long breaks in minutes',
    )
    return parser


def main():
    """Entrypoint for the application."""
    # set up root logger
    _ = get_logger()
    logger = logging.getLogger(__name__)

    parser = get_parser()
    # options = parser.parse_args(namespace=PomodoroOptions())
    options = PomodoroOptions()
    logger.debug('Starting with options %s', options)

    logger.info('Creating an instance of MainWindow')
    win = MainWindow(options)
    win.connect("destroy", Gtk.main_quit)

    logger.info('Launching')
    win.show_all()
    Gtk.main()

    logger.info('All done')
