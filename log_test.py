import ingestor
import statsCollector
import report

collector = statsCollector.StatsCollector()
i = ingestor.TransactionLogIngestor()
r = report.Report(collector, i)
for t in i.run():
    collector.add_transaction(t)
    if i.count % 2700 == 0:
        r.cli_report()


r.cli_report()







