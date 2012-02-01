'''
Created on Feb 1, 2012

@author: lbillon
'''

from compiler.ast import TryExcept

def __exitProgram():
    print("terminating...")
    sys.exit()

if __name__ == '__main__':
    import sys
    import ItemManager
    
    __im = ItemManager.ItemManager()
    while(True):
        try:
            userInput = raw_input();
        except:
            __exitProgram() ## We caught Ctrl + D
        __im.parseInput(userInput)
        
        
        
