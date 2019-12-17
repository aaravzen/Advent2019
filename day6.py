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
    return "Sum of all orbits: %d" % sum(counts.values())

def shortest_path(adj):
    start = adj["YOU"][0]
    end = adj["SAN"][0]
    visited = set()
    visited.add("YOU")
    visited.add("SAN")
    q = [start]
    jumps = 0
    while len(q) > 0:
        q2 = []
        while len(q) > 0:
            curr = q.pop()
            visited.add(curr)
            connected = adj[curr]
            for planet in connected:
                if planet in visited:
                    continue
                if planet == end:
                    return "%s to %s in %d jumps" % (start, end, jumps + 1)
                q2.append(planet)
        q = q2
        jumps += 1

def main():
    adj, counts = create_adjacency(open("Input/6.1.in"))
    generate_counts(adj, counts)
    print(sum_orbits(counts))
    print(shortest_path(adj))
    
if __name__=="__main__":
    main()