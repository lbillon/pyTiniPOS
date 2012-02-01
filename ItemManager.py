'''
Created on Feb 1, 2012

@author: lbillon
'''
import Item
import pickle

class ItemManager(object):
    __basketItems = {}
    __basketValue = 0
    availableItems = {}



    def __init__(self):
        pass

    def saveAvailableItemsToFile(self, fileName):
        f = open(fileName, "w")
        pickle.dump(self.availableItems, f)

    def loadAvailableItemsFromFile(self, fileName):
        f = open(fileName, "r")
        self.availableItems = pickle.load(f)

    def addItemToBasket(self, itemIdentifier):
        i = self.availableItems[itemIdentifier]
        if i in self.__basketItems:
                    self.__basketItems[i] = self.__basketItems[i] + 1
        else:
                    self.__basketItems[i] = 1
        self.__basketValue += i.price


    def getBasketItems(self):
        return self.__basketItems

    def getBasketValue(self):
        return self.__basketValue

    def pay(self, amount):
        self.__basketValue -= amount

    def createNewItem(self, item):
        if(item.name in self.availableItems):
            raise ValueError('Item identifier is already used.')
        self.availableItems[item.name] = item

    def newTransaction(self):
            self.__basketItems = {}
            self.__basketValue = 0

    def saveBasketToHistory(self):
        f = open("history.txt", "a")
        for item in self.__basketItems:
            f.write('{} * {} @ {} = {}\n'.format(self.__basketItems[item], item.name, item.price, item.price * self.__basketItems[item]))
        f.close()
