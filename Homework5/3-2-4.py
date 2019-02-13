class Rectangle:

    # Construct self with center (x, y), width w, and height h.
    def __init__(self, lx, ly, rx, ry):
        self._lx = lx
        self._ly = ly
        self._rx = rx
        self._ry = ry

    # Return the area of self.
    def area(self):
        areaCalc = (self._rx-self._lx) * (self._ry-self._ly)
        return areaCalc

    # Return the perimeter of self.
    def perimeter(self):
        perimCalc = 2 * (self._rx-self._lx) + (self._ry-self._ly)
        return perimCalc

    # Return True if self intersects other, and False otherwise.
    def intersects(self, other):
        xFlag=False
        yFlag=False
        if self._lx<=other._rx and self._lx>=other._lx:
            xFlag=True
        elif self._rx>=other._rx and self._rx<=other._lx:
            xFlag=True


        if self._ly<=other._ry and self._ly>=other._ly:
            yFlag=True
        elif self._ry>=other._ry and self._ry<=other._ly:
            yFlag=True
        return xFlag and yFlag

    # Return True if other is completely inside of self, and False
    # otherwise.
    def contains(self, other):
        #checks if the left and right sides of "other" are inside of "self"
        if self._lx<other._lx and self._rx>other._rx:
            if self._ly>self._ly and self._ry<other._ry:
                return True
        return False




def main():
    rec1 = Rectangle(10,10,10,10)
    rec2 = Rectangle(5,5,5,5)


if __name__ == "__main__":
    main()