def fuel(mass):
    return mass // 3 - 2

inp = open("1.1.in")
l = []

for line in inp:
    l.append(int(line))
#l = [100756]

print(l)

total = 0
for x in l:
    f = fuel(x)
    for_module = f
    while f >= 9:
        f = fuel(f)
        for_module += f
    total += for_module

print(total)