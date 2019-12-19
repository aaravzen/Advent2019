from computer import Computer

def main():
    fname = "Input/9.1.in"
    arr = map(int, open(fname).readline().split(","))
    
    for i in xrange(1,3):
        c = Computer(arr[:])
        ret, outputs, dump = c.run_computer([i])
        print(outputs)

if __name__=="__main__":
    main()