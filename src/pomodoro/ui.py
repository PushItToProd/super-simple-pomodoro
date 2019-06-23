"""
GUI definitions for pomodoro.
"""
import logging

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from playsound import playsound

from pomodoro.timer import Timer
from pomodoro import settings as config


class BigLabelButtonWindow(Gtk.Window):
    """
    Base class for the pomodoro timer window.

    This class is kept separate to separate presentation from logic.
    """
    logger = logging.getLogger('pomodoro.ui')

    def __init__(self, title, startup_message):
        self.title = title
        self.startup_message = startup_message

        Gtk.Window.__init__(self, title=title)
        self.logger.info('BigLabelButtonWindow: initializing')

        self.set_type_hint(Gdk.WindowTypeHint.DIALOG)
        self.set_border_width(25)

        self.main_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.main_box)

        self.label = Gtk.Label()
        self.set_label(startup_message)
        self.main_box_add(self.label)

        self.button_box = Gtk.Box(spacing=6)
        self.main_box_add(self.button_box)

    def set_label(self, message):
        """
        Update the main label.
        """
        self.label.set_markup(
            f'<span font="{config.LABEL_FONT}">{message}</span>')

    def main_box_add(self, widget, padding=0):
        """
        Add an element to the main vertical box.
        """
        self.main_box.pack_start(widget, True, True, padding)

    def add_button(self, label, callback):
        """
        Add a button to the button box at the bottom of the window.
        """
        button = Gtk.Button(label=label)
        button.connect("clicked", callback)
        self.button_box.pack_start(button, True, True, 0)
        return button


class MainWindow(BigLabelButtonWindow):
    """
    Definition of the actual pomodoro timer window.
    """
    def __init__(self):
        super().__init__(config.WINDOW_TITLE, config.STARTUP_MESSAGE)
        self.logger.info('MainWindow: initializing')

        self.work_button = self.add_button("Work", self.work_clicked)
        self.break_button = self.add_button("Break", self.break_clicked)
        self.long_break_button = self.add_button(
            "Long Break", self.long_break_clicked)
        self.stop_button = self.add_button("Stop", self.stop_clicked)

        self.timer = Timer()
        self.timer.connect("tick", self.on_timer_tick)
        self.timer.connect("done", self.on_timer_done)

    def on_timer_tick(self, timer, remaining):
        """
        Handler for timer tick signals.
        """
        _ = remaining
        self.set_label(str(timer))

    def on_timer_done(self, timer):
        """
        Handler for timer done signals.
        """
        _ = timer
        self.set_label("Done!")
        playsound(config.DONE_SOUND)

    def start_timer(self, duration):
        """
        Start the timer object.

        Args:
            duration: Time in seconds.
        """
        assert duration > 0, "can't start timer with zero/negative time!"
        self.timer.emit("start", duration)

    def work_clicked(self, widget):
        """
        Handler for Work button click events.
        """
        _ = widget
        self.logger.info("work_clicked: Work button clicked")
        self.start_timer(config.WORK_DURATION)

    def break_clicked(self, widget):
        """
        Handler for Break button click events.
        """
        _ = widget
        self.logger.info("break_clicked: Break button clicked")
        self.start_timer(config.BREAK_DURATION)

    def long_break_clicked(self, widget):
        """
        Handler for Long Break button click events.
        """
        _ = widget
        self.logger.info("long_break_clicked: Long Break button clicked")
        self.start_timer(config.LONG_BREAK_DURATION)

    def stop_clicked(self, widget):
        """
        Handler for Stop button click events.
        """
        _ = widget
        self.logger.info("stop_clicked: Stop button clicked")
        self.timer.emit('done')
