from enum import Enum


class WorkMode(Enum):
    EFFICIENT = 60  # one minute
    MODERATE = 5 * 60  # 5 minutes
    LAZY = 30 * 60  # 30 minutes

    @staticmethod
    def get_text(work_mode):
        if work_mode == WorkMode.EFFICIENT:
            return "1 minute"
        if work_mode == WorkMode.MODERATE:
            return "5 minutes"
        if work_mode == WorkMode.LAZY:
            return "30 minutes"
