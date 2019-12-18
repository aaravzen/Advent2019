from computer import Computer

def main():
    fname = "Input/5.1.in"
    arr = map(int, open(fname).readline().split(","))
    
    c = Computer(arr[:])
    ret, outputs, dump = c.run_computer([1])
    print(outputs)

    c = Computer(arr[:])
    ret, outputs, dump = c.run_computer([5])
    print(outputs)

if __name__=="__main__":
    main()