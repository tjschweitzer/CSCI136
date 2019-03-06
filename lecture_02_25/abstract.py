from abc import abstractmethod, ABC


class RandomSource(ABC):
    @abstractmethod
    def flip_a_coin(self):
        pass


class NotVeryRandom(RandomSource):
    def flip_a_coin(self):
        return True


class ActuallyRandom(RandomSource):
    def flip_a_coin(self):
        import random
        return random.random() > 0.5


if __name__ == '__main__':
    for _ in range(10):
        print(NotVeryRandom().flip_a_coin())
    print('-----')
    for _ in range(10):
        print(ActuallyRandom().flip_a_coin())
    print('-----')
    for _ in range(10):
        print(RandomSource().flip_a_coin())
