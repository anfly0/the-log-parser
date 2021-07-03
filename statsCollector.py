import transaction
import stats


class StatsCollector:
    def __init__(self):
        self.stats = {}

    def add_transaction(self, t: transaction.Transaction):
        if t.get_name() not in self.stats:
            self.stats[t.get_name()] = stats.Stats(t.get_name())

        self.stats[t.get_name()].add_transaction(t)
