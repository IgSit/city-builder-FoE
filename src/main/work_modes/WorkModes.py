from enum import Enum, auto


class WorkMode(Enum):
    EFFICIENT = 60  # one minute
    MODERATE = 5 * 60  # 5 minutes
    LAZY = 30 * 60  # 30 minutes
