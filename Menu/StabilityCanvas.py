from Tkinter import *
from PIL import ImageTk


class CanvasGo(Canvas):
    def __init__(self, p, w, h, bg):
        Canvas.__init__(self, master=p, width=w, height=h, bg=bg)
        self.image = None

    def interface_image(self):
        self.image = ImageTk.PhotoImage(file='architecture.gif')
        self.create_image(0, 0, anchor=NW, image=self.image)

    def interface_name(self):
        self.create_text(473, 242, text="Stability", anchor=S, font=('GothicE', 90), fill='white')
        self.create_text(470, 240, text="Stability", anchor=S, font=('GothicE', 90), fill='black')
