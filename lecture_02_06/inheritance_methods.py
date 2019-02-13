class Noisemaker:

    def make_noise(self):
        print("*silence*")


class DelegatesToSuper(Noisemaker):

    def make_noise(self):
        # delegate to superclass
        super().make_noise()


class Dog(Noisemaker):
    def make_noise(self):
        # override the method
        print("woof")


class Wrapper(Noisemaker):
    def __init__(self, n):
        self._n = n

    def make_noise(self):
        print("About to make noise")
        self._n.make_noise()
        print("Done making noise")


if __name__ == '__main__':
    Noisemaker().make_noise()
    DelegatesToSuper().make_noise()
    Dog().make_noise()
    Wrapper(Dog()).make_noise()
