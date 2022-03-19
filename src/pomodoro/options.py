"""
Define an object used for common configuration options.
"""
from dataclasses import dataclass, field
from typing import List


class Defaults:
    WINDOW_TITLE = "Pomodoro Timer"
    STARTUP_MESSAGE = "Pomodoro Timer"
    LABEL_FONT = "44"
    SOUND_PATH = "/usr/share/sounds/ubuntu/notifications"
    DONE_SOUND = f"{SOUND_PATH}/Amsterdam.ogg"
    START_SOUND = f"{SOUND_PATH}/Rhodes.ogg"

    WORK_DURATION = 15
    BREAK_DURATION = 3
    LONG_BREAK_DURATION = 20


defaults = Defaults()


def get_default_times() -> 'List[TimerOptionGroup]':
    """
    Default factory for PomodoroOptions.times.
    """
    return [
        TimerOptionGroup([
            TimerOption("Work", 25, True, 'w'),
            TimerOption("Break", 5, False, 'b'),
            TimerOption("Long Break", 30, False, 'l'),
        ]),
        TimerOptionGroup([
            TimerOption("Work", 15, True, 'W'),
            TimerOption("Break", 3, False, 'B'),
            TimerOption("Long Break", 20, False, 'L'),
        ]),
    ]


@dataclass
class TimerOption:
    """
    Configure a timer button.
    """
    label: str
    minutes: int
    is_work: bool
    key: str = None

    @property
    def seconds(self):
        """
        Get timer duration in seconds.
        """
        return self.minutes * 60


@dataclass
class TimerOptionGroup:
    """
    A set of timings to display in a row.
    """
    times: List[TimerOption]


@dataclass
class PomodoroOptions:
    """
    Configuration for the Pomodoro app.
    """
    window_title: str = defaults.WINDOW_TITLE
    startup_message: str = defaults.STARTUP_MESSAGE
    label_font: str = defaults.LABEL_FONT

    done_sound: str = defaults.DONE_SOUND
    start_sound: str = defaults.START_SOUND

    times: List[TimerOptionGroup] = field(default_factory=get_default_times)
