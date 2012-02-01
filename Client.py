'''
Created on Feb 1, 2012

@author: lbillon
'''
from inspect import Traceback


def __listItems():
    print("Item List :")
    for i in __im.items:
        print(__im.items[i].toString())

def parseInput(userInput):
    if userInput == "/+":
        __itemInput();
    elif userInput == "/l":
        __listItems();
    elif userInput[0] == "/":
        print "Command invalid"
    else:
        for c in userInput :
            try:
                print __im.items[c].toString()
            except KeyError:
                print 'The item {} doesn\'t exist'.format(c)

def __itemInput():
    print("Creating New Item")
    try:
        name = raw_input("Name? ")
        identifier = raw_input("Identifier? ")
        price = raw_input("Price? ")
        i = Item.Item(name, identifier, price)
        __im.items[identifier] = i
    except Exception, err:
        print(err)
        print("Item not created")


def __exitProgram():
    print("terminating...")
    sys.exit()

if __name__ == '__main__':
    import sys
    import ItemManager, Item

    __im = ItemManager.ItemManager()
    while(True):
        try:
            userInput = raw_input("# ");
        except:
            __exitProgram() ## We caught Ctrl + D
        parseInput(userInput)



