def any(boolArray):
    total=sum(boolArray)
    if total == 0:
        return False
    else:
        return True


def all(boolArray):
    total=sum(boolArray)
    if total == len(boolArray):
        return True
    else:
        return False

