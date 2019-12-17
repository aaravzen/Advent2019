def check(number):
    s = str(number)
    curr = 0
    for digit in s:
        if int(digit) < curr:
            return False
        curr = int(digit)
    
    double = False
    for i in xrange(1,len(s)):
        if s[i-1] == s[i]:
            if i - 2 >= 0 and s[i-2] == s[i-1] or i + 1 < len(s) and s[i+1] == s[i]:
                pass
            else:
                double = True
    
    return double
    
def part1():
    count = 0
    for i in xrange(240920, 789857+1):
        if check(i):
            count += 1

    print(count)

def main():
    part1()

if __name__=="__main__":
    main()