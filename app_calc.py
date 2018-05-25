from Members.ReadMembers import *
from Members.Beam import Beam
from Members.Column import Column
from Check.ReadMax import *

from Tkinter import *
from tkFileDialog import *


# Check the beams
def check_moment():
    a = members_list()

    B = Beam()
    B.beam_width = a[0]
    B.beam_height = a[1]
    B.beam_length = a[2]
    B.numbers_of_level = a[6]

    C = Column()
    C.column_width = a[3]
    C.column_thickness = a[4]
    C.column_height = a[5]
    C.numbers_of_level = a[6]

    B.weight_from_beam = B.beam_weight()
    B.weight_from_column = C.column_weight()

    C.weight_from_beam = B.beam_weight()
    C.weight_from_column = C.column_weight()

    b_list = get_beamvalues()
    c_list = get_columnvalues()

    n = B.numbers_of_level

    l = [1, 1, 1, 1, 1]
    for i in range(0, len(b_list)):

        bw = b_list[i][0]
        bh = b_list[i][1]
        V = b_list[i][2]
        M = b_list[i][3]

        if n == 1:
            if bw == B.beam_width and bh == B.beam_height:
                if M <= B.beam_moment_5():
                    l[0] = 0

        elif n == 2:
            if bw == B.beam_width and bh == B.beam_height:
                if M <= B.beam_moment_5():
                    l[1] = 0
                if M <= B.beam_moment_4():
                    l[0] = 0

        elif n == 3:
            if bw == B.beam_width and bh == B.beam_height:
                if M <= B.beam_moment_5():
                    l[2] = 0
                if M <= B.beam_moment_4():
                    l[1] = 0
                if M <= B.beam_moment_3():
                    l[0] = 0

        elif n == 4:
            if bw == B.beam_width and bh == B.beam_height:
                if M <= B.beam_moment_5():
                    l[3] = 0
                if M <= B.beam_moment_4():
                    l[2] = 0
                if M <= B.beam_moment_3():
                    l[1] = 0
                if M <= B.beam_moment_2():
                    l[0] = 0

        elif n == 5:
            if bw == B.beam_width and bh == B.beam_height:
                if M <= B.beam_moment_5():
                    l[4] = 0
                if M <= B.beam_moment_4():
                    l[3] = 0
                if M <= B.beam_moment_3():
                    l[2] = 0
                if M <= B.beam_moment_2():
                    l[1] = 0
                if M <= B.beam_moment_1():
                    l[0] = 0
    return l


def check_shear():
    a = members_list()

    B = Beam()
    B.beam_width = a[0]
    B.beam_height = a[1]
    B.beam_length = a[2]
    B.numbers_of_level = a[6]

    C = Column()
    C.column_width = a[3]
    C.column_thickness = a[4]
    C.column_height = a[5]
    C.numbers_of_level = a[6]

    B.weight_from_beam = B.beam_weight()
    B.weight_from_column = C.column_weight()

    C.weight_from_beam = B.beam_weight()
    C.weight_from_column = C.column_weight()

    b_list = get_beamvalues()
    c_list = get_columnvalues()

    n = B.numbers_of_level

    l = [1, 1, 1, 1, 1]
    for i in range(0, len(b_list)):

        bw = b_list[i][0]
        bh = b_list[i][1]
        V = b_list[i][2]
        M = b_list[i][3]

        if n == 1:
            if bw == B.beam_width and bh == B.beam_height:
                if V <= B.beam_shear_5():
                    l[0] = 0

        elif n == 2:
            if bw == B.beam_width and bh == B.beam_height:
                if V <= B.beam_shear_5():
                    l[1] = 0
                if V <= B.beam_shear_4():
                    l[0] = 0

        elif n == 3:
            if bw == B.beam_width and bh == B.beam_height:
                if V <= B.beam_shear_5():
                    l[2] = 0
                if V <= B.beam_shear_4():
                    l[1] = 0
                if V <= B.beam_shear_3():
                    l[0] = 0

        elif n == 4:
            if bw == B.beam_width and bh == B.beam_height:
                if V <= B.beam_shear_5():
                    l[3] = 0
                if V <= B.beam_shear_4():
                    l[2] = 0
                if V <= B.beam_shear_3():
                    l[1] = 0
                if V <= B.beam_shear_2():
                    l[0] = 0

        elif n == 5:
            if bw == B.beam_width and bh == B.beam_height:
                if V <= B.beam_shear_5():
                    l[4] = 0
                if V <= B.beam_shear_4():
                    l[3] = 0
                if V <= B.beam_shear_3():
                    l[2] = 0
                if V <= B.beam_shear_2():
                    l[1] = 0
                if V <= B.beam_shear_1():
                    l[0] = 0
    return l


# Check the columns
def check_axial():
    a = members_list()

    B = Beam()
    B.beam_width = a[0]
    B.beam_height = a[1]
    B.beam_length = a[2]
    B.numbers_of_level = a[6]

    C = Column()
    C.column_width = a[3]
    C.column_thickness = a[4]
    C.column_height = a[5]
    C.numbers_of_level = a[6]

    B.weight_from_beam = B.beam_weight()
    B.weight_from_column = C.column_weight()

    C.weight_from_beam = B.beam_weight()
    C.weight_from_column = C.column_weight()

    b_list = get_beamvalues()
    c_list = get_columnvalues()

    n = B.numbers_of_level

    l = [1, 1, 1, 1, 1]
    for k in range(0, len(c_list)):
        cw = c_list[k][0]
        ct = c_list[k][1]
        a = c_list[k][2]

        if n == 1:
            if cw == C.column_width and ct == C.column_thickness:
                if a <= C.column_axial_5():
                    l[0] = 0

        elif n == 2:
            if cw == C.column_width and ct == C.column_thickness:
                if a <= C.column_axial_5():
                    l[1] = 0
                if a <= C.column_axial_4():
                    l[0] = 0

        elif n == 3:
            if cw == C.column_width and ct == C.column_thickness:
                if a <= C.column_axial_5():
                    l[2] = 0
                if a <= C.column_axial_4():
                    l[1] = 0
                if a <= C.column_axial_3():
                    l[0] = 0

        elif n == 4:
            if cw == C.column_width and ct == C.column_thickness:
                if a <= C.column_axial_5():
                    l[3] = 0
                if a <= C.column_axial_4():
                    l[2] = 0
                if a <= C.column_axial_3():
                    l[1] = 0
                if a <= C.column_axial_2():
                    l[0] = 0

        elif n == 5:
            if cw == C.column_width and ct == C.column_thickness:
                if a <= C.column_axial_5():
                    l[4] = 0
                if a <= C.column_axial_4():
                    l[3] = 0
                if a <= C.column_axial_3():
                    l[2] = 0
                if a <= C.column_axial_2():
                    l[1] = 0
                if a <= C.column_axial_1():
                    l[0] = 0
    return l


def moment_results():
    a = members_list()

    B = Beam()
    B.beam_width = a[0]
    B.beam_height = a[1]
    B.beam_length = a[2]
    B.numbers_of_level = a[6]

    C = Column()
    C.column_width = a[3]
    C.column_thickness = a[4]
    C.column_height = a[5]
    C.numbers_of_level = a[6]

    B.weight_from_beam = B.beam_weight()
    B.weight_from_column = C.column_weight()

    C.weight_from_beam = B.beam_weight()
    C.weight_from_column = C.column_weight()

    n = B.numbers_of_level

    if n == 1:
        a = ['%.2f' % B.beam_moment_5(), 0, 0, 0, 0]
        return a

    if n == 2:
        a = ['%.2f' % B.beam_moment_4(), '%.2f' % B.beam_moment_5(), 0, 0, 0]
        return a

    if n == 3:
        a = ['%.2f' % B.beam_moment_3(), '%.2f' % B.beam_moment_4(), '%.2f' % B.beam_moment_5(), 0, 0]
        return a

    if n == 4:
        a = ['%.2f' % B.beam_moment_2(), '%.2f' % B.beam_moment_3(), '%.2f' % B.beam_moment_4(),
             '%.2f' % B.beam_moment_5(), 0]
        return a

    if n == 5:
        a = ['%.2f' % B.beam_moment_1(), '%.2f' % B.beam_moment_2(), '%.2f' % B.beam_moment_3(),
             '%.2f' % B.beam_moment_4(), '%.2f' % B.beam_moment_5()]
        return a


def shear_results():
    a = members_list()

    B = Beam()
    B.beam_width = a[0]
    B.beam_height = a[1]
    B.beam_length = a[2]
    B.numbers_of_level = a[6]

    C = Column()
    C.column_width = a[3]
    C.column_thickness = a[4]
    C.column_height = a[5]
    C.numbers_of_level = a[6]

    B.weight_from_beam = B.beam_weight()
    B.weight_from_column = C.column_weight()

    C.weight_from_beam = B.beam_weight()
    C.weight_from_column = C.column_weight()

    n = B.numbers_of_level

    if n == 1:
        a = ['%.2f' % B.beam_shear_5(), 0, 0, 0, 0]
        return a

    if n == 2:
        a = ['%.2f' % B.beam_shear_4(), '%.2f' % B.beam_shear_5(), 0, 0, 0]
        return a

    if n == 3:
        a = ['%.2f' % B.beam_shear_3(), '%.2f' % B.beam_shear_4(), '%.2f' % B.beam_shear_5(), 0, 0]
        return a

    if n == 4:
        a = ['%.2f' % B.beam_shear_2(), '%.2f' % B.beam_shear_3(), '%.2f' % B.beam_shear_4(),
             '%.2f' % B.beam_shear_5(), 0]
        return a

    if n == 5:
        a = ['%.2f' % B.beam_shear_1(), '%.2f' % B.beam_shear_2(), '%.2f' % B.beam_shear_3(),
             '%.2f' % B.beam_shear_4(), '%.2f' % B.beam_shear_5()]
        return a


def axial_results():
    a = members_list()

    B = Beam()
    B.beam_width = a[0]
    B.beam_height = a[1]
    B.beam_length = a[2]
    B.numbers_of_level = a[6]

    C = Column()
    C.column_width = a[3]
    C.column_thickness = a[4]
    C.column_height = a[5]
    C.numbers_of_level = a[6]

    B.weight_from_beam = B.beam_weight()
    B.weight_from_column = C.column_weight()

    C.weight_from_beam = B.beam_weight()
    C.weight_from_column = C.column_weight()

    n = B.numbers_of_level

    if n == 1:
        a = ['%.2f' % C.column_axial_5(), 0, 0, 0, 0]
        return a

    if n == 2:
        a = ['%.2f' % C.column_axial_4(), '%.2f' % C.column_axial_5(), 0, 0, 0]
        return a

    if n == 3:
        a = ['%.2f' % C.column_axial_3(), '%.2f' % C.column_axial_4(), '%.2f' % C.column_axial_5(), 0, 0]
        return a

    if n == 4:
        a = ['%.2f' % C.column_axial_2(), '%.2f' % C.column_axial_3(), '%.2f' % C.column_axial_4(),
             '%.2f' % C.column_axial_5(), 0]
        return a

    if n == 5:
        a = ['%.2f' % C.column_axial_1(), '%.2f' % C.column_axial_2(), '%.2f' % C.column_axial_3(),
             '%.2f' % C.column_axial_4(), '%.2f' % C.column_axial_5()]
        return a


def save_txt():
    text_file = Text()
    save_file = asksaveasfile(mode='w', defaultextension=".txt")
    text_save = str(text_file.get(0.0, END))
    save_file.write(text_save)
    save_file.close()

    f = open(save_file.name, 'w')

    a = members_list()

    B = Beam()
    B.beam_width = a[0]
    B.beam_height = a[1]
    B.beam_length = a[2]
    B.numbers_of_level = a[6]

    C = Column()
    C.column_width = a[3]
    C.column_thickness = a[4]
    C.column_height = a[5]
    C.numbers_of_level = a[6]

    B.weight_from_beam = B.beam_weight()
    B.weight_from_column = C.column_weight()

    C.weight_from_beam = B.beam_weight()
    C.weight_from_column = C.column_weight()

    n = B.numbers_of_level

    text = []
    text.append('Dimensions:')

    text1 = 'Beam Width: ' + str(B.beam_width) + ' in.' + '\n' +\
            'Beam Height: ' + str(B.beam_height) + ' in.'
    text2 = 'Column Width: ' + str(C.column_width) + ' in.' + '\n' +\
            'Column Height: ' + str(C.column_thickness) + ' in.'
    text3 = 'Levels: ' + str(n)

    text.append(text1)
    text.append(text2)
    text.append(text3)

    # Moment
    text.append('\n' + 'Moment:')

    m = moment_results()
    for i in range(1,len(m)+1):
        if m[i-1] != 0:
            text_m = 'Moment of beam on Floor' + str(i) + ' = ' + str(m[i-1]) + ' kip*ft'
            text.append(text_m)

    text.append('\n' + 'Shear force:')
    s = shear_results()
    for i in range(1,len(s)+1):
        if s[i-1] != 0:
            text_s = 'Shear force of beam on Floor' + str(i) + ' = ' + str(s[i-1]) + ' kip'
            text.append(text_s)

    text.append('\n' + 'Axial force:')
    a = axial_results()
    for i in range(1,len(a)+1):
        if a[i-1] != 0:
            text_a = 'Axial force of column on Floor' + str(i) + ' = ' + str(a[i-1]) + ' kip'
            text.append(text_a)

    for item in text:
        f.write("%s\n" % item)
