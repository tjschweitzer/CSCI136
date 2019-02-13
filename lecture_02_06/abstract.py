import abc


class MaxFinder(abc.ABC):
    @abc.abstractmethod
    def max_of(self, a, b):
        pass


class NormalCompareMaxFinder(MaxFinder):

    def max_of(self, a, b):
        if a > b:
            return a
        return b


class StrLenMaxFinder(MaxFinder):

    def max_of(self, a, b):
        if len(str(a)) > len(str(b)):
            return a
        return b


def find_max(things, max_finder):
    m = things[0]

    for t in things:
        m = max_finder.max_of(m, t)

    return m


if __name__ == '__main__':
    print(find_max([1, 97, -3, 204, 17], MaxFinder()))
    print(find_max([1, 97, -3, 204, -103, 17], NormalCompareMaxFinder()))
    print(find_max([1, 97, -3, 204, -103, 17], StrLenMaxFinder()))

