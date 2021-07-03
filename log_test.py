import ingestor
import statsCollector
import report
import cli

try:
    log_file = cli.file_from_arg()
    i = ingestor.TransactionLogIngestor(log_file)
except IndexError:
    i = ingestor.TransactionLogIngestor()


collector = statsCollector.StatsCollector()

r = report.Report(collector, i)
for t in i.run():
    collector.add_transaction(t)
    if i.count % 2700 == 0:
        r.cli_report()


r.cli_report()
