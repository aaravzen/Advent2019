class Planet:
    def __init__(self,x,y,z):
        self.position = [x,y,z]
        self.velocity = [0,0,0]
    
    def apply_gravity(self, other):
        for i in xrange(3):
            if self.position[i] < other.position[i]:
                self.velocity[i] += 1
                other.velocity[i] -= 1
            elif self.position[i] > other.position[i]:
                self.velocity[i] -= 1
                other.velocity[i] += 1
    
    def apply_velocity(self):
        for i in xrange(3):
            self.position[i] += self.velocity[i]

    def get_kinetic_energy(self):
        return sum(abs(v) for v in self.velocity)
    
    def get_potential_energy(self):
        return sum(abs(p) for p in self.position)
    
    def get_energy(self):
        return self.get_potential_energy() * self.get_kinetic_energy()
    
    def hash(self):
        ret = "%d %d %d " % (tuple(x for x in self.position))
        ret += "%d %d %d" % (tuple(x for x in self.velocity))
        return ret

    def __repr__(self):
        ret = "<P>pos=<x=%d, y=%d, z=%d>" % (tuple(x for x in self.position))
        ret += ", vel=<x=%d, y=%d, z=%d>" % (tuple(x for x in self.velocity))
        ret += ", energy=%d</P>" % self.get_energy()
        return ret

def hash_planets(planets):
    rets = ["", "", ""]
    for p in planets:
        for i in xrange(3):
            rets[i] += "%d %d " % (p.position[i], p.velocity[i])
    return rets

def generate_planets():
    ret = []
    '''
    ret.append(Planet(-1, 0, 2))
    ret.append(Planet(2, -10, -7))
    ret.append(Planet(4, -8, 8))
    ret.append(Planet(3, 5, -1))
    '''
    '''
    ret.append(Planet(-8, -10, 0))
    ret.append(Planet(5, 5, 10))
    ret.append(Planet(2, -7, 3))
    ret.append(Planet(9, -8, -3))
    '''
    
    ret.append(Planet(19, -10, 7))
    ret.append(Planet(1, 2, -3))
    ret.append(Planet(14, -4, 1))
    ret.append(Planet(8, 7, -6))
    
    return ret

def part1():
    planets = generate_planets()
    for step in xrange(1000):
        #print("After %d steps:" % step)
        #print("\n".join(str(planet) for planet in planets))

        for i in xrange(len(planets)):
            for j in xrange(i+1, len(planets)):
                planets[i].apply_gravity(planets[j])
        
        for p in planets:
            p.apply_velocity()
    
    print("After %d steps:" % (step + 1))
    print("\n".join(str(planet) for planet in planets))
    print(sum(p.get_energy() for p in planets))

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def part2():
    sets = [{}, {}, {}]
    found = [False, False, False]
    planets = generate_planets()
    starts = [-1, -1, -1]
    lengths = [-1, -1, -1]

    for step in xrange(1000000):
        h = hash_planets(planets)
        #print(planets)
        #print(h)
        #break
        for i in xrange(3):
            if h[i] in sets[i] and not found[i]:
                starts[i] = sets[i][h[i]]
                lengths[i] = step - starts[i]
                found[i] = True
            else:
                sets[i][h[i]] = step

        #print("After %d steps:" % step)
        #print("\n".join(str(planet) for planet in planets))

        for i in xrange(len(planets)):
            for j in xrange(i+1, len(planets)):
                planets[i].apply_gravity(planets[j])
        
        for p in planets:
            p.apply_velocity()
        
        if all(found):
            print(starts)
            print(lengths)
            break
    
    m = 1
    for i in xrange(3):
        m = lcm(m, lengths[i])
    print("cycle-length %d, first repeat at %d" % (m, max(starts) + m))

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()