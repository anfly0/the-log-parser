import statsCollector
import ingestor
import stats
import cli
import os


class Report:
    def __init__(self, collector: statsCollector.StatsCollector, ingest: ingestor.TransactionLogIngestor):
        self.collector = collector
        self.ingestor = ingest

    def cli_report(self):
        cli.clear()
        cli.text_color(cli.colors.HEADER)
        print(f'Ingesting {self.ingestor.logFile.name}@~{self.ingestor.get_perf_stat():.2f} lines/sec')
        cli.text_color(cli.colors.OKCYAN)
        print(self.top_five())
        cli.text_color(cli.colors.HEADER)
        print(self.test_results())

    def prc_too_low(self, stat) -> bool:
        return stat.get_prc_at_slow_bound() < 90

    def failure_rate_too_hight(self, stat) -> bool:
        return stat.get_failure_rate() > 0.05

    def test_stat(self, stat: stats.Stats) -> str:
        result = ""
        color = cli.colors.OKGREEN
        if self.prc_too_low(stat):
            color = cli.colors.FAIL
            result += f'P90 duration is above {stat.slow_bound}'

        if self.failure_rate_too_hight(stat):
            color = cli.colors.FAIL
            if result != "":
                result += " and "
            result += "failure rate is higher than 0.05%"

        return f'{color}{stat} | {result}'

    def top_five(self):
        stats_list = list(self.collector.stats.values())
        stats_list.sort(key=lambda x: x.total_duration, reverse=True)
        stats_str = "Top five transactions by cumulative duration" + os.linesep
        for st in stats_list[:5]:
            stats_str += f'{st.name} {st.total_duration:.3f} sec {os.linesep}'
        return stats_str

    def test_results(self):
        stats_list = list(self.collector.stats.values())
        stats_str = "Test results:" + os.linesep
        for st in stats_list:
            stats_str += self.test_stat(st) + os.linesep
        return stats_str



