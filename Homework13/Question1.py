from typing import Optional, Sequence,TypeVar

T= TypeVar('T')

def first(a: Sequence[T],b: T)-> T:
    if len(a) > 0:
        return a[-1]
    return None


arrStr=['123','234','345']
stty='555'
print(first(arrStr,stty))
