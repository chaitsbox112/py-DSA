class TreeNode:
    def __init__(self,location):
        self.location = location
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def print_tree(self,level):
        if self.get_level() > level:
            return 
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.location)
        if self.children:
            for child in self.children:
                child.print_tree(level)


    
def gen_location():
    Global = TreeNode("Global")


    India = TreeNode("India")
    

    Gujrat = TreeNode("Gujrat")
    Gujrat.add_child(TreeNode("Ahmedabad"))
    Gujrat.add_child(TreeNode("Baroda"))
    

    Karnataka = TreeNode("Karnataka")
    Karnataka.add_child(TreeNode("Bangluru"))
    Karnataka.add_child(TreeNode("Mysore"))

    
    India.add_child(Gujrat)
    India.add_child(Karnataka)


    Usa = TreeNode("USA")
   
    newjer = TreeNode("New Jersey")
    newjer.add_child(TreeNode("Princeton"))
    newjer.add_child(TreeNode("Trenton"))
    
    califor = TreeNode("California")
    califor.add_child(TreeNode("San Francisco"))
    califor.add_child(TreeNode("Mountain View"))
    califor.add_child(TreeNode("Palo Alto"))

    Usa.add_child(newjer)
    Usa.add_child(califor)

    Global.add_child(India)
    Global.add_child(Usa)

    return Global





if __name__ == "__main__":
    rootnode = gen_location()
    rootnode.print_tree(1)
    print("***************\n")
    rootnode.print_tree(2)
    print("***************\n")
    rootnode.print_tree(3)
    print("***************\n")

