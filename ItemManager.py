'''
Created on Feb 1, 2012

@author: lbillon
'''
import Item

class ItemManager(object):


    def __init__(self):
        self.__items = {}
    
    def __itemInput(self):
        print("Creating New Item")
        name = raw_input("Name? ")
        
        while(True):
            identifier = raw_input("Identifier?")
            if(len(identifier)==1):
                
                if(identifier not in self.__items ):
                    break
                else:
                    print("This identifier is already used")
           
            else:
                print("The identifier must be 1 character long")
        
        while(True):
            try:
                price = float(raw_input("Price? "))
                break
            except ValueError:
                print("Not a valid price")
        print(price)
        confirm = raw_input("Is this correct ? (y/n)")
        
        if(confirm!="y"):
            return
        i = Item.Item(name,identifier,price)
        self.__items[identifier]=i
    
    def __listItems(self):
        print("Item List : ")
        for i in self.__items:
            print(self.__items[i].toString())

        

    def parseInput(self,userInput):
        if userInput == "/+":
            self.__itemInput();
        elif userInput == "/l":
            self.__listItems();
        elif userInput[0]=="/":
            print "Command invalid"
        else:
            for c in userInput :
                try:
                    print self.__items[c].toString()
                except KeyError:
                    print 'The item {} doesn\'t exist'.format(c)
                
                

        
            