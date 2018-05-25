from Tkinter import *
from app_calc import *
# from tkFileDialog import *


class CalculateResult:
    def __init__(self):
        self.analysis_result = None
        self.cm10 = check_moment()
        self.cs10 = check_shear()
        self.ca10 = check_axial()
        self.m10 = moment_results()
        self.s10 = shear_results()
        self.a10 = axial_results()

        self.color = []
        self.advice_text = ""

    def save_as(self):
        save_txt()

    def finish_analysis(self):
        self.analysis_result.destroy()

    def value_color(self):
        if self.cm10[0] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.cs10[0] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.ca10[0] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.cm10[1] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.cs10[1] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.ca10[1] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.cm10[2] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.cs10[2] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.ca10[2] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.cm10[3] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.cs10[3] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.ca10[3] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.cm10[4] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.cs10[4] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

        if self.ca10[4] == 1:
            self.color.append('black')
        else:
            self.color.append('red')

    def good_or_bad(self):
        text = []
        a1 = 1
        a2 = 1
        a3 = 1
        t1 = "Moment is OK.\n"
        t2 = "Shear force is OK.\n"
        t3 = "Axial force is OK.\n"

        for i in self.cm10:
            if i == 0:
                t1 = "Type 1 Beam Error: You are supposed to choose shorter beam with larger section area.\n"
                a1 = 0

        for i in self.cs10:
            if i == 0:
                t2 = "Type 2 Beam Error: You are supposed to choose larger section area of beam and try again.\n"
                a2 = 0

        for i in self.ca10:
            if i == 0:
                t3 = "Column Error: You are supposed to increase section area of column and try again.\n"
                a3 = 0

        text.append(t1)
        text.append(t2)
        text.append(t3)

        a = a1 + a2 + a3

        if a < 3:
            self.advice_text = text[0] + text[1] + text[2]
        else:
            self.advice_text = "You have done a great job in structure design."

    def result_interface(self):
        self.analysis_result = Toplevel()
        self.analysis_result.title('Result')

        w = 550
        h = 280
        sw = self.analysis_result.winfo_screenwidth()
        sh = self.analysis_result.winfo_screenheight()

        # Position of Result Interface
        x = (sw / 2) - (w / 2)
        y = (sh / 2) - (h / 2)

        self.analysis_result.geometry('%dx%d+%d+%d' % (w, h, x, y))

        floor_number = Label(self.analysis_result, text="Floor #")
        floor_number.grid(row=0, column=0, rowspan=2)

        first_floor = Label(self.analysis_result, text="Floor 1")
        first_floor.grid(row=2, column=0)

        second_floor = Label(self.analysis_result, text="Floor 2")
        second_floor.grid(row=3, column=0)

        third_floor = Label(self.analysis_result, text="Floor 3")
        third_floor.grid(row=4, column=0)

        fourth_floor = Label(self.analysis_result, text="Floor 4")
        fourth_floor.grid(row=5, column=0)

        fifth_floor = Label(self.analysis_result, text="Floor 5")
        fifth_floor.grid(row=6, column=0)

        beam_force = Label(self.analysis_result, text='Beam')
        beam_force.grid(row=0, column=1, columnspan=2)

        column_force = Label(self.analysis_result, text='Column')
        column_force.grid(row=0, column=3)

        bending_moment = Label(self.analysis_result, text='Moment (kip*ft)  ')
        bending_moment.grid(row=1, column=1)

        shear_force = Label(self.analysis_result, text='Shear Force (kip)  ')
        shear_force.grid(row=1, column=2)

        axial_force = Label(self.analysis_result, text='Axial Force (kip)')
        axial_force.grid(row=1, column=3)

        # Check all the forces
        self.value_color()

        bending_moment_1 = Label(self.analysis_result, text=self.m10[0], fg=self.color[0])
        bending_moment_1.grid(row=2, column=1)

        shear_force_1 = Label(self.analysis_result, text=self.s10[0], fg=self.color[1])
        shear_force_1.grid(row=2, column=2)

        axial_force_1 = Label(self.analysis_result, text=self.a10[0], fg=self.color[2])
        axial_force_1.grid(row=2, column=3)

        bending_moment_2 = Label(self.analysis_result, text=self.m10[1], fg=self.color[3])
        bending_moment_2.grid(row=3, column=1)

        shear_force_2 = Label(self.analysis_result, text=self.s10[1], fg=self.color[4])
        shear_force_2.grid(row=3, column=2)

        axial_force_2 = Label(self.analysis_result, text=self.a10[1], fg=self.color[5])
        axial_force_2.grid(row=3, column=3)

        bending_moment_3 = Label(self.analysis_result, text=self.m10[2], fg=self.color[6])
        bending_moment_3.grid(row=4, column=1)

        shear_force_3 = Label(self.analysis_result, text=self.s10[2], fg=self.color[7])
        shear_force_3.grid(row=4, column=2)

        axial_force_3 = Label(self.analysis_result, text=self.a10[2], fg=self.color[8])
        axial_force_3.grid(row=4, column=3)

        bending_moment_4 = Label(self.analysis_result, text=self.m10[3], fg=self.color[9])
        bending_moment_4.grid(row=5, column=1)

        shear_force_4 = Label(self.analysis_result, text=self.s10[3], fg=self.color[10])
        shear_force_4.grid(row=5, column=2)

        axial_force_4 = Label(self.analysis_result, text=self.a10[3], fg=self.color[11])
        axial_force_4.grid(row=5, column=3)

        bending_moment_5 = Label(self.analysis_result, text=self.m10[4], fg=self.color[12])
        bending_moment_5.grid(row=6, column=1)

        shear_force_5 = Label(self.analysis_result, text=self.s10[4], fg=self.color[13])
        shear_force_5.grid(row=6, column=2)

        axial_force_5 = Label(self.analysis_result, text=self.a10[4], fg=self.color[14])
        axial_force_5.grid(row=6, column=3)

        # Show suggestion
        self.good_or_bad()

        suggestion = Label(self.analysis_result, text=self.advice_text)
        suggestion.grid(row=7, column=0, columnspan=4)

        save_button = Button(self.analysis_result, text="Save", command=self.save_as)
        save_button.grid(row=8, column=0, columnspan=2)

        okay_button = Button(self.analysis_result, text="OK", command=self.finish_analysis)
        okay_button.grid(row=8, column=2, columnspan=2)
