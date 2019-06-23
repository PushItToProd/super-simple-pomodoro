"""
A timer utility for GTK.
"""
import logging

from gi.repository import GObject


class Timer(GObject.GObject):
    """
    A simple async timer object. When started, it counts down from the set
    time, signalling time remaining each second, and then signals done.
    """
    logger = logging.getLogger('pomodoro.timer')
    __gsignals__ = {
        'start': (GObject.SIGNAL_RUN_FIRST, None, (int,)),
        'tick': (GObject.SIGNAL_RUN_FIRST, None, (int,)),
        'done': (GObject.SIGNAL_RUN_FIRST, None, ()),
    }

    def __init__(self):
        GObject.GObject.__init__(self)
        self.remaining = None
        self.timeout = None

    def do_start(self, seconds):
        """
        Handler for the start signal, used both to start and initialize the
        timer.

        Args:
            seconds (int): Timer duration.
        """
        assert seconds > 0, "can't start timer with zero/negative time!"
        self.remaining = seconds
        if self.timeout is None:
            self.timeout = GObject.timeout_add(1000, self._timer_tick)
        self.emit('tick', seconds)

    def _timer_tick(self):
        if self.timeout is None:
            return False
        self.remaining -= 1
        if self.remaining <= 0:
            self.emit('done')
            return False
        self.emit('tick', self.remaining)
        return True

    def do_done(self):
        """
        Handler for the done signal, called when the timer ends.
        """
        self.logger.info("Timer.do_done - removing timeout")
        if self.timeout is not None and GObject.source_remove(self.timeout):
            self.timeout = None

    def __str__(self):
        minutes = self.remaining // 60
        seconds = self.remaining % 60
        return f"{minutes:02}:{seconds:02}"

    def __bool__(self):
        return self.remaining > 0
