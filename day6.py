def create_adjacency(lines):
    adj = {}
    planet_counts = {}
    for line in lines:
        a,b = line.strip().split(")")
        if a in adj:
            adj[a].append(b)
        else:
            adj[a] = [b]

        if b in adj:
            adj[b].append(a)
        else:
            adj[b] = [a]

        planet_counts[b] = 0
        planet_counts[a] = 0
    return adj, planet_counts

def generate_counts(adj, m):
    q = ["COM"]
    orbits = 1
    visited = set()
    while len(q) > 0:
        q2 = []
        while len(q) > 0:
            curr = q.pop()
            visited.add(curr)
            connected = adj[curr]
            for planet in connected:
                if planet in visited:
                    continue
                m[planet] += orbits
                q2.append(planet)
        q = q2
        orbits += 1

def sum_orbits(counts):
    return sum(counts.values())

def shortest_path(adj):
    start = adj["YOU"][0]
    end = adj["SAN"][0]
    visited = set()
    visited.add("YOU")
    visited.add("SAN")
    q = [start]
    jumps = 0
    done = False
    while len(q) > 0:
        q2 = []
        while len(q) > 0:
            curr = q.pop()
            print("%s: %d" % (curr, jumps))
            visited.add(curr)
            connected = adj[curr]
            for planet in connected:
                if planet in visited:
                    continue
                if planet == end:
                    done = True
                    break
                q2.append(planet)
        q = q2
        jumps += 1
        if done: break
    print("%s to %s in %d jumps" % (start, end, jumps))
    

def main():
    adj, counts = create_adjacency(open("6.1.in"))
    generate_counts(adj, counts)
    # print(adj)
    # print(counts)
    print(sum_orbits(counts))
    shortest_path(adj)
    
if __name__=="__main__":
    main()