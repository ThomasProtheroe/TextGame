'''
Created on Jun 29, 2014

@author: Thomas
'''
from Main import BaseClasses

class StandardOpenDoor(BaseClasses.Door):
    
    def __init__(self, description, keywords):
        super(StandardOpenDoor, self).__init__(description, keywords, True, "", "You open the door and step through.")

        
class StandardLockedDoor(BaseClasses.Door):
    
    def __init__(self, description, keywords, itemToOpen):
        self.itemToOpen = itemToOpen
        super(StandardLockedDoor, self).__init__(description, keywords, False, "The door is locked. It won't budge.", "You open the door and step through.")
        
    def unlock(self, usedItem):
        if usedItem == self.itemToOpen:
            self.isAccessible = True
            return usedItem.useDescription
        else:    
            return "The key does not appear to work for this door."
    
class UnlockedContainer(BaseClasses.Container):
    
    def __init__(self, description, keywords, openDesc, closeDesc):
        super(UnlockedContainer, self).__init__(description, keywords, False, True, "",openDesc, closeDesc)
        
class LockedContainer(BaseClasses.Container):
    
    def __init__(self, description, keywords, blockedDesc, openDesc, closeDesc, itemToOpen):
        self.itemToOpen = itemToOpen
        super(LockedContainer, self).__init__(description, keywords, False, False, blockedDesc, openDesc, closeDesc)
        
    def unlock(self, usedItem):
        if usedItem == self.itemToOpen:
            self.isAccessible = True
            return usedItem.useDescription
        else:
            return "That key does not seem to fit the lock."
        
class AlwaysOpenContainer(BaseClasses.Container):
    
    def __init__(self, description, keywords):
        super(AlwaysOpenContainer, self).__init__(description, keywords, True, True, "", "", "")
        
    def open(self):
        return "You can't open that."
    
    def close(self):
        return "You can't close that."
    
    def lookAt(self):
        desc = self.description
        if self.itemsContained:
            desc += "On it you see:\n"
            for item in self.itemsContained.itervalues():
                desc += item.seenDescription + "\n"
        return desc