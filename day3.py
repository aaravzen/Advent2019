def input():
    inp = open("3.1.in")
    wire_one_path = inp.readline()
    wire_two_path = inp.readline()

    print(wire_one_path)
    print(wire_two_path)
    return wire_one_path, wire_two_path

class PointMap:
    def __init__(self, wire):
        self.points = {}
        self.traveled = 0
        self.x = 0
        self.y = 0
        for instruction in wire.split(','):
            self.do_instruction(instruction)

    def do_instruction(self, instruction):
        # distance and direction
        distance, x_coord, direction = self.parse(instruction)
        for i in xrange(distance):
            if x_coord:
                self.x += 1 * direction
            else:
                self.y += 1 * direction
            # print("%d %d" % (self.x, self.y))
            t = (self.x, self.y)
            self.traveled += 1
            if t not in self.points:
                self.points[t] = self.traveled

    def parse(self, instruction):
        print(instruction)
        x_coord = True
        direction = 1
        letter = instruction[0]
        if letter == "R":
            pass
        elif letter == "U":
            x_coord = False
        elif letter == "D":
            direction = -1
            x_coord = False
        elif letter == "L":
            direction = -1
        distance = int(instruction[1:])
        return distance, x_coord, direction
    
    def get_closest_intersection(self, other):
        intersections = set(self.points.keys()).intersection(set(other.points.keys()))
        best = 99999999
        for intersection in intersections:
            # delta = abs(intersection[0]) + abs(intersection[1])
            delta = self.points[intersection] + other.points[intersection]
            if delta < best:
                best = delta
        print(best)


def get_closest_hub(pm1, pm2):
    pass

def main():
    w1,w2 = input()
    pm1 = PointMap(w1)
    pm2 = PointMap(w2)
    pm1.get_closest_intersection(pm2)

main()