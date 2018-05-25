from tkMessageBox import *


class ParameterCheck:
    def __init__(self):
        self.error = 0

    def check_warning(self):
        if self.error != 0:
            showerror("Error", "Make sure you conform to our instructions.")

    def check_story_number(self, sn):
        if sn == 1 or sn == 2 or sn == 3 or sn == 4 or sn == 5:
            return sn
        else:
            self.error += 1

    def check_story_height(self, shn):
        if shn >= 8.0:
            if shn <= 15.0:
                return shn
            else:
                self.error += 1
                self.check_warning()
        else:
            self.error += 1

    def check_beam_length(self, bln):
        if bln >= 10.0:
            if bln <= 25:
                return bln
            else:
                self.error += 1
                self.check_warning()
        else:
            self.error += 1

    def check_beam_width(self, bw):
        if bw == 10.0 or bw == 15.0 or bw == 20.0 or bw == 25.0 or bw == 30.0 or bw == 35.0 or bw == 40.0:
            return bw
        else:
            self.error += 1

    def check_beam_height(self, bh):
        if bh == 15.0 or bh == 20.0 or bh == 25.0 or bh == 30.0 or bh == 35.0:
            return bh
        elif bh == 40.0 or bh == 45.0 or bh == 50.0 or bh == 55.0 or bh == 60.0:
            return bh
        else:
            self.error += 1

    def check_column_width(self, cw):
        if cw == 10.0 or cw == 20.0 or cw == 30.0 or cw == 40.0:
            return cw
        else:
            self.error += 1

    def check_column_thickness(self, ct):
        if ct == 10.0 or ct == 20.0 or ct == 30.0 or ct == 40.0:
            return ct
        else:
            self.error += 1
