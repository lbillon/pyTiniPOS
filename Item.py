'''
Created on Feb 1, 2012

@author: lbillon
'''

class Item(object):



    def __init__(self, name, identifier, price):
        if len(identifier) != 1 or not identifier.isalpha():
            raise ValueError('Item identifier length must be a single letter.')


        self.name = str(name)
        self.identifier = str(identifier)
        self.price = float(price)

    def toString(self):
        return '{}({}):{:.2f}'.format(self.name, self.identifier, self.price)

