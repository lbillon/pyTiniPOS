'''
Created on Feb 1, 2012

@author: lbillon
'''

class Item(object):



    def __init__(self, name, identifier, price):
        self.__name= name
        self.__identifier=identifier
        self.__price=price
        
    def toString(self):
        return '{}({}):{}'.format(self.__name,self.__identifier,self.__price)
        
