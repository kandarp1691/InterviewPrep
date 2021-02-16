class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.big = big
        self.medium = medium
        self.small = small
        self.big_counter = 0
        self.medium_counter = 0
        self.small_counter = 0

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if carType == 1 and self.small_counter != self.small:
            self.small_counter = self.small_counter + 1
            return True
        if carType == 2 and self.medium_counter != self.medium:
            self.medium_counter = self.medium_counter + 1
            return True
        if carType == 3 and self.big_counter != self.big:
            self.big_counter = self.big_counter + 1
            return True
        else:
            return False

p = ParkingSystem(1,1,0)
print p.addCar(1)
print p.addCar(2)
print p.addCar(3)
