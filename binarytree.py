class node:
    self.value = None
    self.left = None
    self.right = None
    def self.__init__(value):
        self.value = value
    
    def insert(val):
        if self.value == val:
            return true
        elif val < self.value:
            if self.left!=None:
                self.left.insert(val)
            else:
                self.left = val
                return false
        elif val > self.value:
            if self.right!=None:
                self.right.insert(val)
            else:
                self.right = val
                return false

    def search(val):
        if self.value == val:
            return true
        elif val < self.value:
            if self.left!=None:
                self.left.search(val)
            else:
                return false
        elif val > self.value:
            if self.right!=None:
                self.right.search(val)
            else:
                return false