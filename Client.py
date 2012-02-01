'''
Created on Feb 1, 2012

@author: lbillon
'''
from inspect import Traceback


def __listItems():
    print("Available Items :")
    for i in __im.items:
        print(__im.items[i].toString())

def __parseInput(userInput):
    if userInput == "/+":
        __itemInput();

    elif userInput == "/i":
        __listItems();

    elif userInput.startswith("/s "):
        fileName = userInput.split(" ")[1]
        try:
            __im.saveToFile(fileName)
            print("Saved item definitions to {}".format(fileName))
        except IOError, err:
            print err

    elif userInput.startswith("/l "):
        fileName = userInput.split(" ")[1]
        try:
            __im.loadFromFile(fileName)
            print("Loaded item definitions from {}".format(fileName))
            __listItems()
        except IOError, err:
            print err

    elif userInput[0] == "/":
        print "Command invalid"

    else:
        itemList = {}
        sum = 0
        paid = 0
        for c in userInput :
            try:
                i = __im.items[c]
                if i in itemList:
                    itemList[i] = itemList[i] + 1
                else:
                    itemList[i] = 1
            except KeyError:
                print 'The item {} doesn\'t exist'.format(c)
                return 1
        print("Ordered Items: ")
        for i in itemList:
            print '{} x {} = {:.2f}'.format(itemList[i], i.name, itemList[i] * i.price)
            sum += itemList[i] * i.price
        print("Total:\n{:.2f}".format(sum))
        while(True):
                paid = raw_input("Amount given: ")


                try:
                    paid = float(paid)
                    if(paid < 0):
                        print("Transaction cancelled")
                        break
                    elif(paid < sum):
                        print("Unsufficient amount : need {}".format(sum - paid))
                    else:
                        print("Anount to return : {:.2f}".format(paid - sum))
                        print("Transaction committed\n")
                        break
                except :
                    print("Invalid Value")
                    continue








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
        __parseInput(userInput)



