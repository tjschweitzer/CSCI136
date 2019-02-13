class Rectangle:

    # Construct self with center (x, y), width w, and height h.
    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._width = w
        self._height = h

    # Return the area of self.
    def area(self):
        return self._width * self._height

    # Return the perimeter of self.
    def perimeter(self):
        return 2 * (self._height + self._width)

    # Return True if self intersects other, and False otherwise.
    def intersects(self, other):
        xFlag=False
        yFlag=False
        # checks if right side of "self" is in between the other rectangle
        ##print(self._width / 2 + self._x, other._x - other._width / 2 , self._width / 2 + self._x , other._height / 2 + other._x)
        ##print(self._x - self._width / 2 >= other._x - other._width / 2 , self._x - self._width / 2 <= other._width / 2 + other._x)

        if self._width / 2 + self._x > other._x - other._width / 2 and self._width / 2 + self._x <= other._height / 2 + other._x:
            xFlag=True
            # checks if left side of "self" is in between the other rectangle
        elif self._x - self._width / 2 >= other._x - other._width / 2  and self._x - self._width / 2  <= other._width / 2 + other._x :
            xFlag=True


        # checks if top side of "self" is in between the other rectangle
        ##print(self._height / 2 + self._y , other._height / 2 + other._y , self._y + self._height / 2, other._y - other._height / 2 )
        ##print(self._y - self._height / 2 , other._y - other._y / 2 , self._y - self._height / 2, other._height / 2 + other._y)
        if self._height / 2 + self._y <= other._height / 2 + other._y and  self._y + self._height / 2 >= other._y - other._height / 2 :
            yFlag = True
            # checks if bottom side of "self" is in between the other rectangle
        elif self._y - self._height / 2 >= other._y - other._y / 2 and  self._y - self._height / 2  <= other._height / 2 + other._y:
            yFlag = True

        return xFlag and yFlag

    # Return True if other is completely inside of self, and False
    # otherwise.
    def contains(self, other):
        #checks if the left and right sides of "other" are inside of "self"
        if self._x - self._width / 2  < other._x  - other._width / 2 and self._width / 2 + self._x > other._width / 2 + other._x:

            # checks if the top and bottom sides of "other" are inside of "self"
            if self._y - self._height / 2 < other._y - other._height / 2 and self._height / 2 + self._y > other._height / 2 + other._y:
                return True
        return False




def main():
    rec1 = Rectangle(10,10,10,10)
    rec2 = Rectangle(5,5,5,5)


if __name__ == "__main__":
    main()