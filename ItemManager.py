'''
Created on Feb 1, 2012

@author: lbillon
'''
import Item
import pickle

class ItemManager(object):


    def __init__(self):
        self.items = {}

    def saveToFile(self, fileName):
        f = open(fileName, "w")
        pickle.dump(self.items, f)

    def loadFromFile(self, fileName):
        f = open(fileName, "r")
        self.items = pickle.load(f)















