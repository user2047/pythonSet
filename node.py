class node:
    
    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,val):
        if self.value == None:
            self.value = val
        if self.value == val:
            return True
        elif val < self.value:
            if self.left!=None:
                self.left.insert(val)
            else:
                self.left = node(val)
                return False
        elif val > self.value:
            if self.right!=None:
                self.right.insert(val)
            else:
                self.right = node(val)
                return False

    def search(self,val):
        if self.value == None:
            return False
        if self.value == val:
            return True
        elif val < self.value:
            if self.left!=None:
                self.left.search(val)
            else:
                return False
        elif val > self.value:
            if self.right!=None:
                self.right.search(val)
            else:
                return False

if __name__ == "__main__":
    asdf = node()
    asdf.insert(50)
    asdf.insert(100)
    asdf.insert(25)
    asdf.insert(34)
    asdf.search(34)
    print(asdf.search(100))
    print(asdf.value)