class Fraction:
    def __init__(self,n,d):
        self.num =n
        self.den =d

    def __str__(self):
        return "{}/{}".format(self.num , self.den)

    
    def __add__(self,other):

        self.num = self.num*other.den + self.den*other.num
        self.den = self.den*other.den

        return "{}/{}".format(self.num ,self.den)

    def __mul__(self,other):
        self.num = self.num*other.num
        self.den= self.den*other.den

        return "{}/{}".format(self.num , self.den)
