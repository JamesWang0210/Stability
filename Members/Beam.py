from Loads.ReadLoads import *
from MembersParent import MembersParent


class Beam(MembersParent):
    def __init__(self):
        super(MembersParent, self).__init__()
        self.volume = 0       # ft^3
        self.weight = 0       # kip
        self.beam_shear5 = 0  # kip
        self.beam_shear4 = 0  # kip
        self.beam_shear3 = 0  # kip
        self.beam_shear2 = 0  # kip
        self.beam_shear1 = 0  # kip
        self.beam_moment5 = 0  # kip*ft
        self.beam_moment4 = 0  # kip*ft
        self.beam_moment3 = 0  # kip*ft
        self.beam_moment2 = 0  # kip*ft
        self.beam_moment1 = 0  # kip*ft

    def beam_volume(self):  # ft^3
        self.volume = 1.0 * self.beam_height * self.beam_width * self.beam_length / (12 ** 2)
        return self.volume

    def beam_weight(self):  # lbf
        self.weight = 1.0 * self.beam_volume() * self.density
        return self.weight

    def area(self):
        a = (2 * self.beam_width+self.beam_height) * 1
        return a

    # Shear
    def beam_shear_5(self):  # kip
        self.beam_shear5 = (self.beam_weight() + total_loads() * self.beam_length) / 2.0
        return self.beam_shear5

    def beam_shear_4(self):  # kip
        self.beam_shear4 = (2 * self.beam_weight() + total_loads() * self.beam_length
                            + 2 * self.weight_from_column/3.0) / 2.0
        return self.beam_shear4

    def beam_shear_3(self):  # kip
        self.beam_shear3 = (3 * self.beam_weight() + total_loads() * self.beam_length
                            + 4 * self.weight_from_column/3.0) / 2.0
        return self.beam_shear3

    def beam_shear_2(self):  # kip
        self.beam_shear2 = (4 * self.beam_weight() + total_loads() * self.beam_length
                            + 6 * self.weight_from_column/3.0) / 2.0
        return self.beam_shear2

    def beam_shear_1(self):  # kip
        self.beam_shear1 = (5 * self.beam_weight() + total_loads() * self.beam_length
                            + 8 * self.weight_from_column/3.0) / 2.0
        return self.beam_shear1

    # Moment
    # for the top floor
    def beam_moment_5(self):  # kip*ft
        self.beam_moment5 = (self.beam_weight() * self.beam_length / 4.0 +
                             (self.beam_length ** 2) * total_loads() / 8.0)
        return self.beam_moment5

    # for the second top floor
    def beam_moment_4(self):  # kip*ft
        self.beam_moment4 = (self.beam_weight() + self.weight_from_column*(2.0/3))\
                            * self.beam_length / 4.0 + (self.beam_length ** 2) * total_loads() / 8
        return self.beam_moment4

    # for the third floor
    def beam_moment_3(self):  # kip*ft
        self.beam_moment3 = (self.beam_weight() + 2*self.weight_from_column*(2.0/3)) \
                            * self.beam_length / 4.0 + (self.beam_length ** 2) * total_loads() / 8
        return self.beam_moment3

    # for the second last floor
    def beam_moment_2(self):  # kip*ft
        self.beam_moment2 = (self.beam_weight() + 3*self.weight_from_column*(2.0/3)) \
                            * self.beam_length / 4.0 + (self.beam_length ** 2) * total_loads() / 8
        return self.beam_moment2

    # for the last floor
    def beam_moment_1(self):  # kip*ft
        self.beam_moment1 = (self.beam_weight() + 4*self.weight_from_column*(2.0/3)) \
                            * self.beam_length / 4.0 + (self.beam_length ** 2) * total_loads() / 8
        return self.beam_moment1
