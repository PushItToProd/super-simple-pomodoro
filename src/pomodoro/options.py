"""
Define an object used for common configuration options.
"""
from dataclasses import dataclass

from pomodoro import defaults


@dataclass
class PomodoroOptions:
    window_title: str = defaults.WINDOW_TITLE
    startup_message: str = defaults.STARTUP_MESSAGE
    label_font: str = defaults.LABEL_FONT

    done_sound: str = defaults.DONE_SOUND
    start_sound: str = defaults.START_SOUND

    work_duration: int = defaults.WORK_DURATION
    break_duration: int = defaults.BREAK_DURATION
    long_break_duration: int = defaults.LONG_BREAK_DURATION

    @property
    def work_duration_seconds(self):
        return self.work_duration * 60

    @property
    def break_duration_seconds(self):
        return self.break_duration * 60

    @property
    def long_break_duration_seconds(self):
        return self.long_break_duration * 60
