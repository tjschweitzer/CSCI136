from typing import Optional, Sequence,TypeVar


def  square (n: int)->int:
    return n*n

T= TypeVar('T')

def first(a: Sequence[T],b: T)-> T:
    if len(a) > 0:
        return a[-1]
    return None




print(square(3))
# print(square('wrong'))

arrStr=['123','234','345']
stty='555'
print(first(arrStr,stty))
