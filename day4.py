def check(number, part):
    s = str(number)
    curr = 0
    for digit in s:
        if int(digit) < curr:
            return False
        curr = int(digit)
    
    double = False
    for i in xrange(1,len(s)):
        if s[i-1] == s[i]:
            # part 1 logic
            if part == 0: return True
            
            # part 2 logic
            if i - 2 >= 0 and s[i-2] == s[i-1] or i + 1 < len(s) and s[i+1] == s[i]:
                pass
            else:
                double = True
    
    return double
    
def dobothparts():
    counts = [0, 0]
    for i in xrange(240920, 789857+1):
        for j in xrange(2):
            if check(i, j):
                counts[j] += 1
    print("\n".join(str(c) for c in counts))

def main():
    dobothparts()

if __name__=="__main__":
    main()