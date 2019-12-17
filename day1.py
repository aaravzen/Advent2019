def fuel(mass):
    return mass // 3 - 2

inp = open("Input/1.1.in")
l = []

for line in inp:
    l.append(int(line))

# print(l)

part_one = 0
part_two = 0
for x in l:
    f = fuel(x)
    part_one += f
    for_module = f
    while f >= 9:
        f = fuel(f)
        for_module += f
    part_two += for_module

print(part_one)
print(part_two)