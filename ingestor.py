import sys
import log_entry
import time
import transaction


class TransactionLogIngestor:
    def __init__(self, logFile=sys.stdin):
        self.logFile = logFile
        self.count = 0
        self.open_transactions = {}

    def run(self):
        self.start_time = time.perf_counter()
        for line in self.logFile:
            self.count += 1
            try:
                entry = log_entry.LogEntry(line)
            except Exception:
                # Skip the line if parsing fails
                continue

            if entry.is_start():
                self.open_transactions[entry.id] = transaction.Transaction(entry)
                continue

            if entry.id in self.open_transactions:
                t = self.open_transactions[entry.id]
                t.end(entry)
                yield t
                del self.open_transactions[entry.id]

    def get_perf_stat(self):
        lines_per_sec = self.count / (time.perf_counter() - self.start_time)
        self.count = 0
        self.start_time = time.perf_counter()
        return lines_per_sec
