from typing import Hashable, TypeVar, Mapping, List, Sequence, MutableMapping


def pos_ints(ints: list) -> list:
    out = []
    for x in ints:
        if x > 0:
            out.append(x)

    return out


def pos_ints2(ints: Sequence[int]) -> List[int]:
    out = []
    for x in ints:
        if x > 0:
            out.append(x)

    return out


T = TypeVar('T', bound=Hashable)


def counts(data: Sequence[T]) -> Mapping[T, int]:
    counters: MutableMapping[T, int] = {}
    for x in data:
        if x in counters:
            counters[x] = counters[x] + 1
        else:
            counters[x] = 1

    return counters


print(pos_ints2([1, 2, -3, 4, -5]))
print(pos_ints2(['foo', 'bar']))

print(counts([1, 2, 3, 1, 2]))
print(counts(['foo', 'bar', 'baz']))
# not hashable, but mypy doesn't complain...?
print(counts([set()]))

