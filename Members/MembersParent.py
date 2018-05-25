# from Loads.ReadLoads import *


class MembersParent(object):
    unitprice = 30   # $/ft^3
    density = 0.49    # kip/ft^3

    CompressiveYieldStrength = 29000  # psi
    ShearModulus = 11500  # psi

    def __init__(self, wb, hb, lb, wc, tc, hc, n):
        self.beam_width = wb        # in
        self.beam_height = hb       # in
        self.beam_length = lb       # ft

        self.column_width = wc      # in
        self.column_thickness = tc  # in
        self.column_height = hc     # ft

        self.numbers_of_level = n     # #

        self.weight_from_beam = 0
        self.weight_from_column = 0
