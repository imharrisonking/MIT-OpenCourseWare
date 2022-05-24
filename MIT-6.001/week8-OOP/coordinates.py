class Coordinate(object):
    def __init__(self, x, y):
        # Sets the x and y coordinates of the object
        self.x = x
        self.y = y

    def distance(self, other):
        # Returns the euclidean distance between two points
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __str__(self):
        # Special operator __str__ to return a string representaiton to the user when print(c) is called
        return "<{}, {}>".format(self.x, self.y)

c = Coordinate(3,4)
origin = Coordinate(0,0)

print(c.distance(origin))
print(c)
print(type(c))
