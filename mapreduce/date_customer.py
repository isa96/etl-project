#!/usr/bin/python3

from mrjob.job import MRJob
from mrjob.step import MRStep

class CustomerTrend(MRJob):
    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer), MRStep(mapper=self.separator, reducer=self.counter)]
    def mapper(self, key, line):
        (transaction, customer, date, product, quantity) = line.split(',')
        if date != 'date_transaction': 
            yield (date, customer), 1
    def reducer(self, date_customer, count):
        yield date_customer, sum(count)
    def separator(self, date_customer, _):
        yield date_customer[0], 1
    def counter(self, year, count):
        yield year, sum(count)

if __name__ == '__main__':
    CustomerTrend.run()