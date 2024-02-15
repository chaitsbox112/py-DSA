class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self,data):
        if data == self.data:
            return 
        
        if data < self.data:
        # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BSTNode(data)
    
    def inot(self):
        elements = []

        # visit left tree
        if self.left:
            elements += self.left.inot()

        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.inot()
        
        return elements

    def preot(self):
        elements = []
        #visit root node
        elements.append(self.data)

        #visit left tree
        if self.left:
            elements += self.left.preot()

        #visit right tree
        if self.right:
            elements += self.right.preot()

        return elements
    
    def postot(self):
        elements = []
        #visit left tree
        if self.left:
            elements += self.left.postot()

        #visit right tree
        if self.right:
            elements += self.right.postot()

        # vist base node
        elements.append(self.data)

        return elements

    def search(self,val):
        if val == self.data:
            return True
        
        # value might be present on the left subtree
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
            
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        
        return self


        

    
    
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BSTNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root




if __name__ == "__main__":
    numbers = [17,4,1,20,9,23,18,34]
    bt = build_tree(numbers)
    print(numbers)
    print("Inorder traversal ==>", bt.inot())
    print("preorder traversal ==>",bt.preot())
    print("postorder traversal ==>",bt.postot())
    print(bt.search(20))

    print("Minimum element ==> ",bt.find_min())
    print("Max value ==>",bt.find_max())
    bt.delete(20)
    print("After deleting 20",bt.inot())