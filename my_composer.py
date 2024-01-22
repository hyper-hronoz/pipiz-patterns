class LeafElement: 
  
    '''Class representing objects at the bottom or Leaf of the hierarchy tree.'''
  
    def __init__(self, pos): 
  
        ''''Takes the first positional argument and assigns to member variable "position".'''
        self.position = pos
  
    def showDetails(self): 
  
        '''Prints the position of the child element.'''
        print("\t", end ="") 
        print(self.position) 
  
  
class CompositeElement: 
  
    '''Class representing objects at any level of the hierarchy 
     tree except for the bottom or leaf level. Maintains the child 
      objects by adding and removing them from the tree structure.'''
  
    def __init__(self, pos): 
  
        '''Takes the first positional argument and assigns to member 
         variable "position". Initializes a list of children elements.'''
        self.position = pos
        self.children = [] 
  
    def add(self, child): 
  
        '''Adds the supplied child element to the list of children 
         elements "children".'''
        self.children.append(child) 
  
    def remove(self, child): 
  
        '''Removes the supplied child element from the list of 
        children elements "children".'''
        self.children.remove(child) 
  
    def showDetails(self): 
  
        '''Prints the details of the component element first. Then, 
        iterates over each of its children, prints their details by 
        calling their showDetails() method.'''
        print(self.position) 
        for child in self.children: 
            print("\t", end ="") 
            child.showDetails() 
  
  
"""main method"""
  
if __name__ == "__main__": 
  
    topLevelMenu = CompositeElement("GeneralManager") 
    subMenuItem1 = CompositeElement("Manager1") 
    subMenuItem2 = CompositeElement("Manager2") 
    subMenuItem = CompositeElement("Manager3") 
    subMenuItem11 = CompositeElement("Developer11") 
    subMenuItem111 = LeafElement("Developer111") 
    subMenuItem112 = LeafElement("Developer112") 
    subMenuItem12 = LeafElement("Developer12") 
    subMenuItem21 = LeafElement("Developer21") 
    subMenuItem22 = LeafElement("Developer22") 
    subMenuItem1.add(subMenuItem11) 
    subMenuItem1.add(subMenuItem12) 
    subMenuItem2.add(subMenuItem22) 
    subMenuItem2.add(subMenuItem22) 

    subMenuItem11.add(subMenuItem111);
    subMenuItem11.add(subMenuItem112);
  
    topLevelMenu.add(subMenuItem1) 
    topLevelMenu.add(subMenuItem2) 
    topLevelMenu.showDetails() 
