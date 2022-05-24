class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self, num, denom):
        # num and demon are integers
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom
    
    def __str__(self):
        # return the string representation of the object
        return "{}/{}".format(self.num, self.denom)

    def __add__(self, other):
        # returns a new fraction of the addtion of two fraction objection
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    
    def __sub__(self, other):
        # Returns a new fraction representing the subtraction
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    
    def __float__(self):
        # Returns a float value of the fraction """
        return self.num/self.denom

    def inverse(self):
        # Returns a new fraction representing 1/self 
        return Fraction(self.denom, self.num)

a = Fraction(1,4)
b = Fraction(3,4)
c = a + b
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))