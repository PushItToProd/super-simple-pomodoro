from datetime import timedelta

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject


STARTUP_MESSAGE = "Pomodoro Timer"
LABEL_FONT = "44"


class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Pomodoro timer")
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

    def set_label(self, message):
        self.label.set_markup(f'<span font="{LABEL_FONT}">{message}</span>')

    def box_add(self, widget, padding=0):
        self.box.pack_start(widget, True, True, padding)

    def add_button(self, label, callback):
        button = Gtk.Button(label=label)
        button.connect("clicked", callback)
        # self.box_add(button)
        self.button_box.pack_start(button, True, True, 0)
        return button

    def work_clicked(self):
        pass

    def break_clicked(self):
        pass

    def long_break_clicked(self):
        pass

    def stop_clicked(self):
        pass


if __name__ == "__main__":
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()