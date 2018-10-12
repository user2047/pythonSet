class aset:
    def __init__(self):
        self.hash = dict()
        self.list = list()

    #def __iter__(self):

    def contains(self,val):
        try:
            self.hash[val]
            return True
        except KeyError:
            return False
    
    def insert(self,val):
        if not self.contains(val):
            self.hash[val] = val
            self.list.append(val)

    def insertList(self,alist):
        for index in alist:
            self.insert(index)


    def delete(self,val):
        del self.hash[val]
        self.list.remove(val)
        
    