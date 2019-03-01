import abc as abc
from abc import abstractmethod

class predicate(abc):
    @abstractmethod
    def isTrue(self,x):
        pass

class intPred(predicate):
    def isTrue(self,x):
        return x>0



def eval(a,p):
    aRR=[]
    for z in a:
        if p.isTrue(z):
            aRR.append(z)
    return aRR

ray=[1,2,3,4,-5,6,-7]
print(eval(ray,intPred()))
