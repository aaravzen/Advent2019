def get_asteroids(fname):
    asteroids = []
    for i,line in enumerate(open(fname)):
        for j,char in enumerate(line):
            if char == "#":
                t = (j,i)
                asteroids.append(t)
    return asteroids

def calculate_best_position(asteroids):
    best = 0
    coords = None
    best_slopes = None
    for a1 in asteroids:
        slopes = {}
        for a2 in asteroids:
            if a1[0] == a2[0] and a1[1] == a2[1]:
                continue
            
            try:
                s = -float(a2[1]-a1[1]) / float(a2[0]-a1[0])
            except:
                s = 9999999
            t = (s, a2[0] >= a1[0], a2[0] == a1[0] and a2[1] > a1[1])
            
            if t in slopes:
                slopes[t].append(a2)
                slopes[t].sort(key=lambda a: (a[0]-a1[0])*(a[0]-a1[0]) + (a[1]-a1[1])*(a[1]-a1[1]))
            else:
                slopes[t] = [a2]

        if len(slopes) > best:
            best = len(slopes)
            coords = a1
            best_slopes = slopes

    return best, coords, best_slopes

def sort_slopes(slopes):
    slopes.sort(key=lambda a: (-a[0][0]))
    slopes.sort(key=lambda a: (a[0][2]))
    slopes.sort(key=lambda a: (not a[0][1]))
    # print("\n".join(str(x) for x in slopes))
    return slopes

def calc_xth_destroyed(coords, slopes, x):
    while x >= len(slopes):
        x -= len(slopes)
        slopes = map(lambda t: (t[0], t[1][1:]), slopes)
        slopes = [s for s in slopes if s[1] and len(s[1]) > 0]
    
    slopes = sort_slopes(slopes)
    return slopes[x][1][0]

def main():
    fname = "Input/10.1.in"
    asteroids = get_asteroids(fname)
    best,position,slopes = calculate_best_position(asteroids)
    print(best)
    
    xth = 200
    coords = calc_xth_destroyed(position, list(slopes.items()), xth - 1)
    print("%d: %s. Ans = %d" % (xth, coords, coords[0]*100+coords[1]))

if __name__ == "__main__":
    main()