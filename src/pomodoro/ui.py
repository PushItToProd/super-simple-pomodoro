"""
GUI definitions for pomodoro.
"""
import logging

import gi

from pomodoro.options import PomodoroOptions

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from playsound import playsound

from pomodoro.timer import Timer


class State:
    stopped = ""
    working = "Working"
    break_time = "Break Time"


class BigLabelButtonWindow(Gtk.Window):
    """
    Base class for the pomodoro timer window.

    This class is kept separate to separate presentation from logic.
    """
    logger = logging.getLogger('pomodoro.ui')

    def __init__(self, options: PomodoroOptions):
        self.options = options
        self.title = options.window_title
        self.startup_message = options.startup_message

        Gtk.Window.__init__(self, title=self.title)
        self.logger.info('BigLabelButtonWindow: initializing')

        self.set_type_hint(Gdk.WindowTypeHint.DIALOG)
        self.set_border_width(25)

        self.main_box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.main_box)

        self.label = Gtk.Label()
        self.set_label(self.options.startup_message)
        self.main_box_add(self.label)

        self.state_label = Gtk.Label()
        self.state = ""
        self.set_state("")
        self.main_box_add(self.state_label)

        self.button_box = Gtk.Box(spacing=6)
        self.main_box_add(self.button_box)

    def set_label(self, message):
        """
        Update the main label.
        """
        self.label.set_markup(
            f'<span font="{self.options.label_font}">{message}</span>')

    def set_state(self, state):
        self.state = state
        self.state_label.set_label(self.state)

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
    def __init__(self, options: PomodoroOptions):
        super().__init__(options)
        self.logger.info('MainWindow: initializing')

        self.work_button = self.add_button(
            f"Work ({options.work_duration})", self.work_clicked
        )
        self.break_button = self.add_button(
            f"Break ({options.break_duration})", self.break_clicked
        )
        self.long_break_button = self.add_button(
            f"Long Break ({options.long_break_duration})",
            self.long_break_clicked
        )
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
        self.set_state(State.stopped)
        playsound(self.options.done_sound)

    def start_timer(self, duration, state):
        """
        Start the timer object.

        Args:
            duration: Time in seconds.
        """
        assert duration > 0, "can't start timer with zero/negative time!"
        self.timer.emit("start", duration)
        self.set_state(state)
        playsound(self.options.start_sound)

    def stop_timer(self):
        """
        Stop the timer object.
        """
        self.set_state(State.stopped)
        self.timer.emit("done")

    def work_clicked(self, widget):
        """
        Handler for Work button click events.
        """
        _ = widget
        self.logger.info("work_clicked: Work button clicked")
        self.start_timer(self.options.work_duration_seconds, State.working)

    def break_clicked(self, widget):
        """
        Handler for Break button click events.
        """
        _ = widget
        self.logger.info("break_clicked: Break button clicked")
        self.start_timer(self.options.break_duration_seconds, State.break_time)

    def long_break_clicked(self, widget):
        """
        Handler for Long Break button click events.
        """
        _ = widget
        self.logger.info("long_break_clicked: Long Break button clicked")
        self.start_timer(self.options.long_break_duration_seconds,
                         State.break_time)

    def stop_clicked(self, widget):
        """
        Handler for Stop button click events.
        """
        _ = widget
        self.logger.info("stop_clicked: Stop button clicked")
        self.stop_timer()
