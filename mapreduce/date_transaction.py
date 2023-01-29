#!/usr/bin/python3

from mrjob.job import MRJob
from mrjob.step import MRStep

class TransactionTrend(MRJob):
    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer), MRStep(mapper=self.separator, reducer=self.counter)]
    def mapper(self, key, line):
        (transaction, customer, date, product, quantity) = line.split(',')
        if date != 'date_transaction':
            yield (date, transaction), 1
    def reducer(self, date_transaction, count):
        yield date_transaction, sum(count)
    def separator(self, date_transaction, _):
        yield date_transaction[0], 1
    def counter(self, year, count):
        yield year, sum(count)

if __name__ == '__main__':
    TransactionTrend.run()