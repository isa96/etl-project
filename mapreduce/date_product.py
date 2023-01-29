#!/usr/bin/python3

from mrjob.job import MRJob

class ProductTrend(MRJob):
    def mapper(self, key, line):
        (transaction, customer, date, product, quantity) = line.split(',')
        if date != 'date_transaction': 
            yield date, int(quantity)
    def reducer(self, date, quantity):
        yield date, sum(quantity)

if __name__ == '__main__':
    ProductTrend.run()