'''
Created on Feb 1, 2012

@author: lbillon
'''

class Item(object):



    def __init__(self, name, identifier, price):
        if len(identifier) != 1 or not identifier.isalpha():
            raise ValueError('Item identifier length must be a single letter.')


        self.__name = str(name)
        self.__identifier = str(identifier)
        self.__price = float(price)

    def toString(self):
        return '{}({}):{}'.format(self.__name, self.__identifier, self.__price)

