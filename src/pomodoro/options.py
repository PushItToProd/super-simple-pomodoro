"""
Define an object used for common configuration options.
"""
from dataclasses import dataclass, field
from typing import List

from pomodoro import defaults


@dataclass
class TimerOption:
    """
    Configure a timer button.
    """
    label: str
    minutes: int
    is_work: bool

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


def get_default_times() -> List[TimerOptionGroup]:
    return [
        TimerOptionGroup([
            TimerOption("Work", 25, True),
            TimerOption("Break", 5, False),
            TimerOption("Long Break", 30, False),
        ]),
        TimerOptionGroup([
            TimerOption("Work", 15, True),
            TimerOption("Break", 3, False),
            TimerOption("Long Break", 20, False),
        ]),
    ]


@dataclass
class PomodoroOptions:
    window_title: str = defaults.WINDOW_TITLE
    startup_message: str = defaults.STARTUP_MESSAGE
    label_font: str = defaults.LABEL_FONT

    done_sound: str = defaults.DONE_SOUND
    start_sound: str = defaults.START_SOUND

    times: List[TimerOptionGroup] = field(default_factory=get_default_times)
