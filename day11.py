from computer import Computer
import time

def printf(str):
    pass
    # print(str)

class DIR:
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = DIR.UP
        self.coordinates = {}
    
    def paint(self, color):
        t = (self.x, self.y)
        self.coordinates[t] = color

    def move(self):
        if self.direction == DIR.UP:
            self.y += 1
            printf("up to %d %d" % (self.x, self.y))
        elif self.direction == DIR.DOWN:
            self.y -= 1
            printf("down to %d %d" % (self.x, self.y))
        elif self.direction == DIR.RIGHT:
            self.x += 1
            printf("right to %d %d" % (self.x, self.y))
        elif self.direction == DIR.LEFT:
            self.x -= 1
            printf("left to %d %d" % (self.x, self.y))
        
        t = (self.x, self.y)
        if t in self.coordinates:
            return self.coordinates[t]
        return 0

    def turn(self, direction):
        if direction == 0:
            self.direction += 3
        else:
            self.direction += 1
        self.direction %= 4

def part1(arr):
    c = Computer(arr[:])
    robot = Robot()
    c.run_computer([0])
    outputs = set()
    while c.can_continue:
        color,direction = c.outputs[-2:]
        outputs.add((color, direction))
        
        robot.paint(color)
        robot.turn(direction)
        new_panel = robot.move()
        c.continue_run([new_panel])
        
    print(len(robot.coordinates))

def paint_coordinates(coords):
    minx = maxx = miny = maxy = 0
    for coord in coords:
        minx = min(coord[0], minx)
        maxx = max(coord[0], maxx)
        miny = min(coord[1], miny)
        maxy = max(coord[1], maxy)

    plates = []
    for i in xrange(miny,maxy+1):
        line = ""
        for j in xrange(minx,maxx+1):
            t = (j, i)
            if t in coords and coords[t] == 1:
                line += "X"
            else:
                line += " "
        plates.append(line)

    print("\n".join(plate for plate in reversed(plates)))


def part2(arr):
    c = Computer(arr[:])
    robot = Robot()
    c.run_computer([1])
    outputs = set()
    while c.can_continue:
        color,direction = c.outputs[-2:]
        outputs.add((color, direction))
        
        robot.paint(color)
        robot.turn(direction)
        new_panel = robot.move()
        c.continue_run([new_panel])
    
    paint_coordinates(robot.coordinates)

def main():
    fname = "Input/11.1.in"
    arr = map(int, open(fname).readline().split(","))
    part1(arr)
    part2(arr)
    

if __name__=="__main__":
    main()