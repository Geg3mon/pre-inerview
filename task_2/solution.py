from dataclasses import dataclass
import datetime
import json


@dataclass
class Todo:
    todo: str
    time_started: str = str(
        datetime.datetime.now().isoformat(sep=" ", timespec="days"))
    time_finished: str = ''
    status: str = 'in progress'
