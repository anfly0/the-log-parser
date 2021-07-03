import transaction


class Stats:
    def __init__(self, transactionName: str):
        self.name = transactionName
        self.count = 0
        self.failed_count = 0
        self.slow_count = 0
        self.total_duration = 0
        self.slow_bound = 2

    def add_transaction(self, transaction: transaction.Transaction):
        if transaction.get_name() != self.name:
            raise Exception('Name did not match')

        if transaction.is_open():
            raise Exception("Can't add open transaction to stats")

        self.count += 1
        if transaction.is_failed():
            self.failed_count += 1

        if transaction.get_duration() >= self.slow_bound and not transaction.is_failed():
            self.slow_count += 1

        self.total_duration += transaction.get_duration()

    def get_failure_rate(self) -> float:
        return self.failed_count / self.count * 100

    def get_prc_at_slow_bound(self):
        if self.slow_count == 0:
            return 100
        else:
            return 100 - (self.slow_count / (self.count - self.failed_count) * 100)

    def __str__(self):
        return f'Name: {self.name:17} | Cumulative duration: {self.total_duration:.3f} sec | Failure rate: {self.get_failure_rate():.3f}% | PRC at {self.slow_bound} sec: {self.get_prc_at_slow_bound():8.3f}'
