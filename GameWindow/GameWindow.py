import ttk
from Tkinter import *
from tkMessageBox import *

from CalculateResult import CalculateResult
from GameCanvas import GameCanvas
from Menu.StabilityCanvas import CanvasGo
from Menu.StabilityWindow import Stability
from ParameterCheck import ParameterCheck
from app_calc import save_txt


class Game(Stability):
    def __init__(self):
        super(Game, self).__init__()
        self.game_interface = None
        self.game_canvas = None

        self.enter_player_ID = None
        self.Id = None
        self.pass_word = None
        self.a = None

        self.story_number = None
        self.story_height_number = None
        self.beam_length_number = None
        self.beam_width = None
        self.beam_height = None
        self.column_width = None
        self.column_thickness = None

        self.sn = None
        self.shn = None
        self.bln = None

        self.result = None

        self.calculate_button = None

        self.key = 0

    def check_player(self, event):
        m = self.Id.get()
        n = self.pass_word.get()
        f = open("UserInfo.txt", "r+")
        one_line = f.readline()
        while len(one_line) != 0:
            self.a = 0
            i = one_line.split(',')
            j = i[1].splitlines()
            if m == i[0] and n == j[0]:
                self.window.withdraw()
                self.enter_player_ID.destroy()
                self.open_game_window()
                break
            else:
                self.a += 1
                one_line = f.readline()
        if self.a != 0:
            showwarning("Oops", "Your ID or password may not be correct!\n"
                                "Try again, please.")

    def enter_ID(self):
        self.window.iconify()
        self.enter_player_ID = Toplevel()
        self.enter_player_ID.title('Info Check')
        self.enter_player_ID.geometry("270x120+500+250")

        label1 = Label(self.enter_player_ID, text='ID')
        label1.grid(row=0, column=0, padx=10, pady=10)

        n = StringVar()
        self.Id = Entry(self.enter_player_ID, textvariable=n)
        self.Id.grid(row=0, column=1, padx=5, pady=5)

        label2 = Label(self.enter_player_ID, text='Password')
        label2.grid(row=1, column=0, padx=10, pady=10)

        pw = StringVar()
        self.pass_word = Entry(self.enter_player_ID, textvariable=pw)
        self.pass_word.grid(row=1, column=1, padx=5, pady=5)

        button = Button(self.enter_player_ID, text='Enter')
        button.grid(row=2, column=0, columnspan=2)
        button.bind("<Button-1>", self.check_player)

    def open_game_window(self):
        self.game_window()

    def get_structure(self):  # Get component information of structure
        try:
            sn = int(self.story_number.get())
            shn = float(self.story_height_number.get())
            bln = float(self.beam_length_number.get())
            bw = float(self.beam_width.get())
            bh = float(self.beam_height.get())
            cw = float(self.column_width.get())
            ct = float(self.column_thickness.get())

            pc = ParameterCheck()
            self.sn = pc.check_story_number(sn)
            self.shn = pc.check_story_height(shn)
            self.bln = pc.check_beam_length(bln)
            bw = pc.check_beam_width(bw)
            bh = pc.check_beam_height(bh)
            cw = pc.check_column_width(cw)
            ct = pc.check_column_thickness(ct)

            pc.check_warning()

            if pc.error == 0:
                self.calculate_button['state'] = 'normal'

                f = open('Members_info.txt', 'r+')
                f.seek(0, 2)
                f.write(str(bw)+','+str(bh)+','+str(self.bln)+','+str(cw)+','+str(ct)+','+str(self.shn)+','+str(self.sn)+'\n')

                showinfo('God Job', "Information has been checked.\n"
                                    "Now you can build your structure on left.")

                self.game_canvas.Click = None
                self.game_canvas.bind("<Button-1>", self.canvas_clicked)
        except ValueError:
            showwarning("Warning", "You must check whether you enter a correct number in each box.")

    def calculate_result(self):  # Force Analysis
        self.result = CalculateResult()
        self.result.result_interface()
        self.key = 1
        self.calculate_button['state'] = 'disabled'

    def clear_canvas(self):  # Clear canvas to redesign the structure
        self.game_canvas.delete('all')
        self.game_canvas.game_background()

    def canvas_clicked(self, event):  # Visualize structure on canvas
        self.clear_canvas()
        self.game_canvas.Click = [event.x, event.y]
        self.game_canvas.draw_structure(self.sn, self.shn, self.bln)

    def save_file(self):
        if self.key == 0:
            showinfo("Attention", "You do not have any analysis result yet.")
        else:
            save_txt()
            self.key = 0

    def back_game(self):  # Exit the Game; Back to Main Interface
        self.game_interface.destroy()
        self.window.update()
        self.window.deiconify()

    def game_info(self):
        showinfo('About', "The game Stability is developed for you\n to design steel frame structure by yourself.")

    def game_window(self):
        self.game_interface = Toplevel()
        self.game_interface.title('Stability')

        w = 1080
        h = 540
        sw = self.game_interface.winfo_screenwidth()
        sh = self.game_interface.winfo_screenheight()

        # Position of Game Interface
        x = (sw / 2) - (w / 2)
        y = (sh / 2) - (h / 2)

        self.game_interface.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.game_canvas = GameCanvas(self.game_interface, 640, 540, "white")
        self.game_canvas.grid(row=0, column=0, rowspan=11, sticky='NW')
        self.game_canvas.game_background()

        # Choose number of story
        story = Label(self.game_interface, text="Number of Story")
        story.grid(row=0, column=1)

        s = StringVar()
        self.story_number = ttk.Combobox(self.game_interface, textvariable=s)
        self.story_number['values'] = (1, 2, 3, 4, 5)
        self.story_number.grid(row=0, column=2, columnspan=6)

        # Decide height of one story, aka length of column
        story_height = Label(self.game_interface, text="Story Height")
        story_height.grid(row=1, column=1)

        sh = StringVar()
        self.story_height_number = Entry(self.game_interface, textvariable=sh)
        self.story_height_number.grid(row=1, column=2, columnspan=6)

        sh_unit = Label(self.game_interface, text='ft.')
        sh_unit.grid(row=1, column=7)

        sh_note = Label(self.game_interface, text='(Range of Height Value: [8, 15])')
        sh_note.grid(row=2, column=2, columnspan=6)

        # Decide length of beam
        beam_length = Label(self.game_interface, text="Length of Beam")
        beam_length.grid(row=3, column=1)

        bl = StringVar()
        self.beam_length_number = Entry(self.game_interface, textvariable=bl)
        self.beam_length_number.grid(row=3, column=2, columnspan=6)

        bl_unit = Label(self.game_interface, text='ft.')
        bl_unit.grid(row=3, column=7)

        sh_note = Label(self.game_interface, text='(Range of Length Value: [10, 25])')
        sh_note.grid(row=4, column=2, columnspan=6)

        # Parameters(width and height) of beam section
        sb = Label(self.game_interface, text="Section of Beam")
        sb.grid(row=5, column=1)

        wb = Label(self.game_interface, text="width")
        wb.grid(row=6, column=1)

        bw = StringVar()
        self.beam_width = ttk.Combobox(self.game_interface, textvariable=bw, width=5)
        self.beam_width['values'] = (10, 15, 20, 25, 30, 35, 40)
        self.beam_width.grid(row=6, column=2)

        bw_unit = Label(self.game_interface, text='in.   ')
        bw_unit.grid(row=6, column=3, columnspan=2)

        hb = Label(self.game_interface, text="height      ")
        hb.grid(row=6, column=5)

        bh = StringVar()
        self.beam_height = ttk.Combobox(self.game_interface, textvariable=bh, width=5)
        self.beam_height['values'] = (15, 20, 25, 30, 35, 40, 45, 50, 55, 60)
        self.beam_height.grid(row=6, column=6)

        bh_unit = Label(self.game_interface, text='   in.')
        bh_unit.grid(row=6, column=7)

        # Parameters(width and thickness) of column section
        sc = Label(self.game_interface, text="Section of Column")
        sc.grid(row=7, column=1)

        wc = Label(self.game_interface, text="width")
        wc.grid(row=8, column=1)

        cw = StringVar()
        self.column_width = ttk.Combobox(self.game_interface, textvariable=cw, width=5)
        self.column_width['values'] = (10, 20, 30, 40)
        self.column_width.grid(row=8, column=2)

        cw_unit = Label(self.game_interface, text='in.   ')
        cw_unit.grid(row=8, column=3, columnspan=2)

        tc = Label(self.game_interface, text="thickness      ")
        tc.grid(row=8, column=5)

        ct = StringVar()
        self.column_thickness = ttk.Combobox(self.game_interface, textvariable=ct, width=5)
        self.column_thickness['values'] = (10, 20, 30, 40)
        self.column_thickness.grid(row=8, column=6)

        ct_unit = Label(self.game_interface, text='   in.')
        ct_unit.grid(row=8, column=7)

        # Buttons for calculation
        confirm_button = Button(self.game_interface, text='Confirm', command=self.get_structure)
        confirm_button.grid(row=9, column=1, columnspan=2)

        self.calculate_button = Button(self.game_interface, text='Calculate', state=DISABLED, command=self.calculate_result)
        self.calculate_button.grid(row=9, column=3, columnspan=2)

        clear_button = Button(self.game_interface, text='Clear', command=self.clear_canvas)
        clear_button.grid(row=9, column=5, columnspan=3)

        # Notation for players
        remark_label = Label(self.game_interface, text="DO REMEMBER:\n"
                                                       "\n"
                                                       "Only building a structure of more than three stories\n"
                                                       "that also pass force analysis can you build a strong structure!\n"
                                                       "\n"
                                                       "Try your best!!!")
        remark_label.grid(row=10, column=1, columnspan=7)

        # Menu Bar for Game Interface
        menu_bar = Menu(self.game_interface)
        self.game_interface.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # File Menu
        file_menu.add_command(label="Save as...", command=self.save_file)

        file_menu.add_separator()

        file_menu.add_command(label="Back", command=self.back_game)

        # Help Menu
        help_menu.add_command(label="About", command=self.game_info)

    def create_component(self):
        # Create canvas to beautify main interface
        self.canvas = CanvasGo(self.window, 960, 540, 'white')
        self.canvas.pack()

        self.canvas.interface_image()
        self.canvas.interface_name()

        # Create buttons for players to use
        self.start_game = Button(self.window, text='Start', font=('GothicE', 20), command=self.enter_ID)
        self.start_game.place(x=430, y=340, width=100, height=30)

        self.exit_game = Button(self.window, text='Exit', font=('GothicE', 20), command=self.exit_button)
        self.exit_game.place(x=430, y=400, width=100, height=30)
