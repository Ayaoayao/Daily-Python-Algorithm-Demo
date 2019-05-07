class randomSet(object):
    def __init__(self):
        self.testset=set()

    def insert(self,val):
        if  self.testset:
            for var in self.testset:
                if var==val:
                    return False
                else:
                    self.testset.add(val)
                    return True
        else:
            self.testset.add(val)
            return True

    def remove(self,val):
        if self.testset:
            for var in self.testset:
                if var==val:
                    self.testset.remove(val)                
                    return True
                else:
                    return False
        else:
            return False

    def getRandom(self):
        if  self.testset:
            temp=list(self.testset)
            return random.choice(temp)
        else:
            return False

if __name__ == '__main__':
    import random
    obj=randomSet()
    param=obj.insert(1)
    param=obj.remove(2)
    param=obj.insert(2)
    param=obj.getRandom()
    param=obj.remove(1)
    param=obj.insert(2)
    param=obj.getRandom()
    print(param)
    print(obj.testset)