"""
GUI definitions for pomodoro.
"""
import logging
from enum import Enum

import gi

from pomodoro.options import PomodoroOptions

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from playsound import playsound

from pomodoro.timer import Timer


class State(Enum):
    """Enumeration of the possible timer states."""
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
            orientation=Gtk.Orientation.VERTICAL, spacing=10
        )
        self.add(self.main_box)

        self.label = Gtk.Label()
        self.set_label(self.options.startup_message)
        self.main_box_add(self.label)

        self.state_label = Gtk.Label()
        self.set_timer_state(State.stopped)
        self.main_box_add(self.state_label)

        self.button_rows = []

    def set_label(self, message):
        """
        Update the main label.
        """
        self.label.set_markup(
            f'<span font="{self.options.label_font}">{message}</span>')

    def set_timer_state(self, state: State):
        """
        Set the timer state label.
        """
        self.state_label.set_label(state.value)

    def main_box_add(self, widget, padding=0):
        """
        Add an element to the main vertical box.
        """
        self.main_box.pack_start(widget, True, True, padding)

    def add_button_row(self):
        """
        Add a new button box to the window for a new row of buttons.
        """
        box = Gtk.Box(spacing=6)
        self.button_rows.append(box)
        self.main_box_add(box)

    def add_button(self, label, on_click, row=-1):
        """
        Add a button to the button box at the bottom of the window.

        :arg label: The label to put on the button.
        :arg on_click: The callback to invoke when the button is clicked.
        :arg row: The button row to add to. By default this is the last row.
        :return: The created button object.
        """
        button = Gtk.Button(label=label)
        button.connect("clicked", on_click)
        self.button_rows[row].pack_start(button, True, True, 0)
        return button


class MainWindow(BigLabelButtonWindow):
    """
    Definition of the actual pomodoro timer window.
    """
    def __init__(self, options: PomodoroOptions):
        super().__init__(options)
        self.logger.info('MainWindow: initializing')

        for group in options.times:
            self.add_button_row()
            for opt in group.times:
                self.add_button(
                    f"{opt.label} ({opt.minutes})",
                    self.get_button_callback(opt.seconds, opt.is_work)
                )

        self.add_button_row()
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
        self.set_timer_state(State.stopped)
        playsound(self.options.done_sound)

    def start_timer(self, duration, state):
        """
        Start the timer object.

        Args:
            duration: Time in seconds.
        """
        assert duration > 0, "can't start timer with zero/negative time!"
        self.timer.emit("start", duration)
        self.set_timer_state(state)
        playsound(self.options.start_sound)

    def stop_timer(self):
        """
        Stop the timer object.
        """
        self.set_timer_state(State.stopped)
        self.timer.emit("done")

    def get_button_callback(self, duration: int, is_work: bool):
        """
        Generate a callback for a timer button object.
        :param duration: The duration of the timer in seconds.
        :param is_work: If true, the button will start a working state.
            Otherwise, it will start a break state.
        :return: The generated callback function.
        """
        def callback(widget):
            _ = widget
            self.logger.info("button callback called")
            state = State.working if is_work else State.break_time
            self.start_timer(duration, state)
        return callback

    def stop_clicked(self, widget):
        """
        Handler for Stop button click events.
        """
        _ = widget
        self.logger.info("stop_clicked: Stop button clicked")
        self.stop_timer()
