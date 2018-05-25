from Loads.Load import Load


def getloads():
    f = open("Loads_info.txt", 'r')

    loads = []

    oneline = f.readline()

    try:
        while len(oneline) != 0:
            loadsItem = oneline.split(',')
            newLoads = Load(int(loadsItem[0]),int(loadsItem[1]))
            loads.append(newLoads)
            oneline = f.readline()
    except:
        print

    for load in loads:
        return 1.6*load.live_load + 1.2*load.dead_load


def total_loads():  # kip
    return getloads()
