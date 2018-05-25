from MembersParent import MembersParent


def getmember():
    f = open("Members_info.txt", 'r+')

    members = []

    oneline = f.readline()

    try:
        while len(oneline) != 0:
            members_item = oneline.split(',')
            new_member = MembersParent(float(members_item[0]),float(members_item[1]),float(members_item[2]),
                                      float(members_item[3]),float(members_item[4]),float(members_item[5]),
                                      int(members_item[6]))
            members.append(new_member)
            oneline = f.readline()
    except:
        print

    m = []

    for member in members:
        a = [member.beam_width, member.beam_height, member.beam_length,
             member.column_width, member.column_thickness, member.column_height,
             member.numbers_of_level]
        m.append(a)

    return m


def members_list():
    ll = len(getmember()) - 1
    member_list = [getmember()[ll][0], getmember()[ll][1], getmember()[ll][2],
                   getmember()[ll][3], getmember()[ll][4], getmember()[ll][5],
                   getmember()[ll][6]]
    return member_list
