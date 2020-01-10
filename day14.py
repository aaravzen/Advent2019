import math
TRILLION = 1000000000000

def get_chemical_map():
    chemical_to_info = {}
    fname = "Input/14.1.in"
    for line in open(fname):
        line = line.strip()
        i,o = line.split(" => ")
        ia = i.split(", ")
        
        ia = [(int(a.split()[0]), a.split()[1]) for a in ia]
        
        elem = o.split()[1]
        count = int(o.split()[0])
        t = (count, ia)
        chemical_to_info[elem] = t
    return chemical_to_info

def solve(required):
    m = get_chemical_map()
    extra = {}
    ore_count = 0
    while required:
        count,out = required.pop()
        if out in extra:
            if count < extra[out]:
                extra[out] -= count
                continue
            elif count == extra[out]:
                del extra[out]
                continue
            else:
                count -= extra[out]
                del extra[out]
        makes,ins = m[out]

        mult = 1
        if makes < count:
            mult = int(math.ceil(float(count) / makes))
        
        if makes * mult > count:
            extra[out] = makes * mult - count

        for num,i in ins:
            if i == "ORE":
                ore_count += num*mult
            else:
                required.append((num*mult,i))
    
    return ore_count

def part1():
    print(solve([(1, "FUEL")]))

def part2():
    low = 0
    high = 10000000000
    while low + 1 < high:
        mid = (high + low) // 2
        if solve([(mid, "FUEL")]) < TRILLION:
            low = mid
        else:
            high = mid - 1
    
    if solve([(high, "FUEL")]) < TRILLION:
        print(high)
    else:
        print(low)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()