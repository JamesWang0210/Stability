from Loads.ReadLoads import *
from MembersParent import MembersParent


class Column(MembersParent):
    def __init__(self):
        super(MembersParent, self).__init__()
        self.volume = 0      # ft^3
        self.weight = 0      # kip
        self.axial5 = 0       # kip
        self.axial4 = 0       # kip
        self.axial3 = 0       # kip
        self.axial2 = 0       # kip
        self.axial1 = 0       # kip

    def column_volume(self):  # ft^3
        self.volume = self.area()*self.column_height/(12**2)
        return self.volume

    def column_weight(self):  # lbf
        self.weight = self.column_volume()*self.density
        return self.weight

    # Axial force
    def area(self):
        a = 2 * (self.column_width+self.column_thickness) * 1
        return a

    def column_axial_5(self):
        self.axial5 = (total_loads() + self.weight_from_beam) / 2.0
        return self.axial5

    def column_axial_4(self):
        self.axial4 = (2*total_loads() + self.weight_from_beam + 2*self.weight_from_column) / 2.0
        return self.axial4

    def column_axial_3(self):
        self.axial3 = (3*total_loads() + self.weight_from_beam + 4*self.weight_from_column) / 2.0
        return self.axial3

    def column_axial_2(self):
        self.axial2 = (4*total_loads() + self.weight_from_beam + 6*self.weight_from_column) / 2.0
        return self.axial2

    def column_axial_1(self):
        self.axial1 = (5*total_loads() + self.weight_from_beam + 8*self.weight_from_column) / 2.0
        return self.axial1
