#! /usr/bin/env python

'''
Created on Feb 1, 2012

@author: lbillon
'''

if __name__ == '__main__':
    import sys
    import ItemManager, Item


    __im = ItemManager.ItemManager()

    def printUsage():
        print(
"Available commands:\n\
/+\t\tAdd new item definition\n\
/s filename\tSave item definitions to file\n\
/l filename\tLoad item definitions from file\n\
/h\t\tDisplay this help message\n\
\n\
Type a series of identifiers to register an order\n\
")

    def __exitProgram():
        print("terminating...")
        sys.exit()

    def __listItems():
        print("Available Items :")
        for i in __im.availableItems:
            print(__im.availableItems[i].toString())

    def __itemInput():
        print("Creating New Item")
        try:
            name = raw_input("Name? ")
            identifier = raw_input("Identifier? ")
            price = raw_input("Price? ")
            i = Item.Item(name, identifier, price)
            __im.createNewItem(i)
        except Exception, err:
            print err
            print("Item not created")


    def __parseInput(userInput):
        if userInput == "":
            printUsage()

        elif userInput == "/+":
            __itemInput();

        elif userInput == "/h":
            printUsage()

        elif userInput == "/i":
            __listItems();

        elif userInput.startswith("/s "):
            fileName = userInput.split(" ")[1]
            try:
                __im.saveAvailableItemsToFile(fileName)
                print("Saved item definitions to {}".format(fileName))
            except IOError, err:
                print err

        elif userInput.startswith("/l "):
            fileName = userInput.split(" ")[1]
            try:
                __im.loadAvailableItemsFromFile(fileName)
                print("Loaded item definitions from {}".format(fileName))
                __listItems()
            except IOError, err:
                print err

        elif userInput[0] == "/":
            print "Command invalid"

        else:
            __im.newTransaction()
            for c in userInput :
                try:
                    __im.addItemToBasket(c)
                except KeyError:
                    print 'The item {} doesn\'t exist'.format(c)
                    return 1
            print("Ordered Items: ")
            basketItems = __im.getBasketItems()
            for i in basketItems:
                print '{} x {} = {:.2f}'.format(basketItems[i], i.name, basketItems[i] * i.price)
            while (__im.getBasketValue() > 0):
                print("Yet to pay:\n{:.2f}".format(__im.getBasketValue()))
                collected = raw_input("Amount given: ")
                try:
                    collected = float(collected)
                    __im.pay(collected)

                except :
                    print("Transaction cancelled")
                    return 1
            print("Anount to return : {:.2f}".format(-__im.getBasketValue()))
            __im.saveBasketToHistory()
            print("Transaction committed\n")


    while(True):
        try:
            userInput = raw_input("# ");
        except:
            __exitProgram() ## We caught Ctrl + D

        __parseInput(userInput)
