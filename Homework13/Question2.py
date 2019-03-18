# Wight a simple Counter class with git() and increment() functions, as well as hash

# What would happen if you used a counter to as a key then incremented the counter?
# Your hash table would be incorrect unless you recalculated the hast table after every increment.
# this could be very inefficient for memory and processing


class Clounter:
    def __init__(self):
        self._counter=0

    def get(self):
        return self._counter

    def incerment(self):
        self._counter += 1

    def __hash__(self):
        return hash(self._counter)


