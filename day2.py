from computer import Computer

def main():
    fname = "Input/2.1.in"
    arr = map(int, open(fname).readline().split(","))
    
    for n in xrange(100):
        for v in xrange(100):
            c = Computer(arr[:])
            c.nounverb(n, v)
            ret,outputs,dump = c.run_computer()
            if n == 12 and v == 2:
                print("1202 run yields: %d" % ret)
            if ret == 19690720:
                print("Noun: %d / Verb: %d / Ans: %d" % (n,v, 100*n+v))

if __name__=="__main__":
    main()