from computer import Computer

def get_blocks(output):
    count = 0
    while output:
        x,y,tile = output[:3]
        if tile == 2:
            count += 1
        output = output[3:]
    return count

def t(tile):
    if tile == 0:
        return " "
    elif tile == 1:
        return "W"
    elif tile == 2:
        return "*"
    elif tile == 3:
        return "-"
    elif tile == 4:
        return "o"

def display(output):
    minx = 0
    maxx = 0
    miny = 0
    maxy = 0
    things = {}
    while output:
        x,y,tile = output[:3]
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
        things[(x,y)] = tile
        output = output[3:]
    print("SCORE: %d" % things.get((-1,0),0))
    # print(things)
    ret = ""
    for i in xrange(maxy):
        for j in xrange(maxx):
            ret += t(things.get((j,i), 0))
        ret += "\n"
    print(ret)

def main():
    fname = "Input/13.1.in"
    arr = map(int, open(fname).readline().split(","))
    
    c = Computer(arr[:])
    ret, outputs, dump = c.run_computer()
    # part 1
    print(get_blocks(outputs))

    # part 2
    quarters = arr[:]
    quarters[0] = 2
    c = Computer(quarters)
    ret, outputs, dump = c.run_computer()
    display(outputs)
    while(True):
        try:
            move = {'a':-1,'s':0,'d':1,'':0}[raw_input()]
        except:
            continue
        ret, outputs, dump = c.continue_run([move])
        display(outputs)




if __name__=="__main__":
    main()