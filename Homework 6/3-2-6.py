import math

class Location():
    def __init__(self,lat,long):
        self._long = long
        self._lat = lat

    def distanceTO(self,other):
        x1 = math.radians(self._lat)
        x2 = math.radians(other._lat)
        y1 = math.radians(self._long)
        y2 = math.radians(other._long)
        angle = math.acos(math.sin(x1) * math.sin(x2) \
                          + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
        # Convert back to degrees.
        angle = math.degrees(angle)

        # Each degree on a great circle of Earth is 60 nautical miles.
        distance = 60.0 * angle
        return distance