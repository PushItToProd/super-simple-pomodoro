from datetime import timedelta

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

import logging


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


STARTUP_MESSAGE = "Pomodoro Timer"
LABEL_FONT = "44"


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Pomodoro timer")
        logger.info('MainWindow: initializing')
        self.set_type_hint(1)  # TODO: find the DIALOG constant
        self.set_border_width(25)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.box)

        self.label = Gtk.Label()
        self.set_label(STARTUP_MESSAGE)
        self.box_add(self.label)

        self.button_box = Gtk.Box(spacing=6)
        self.box_add(self.button_box)

        self.work_button = self.add_button("Work", self.work_clicked)
        self.break_button = self.add_button("Break", self.break_clicked)
        self.long_break_button = self.add_button(
            "Long Break", self.long_break_clicked)
        self.stop_button = self.add_button("Stop", self.stop_clicked)

        self.time_remaining = None

        GObject.timeout_add(1000, self.timer_tick)

    def set_label(self, message):
        self.label.set_markup(f'<span font="{LABEL_FONT}">{message}</span>')

    def box_add(self, widget, padding=0):
        self.box.pack_start(widget, True, True, padding)

    def add_button(self, label, callback):
        button = Gtk.Button(label=label)
        button.connect("clicked", callback)
        self.button_box.pack_start(button, True, True, 0)
        return button

    def timer_tick(self):
        if self.time_remaining is None:
            logger.debug("timer_tick: No timer running.")
            return True

    def work_clicked(self):
        logger.info("work_clicked: Work button clicked")
        pass

    def break_clicked(self):
        logger.info("break_clicked: Break button clicked")
        pass

    def long_break_clicked(self):
        logger.info("long_break_clicked: Long Break button clicked")
        pass

    def stop_clicked(self):
        logger.info("stop_clicked: Stop button clicked")
        pass


if __name__ == "__main__":
    logger.info('Creating an intance of MainWindow')
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    logger.info('Launching')
    win.show_all()
    Gtk.main()
    logger.info('All done')