from Tkinter import *
from PIL import ImageTk
from tkMessageBox import *


class GameCanvas(Canvas):
    def __init__(self, p, w, h, bg):
        Canvas.__init__(self, master=p, width=w, height=h, bg=bg)
        self.image = None

        self.component_color = "brown"
        self.component_size = 8

        self.Click = None
        self.c = None
        self.line = None

    def game_background(self):
        self.image = ImageTk.PhotoImage(file='game_background.gif')
        self.create_image(0, 0, anchor=NW, image=self.image)

    def draw_structure(self, sn, shn, bln):
        self.c = []

        x00 = self.Click[0]
        y00 = self.Click[1]

        if 5.0 <= x00 <= 450.0:
            if 468.0 <= y00 <= 480.0:
                x01 = x00 + bln*6
                y01 = y00

                self.c.append([x00, y00])
                self.c.append([x01, y01])

                for i in range(1, sn+1):
                    m = x00
                    n = y00 - shn*6*i
                    p = x01
                    q = y01 - shn*6*i
                    self.c.append([m, n])
                    self.c.append([p, q])

                    z0 = self.c[2*i-2]
                    z1 = self.c[2*i-1]
                    z2 = self.c[2*i]
                    z3 = self.c[2*i+1]

                    self.create_line(z0[0], z0[1], z2[0], z2[1], width=self.component_size,fill=self.component_color)
                    self.create_line(z1[0], z1[1], z3[0], z3[1], width=self.component_size, fill=self.component_color)
                    self.create_line(z2[0], z2[1], z3[0], z3[1], width=self.component_size, fill=self.component_color)
            else:
                showwarning("Warning", "Please click 'Confirm' again and create structure siting on the lawn.")
        else:
            showwarning("Warning", "Please click 'Confirm' again and create structure siting on the lawn.")
