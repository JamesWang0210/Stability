from Tkinter import *
from tkMessageBox import *
# from StabilityCanvas import CanvasGo


class Stability(object):
    def __init__(self):
        self.window = Tk()

        self.canvas = None
        self.start_game = None
        self.exit_game = None

        self.player_check_in = None
        self.ID = None
        self.Password = None

    '''
    Functions used in GUI creation
    '''

    def create_window(self):
        self.window.title("Stability")

        w = 960
        h = 540
        sw = self.window.winfo_screenwidth()
        sh = self.window.winfo_screenheight()

        # Position of Main Interface
        x = (sw/2) - (w/2)
        y = (sh/2) - (h/2)

        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def save_player(self,event):
        m = self.ID.get()
        n = self.Password.get()
        if len(m) <= 7 and len(n) >= 6:
            with open('UserInfo.txt', 'a') as f:
                f.write(m + ',' + n + '\n')
            self.player_check_in.destroy()
            self.window.deiconify()
        else:
            showinfo("Notification", "Your ID should be at most 7 characters.\n"
                     "Your password should be at least 6 characters. ")

    def create_player(self):  # Create your own player!
        self.window.iconify()
        self.player_check_in = Toplevel()
        self.player_check_in.title('Create New Player')
        self.player_check_in.geometry("300x120+500+250")

        label1 = Label(self.player_check_in, text='ID')
        label1.grid(row=0, column=0, padx=10, pady=10)

        n = StringVar()
        self.ID = Entry(self.player_check_in, textvariable=n)
        self.ID.grid(row=0, column=1, padx=5, pady=5)

        label2 = Label(self.player_check_in, text='Password')
        label2.grid(row=1, column=0, padx=10, pady=10)

        pw = StringVar()
        self.Password = Entry(self.player_check_in, textvariable=pw)
        self.Password.grid(row=1, column=1, padx=5, pady=5)

        button = Button(self.player_check_in, text='OK')
        button.grid(row=2, column=0, columnspan=2)
        button.bind("<Button-1>", self.save_player)

    def about_info(self):
        showinfo('About', "The game Stability is developed for you\n to design steel frame structure by yourself.")

    def exit_button(self):  # Exit the Game
        self.window.quit()

    def create_menu(self):  # Menu Bar for Main Interface
        menu_bar = Menu(self.window)
        self.window.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # File Menu
        file_menu.add_command(label="New Player", command=self.create_player)

        file_menu.add_separator()

        file_menu.add_command(label="Exit", command=self.exit_button)

        # Help Menu
        help_menu.add_command(label="About", command=self.about_info)

    def create_component(self):
        return None
