import log_entry


class Transaction:
    def __init__(self, entry: log_entry.LogEntry):
        if not entry.is_start():
            raise Exception("This is not the start of a transaction!")

        self.start = entry
        self.open = True

    def end(self, entry: log_entry.LogEntry):
        if self.start.id != entry.id:
            raise Exception("Transaction id does not match!")
        self.end = entry
        self.open = False

    def get_duration(self) -> float:
        diff = self.end.dt - self.start.dt
        return diff.total_seconds()

    def is_failed(self) -> bool:
        return self.end.is_failed()

    def get_name(self) -> str:
        return self.start.name

    def is_open(self) -> bool:
        return self.open
