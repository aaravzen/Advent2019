IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6
IMAGE_SIZE = IMAGE_WIDTH * IMAGE_HEIGHT

def calc_layer(flat):
    zeroes = flat.count(0)
    ones = flat.count(1)
    twos = flat.count(2)
    return zeroes,ones * twos

def part1(data):
    lowest_zeroes = 9999999
    score = -1
    while data:
        z,s = calc_layer(data[:IMAGE_SIZE])
        if z < lowest_zeroes:
            lowest_zeroes = z
            score = s 
        data = data[IMAGE_SIZE:]
    print("The best layer had %d zeroes and a score of %d" % (lowest_zeroes, score))

def print_stacked(layer):
    s = ""
    for i,p in enumerate(layer):
        if i % IMAGE_WIDTH == 0:
            s += "\n"
        s += str(p)
    print(s.replace("0"," "))

def part2(data):
    top = data[:IMAGE_SIZE]
    while data:
        layer = data[:IMAGE_SIZE]
        for i in xrange(IMAGE_SIZE):
            if top[i] == 2:
                top[i] = layer[i]
        data = data[IMAGE_SIZE:]
    print_stacked(top)

def main():
    fname = "Input/8.1.in"
    raw_data = map(int, open(fname).readline().strip())
    #print(raw_data)
    #print(len(raw_data))
    part1(raw_data[:])
    part2(raw_data[:])

    

if __name__ == "__main__":
    main()