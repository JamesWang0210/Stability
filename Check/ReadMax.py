from CheckMax_B import CheckMax_B
from CheckMax_C import CheckMax_C


def get_beamvalues():
    f = open("beam_maximum_value.txt", 'r')

    beam_values = []

    oneline = f.readline()

    try:
        while len(oneline) != 0:
            beam_value_item = oneline.split(',')
            new_beam_values = CheckMax_B(float(beam_value_item[0]), float(beam_value_item[1]),
                                         float(beam_value_item[2]), float(beam_value_item[3]))
            beam_values.append(new_beam_values)
            oneline = f.readline()
    except:
        print

    bv = []
    for beam_value in beam_values:
        a = [beam_value.bw, beam_value.bh, beam_value.Vm, beam_value.Mm]
        bv.append(a)

    return bv


def get_columnvalues():
    f = open("column_maximum_value.txt", 'r')

    column_values = []

    oneline = f.readline()

    try:
        while len(oneline) != 0:
            column_value_item = oneline.split(',')
            new_column_values = CheckMax_C(float(column_value_item[0]), float(column_value_item[1]),
                                           float(column_value_item[2]))
            column_values.append(new_column_values)
            oneline = f.readline()
    except:
        print

    cv = []
    for column_value in column_values:
        a = [column_value.cw,column_value.ct,column_value.a]
        cv.append(a)

    return cv
