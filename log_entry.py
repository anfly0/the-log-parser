import datetime


class LogEntry:
    def __init__(self, rawLogEntry: str):
        self.raw = rawLogEntry
        self.parse()

    def parse(self):
        self.parts = self.raw.split()
        self.parse_time()
        self.parse_level()
        self.parse_name()
        self.parse_type()
        self.parse_id()

    def parse_time(self):
        day = self.parts[0]
        time = self.parts[1]
        self.dt = datetime.datetime.strptime(day + " " + time, "%Y-%m-%d %H:%M:%S,%f")

    def parse_level(self):
        self.level = self.parts[2][:-1]

    def parse_name(self):
        self.name = self.parts[3][1:-1]

    def parse_id(self):
        self.id = self.parts[4][1:-2]

    def parse_type(self):
        self.type = self.parts[-1]

    def is_start(self) -> bool:
        return self.type == "Start"

    def is_failed(self) -> bool:
        return self.type == "Failed"
    

    def __str__(self):
        return f'{self.dt} {self.level} {self.name} {self.id} {self.type}'
