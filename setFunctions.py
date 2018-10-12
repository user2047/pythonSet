from aset import *

def union(set1, set2):
    output = aset()
    for index in set1.list:
        output.insert(index)
    for index in set2.list:
        output.insert(index)
    return output
    
def intersection(set1,set2):
    output = aset()
    for index in set1.list:
        if set2.contains(index):
            output.insert(index)
    return output

def difference(set1,set2):
    output = aset()
    for index in set1.list:
        if not set2.contains(index):
            output.insert(index)
    return output

def xor(set1,set2):
    output = aset()
    for index in set1.list:
        if not set2.contains(index):
            output.insert(index)
    for index in set2.list:
        if not set1.contains(index):
            output.insert(index)
    return output

def genUniversal():
    universal = aset()
    for index in range(-6,13,1):
        universal.insert(index)
    # for index in universal.list:
    #     print(index,end='')
    return universal
def negation(set1):
    output = genUniversal()
    for index in set1.list:
        output.delete(index)
    return output

def cross(set1,set2):
    output = aset()
    for i in set1.list:
        for j in set2.list:
            output.insert((i,j))
    return output

def powerSet(set1):
    output = aset()
    # to be written


if __name__ == "__main__":
    asdf = aset()
    a = aset()
    b = aset()
    c = aset()
    d = aset()
    e = aset()
    f = aset()
    g = aset()
    a.insertList([1,3,5,7,9,11])
    b.insertList([-3,-2,-1,0,1,2,3])
    c.insertList([-6,-4,-2,0,2,4,6,8,10,12])
    d.insertList([-6,-5,-4,-3,-2,-1,0])
    e.insertList([2,4,6])
    f.insertList([1,2,3,4,5])
    g.insertList([0,1])
    print("a",end="")
    print(a.list)
    print("b",end="")
    print(b.list)
    print("c",end="")
    print(c.list)
    print("d",end="")
    print(d.list)
    print("e",end="")
    print(e.list)
    print("f",end="")
    print(f.list)
    print("g",end="")
    print(g.list)
    print()
    print()



    print(union(a,b).list)
    print()
    print(intersection(c,e).list)
    print()
    print(union(intersection(a,b),e).list)
    print()
    print(intersection(c,d).list)
    print()
    # print(powerSet(e).list)
    print()
    print(difference(a,b).list)
    print()
    print(negation(d).list)
    print()
    print(xor(e,f).list)
    print()
    print(intersection(negation(union(union(a,b),e)),difference(c,d)).list)
    print()
    print(cross(e,g).list)
