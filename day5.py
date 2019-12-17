from computer import Computer

def main():
    fname = "Input/5.1.in"
    arr = map(int, open(fname).readline().split(","))
    
    c = Computer(arr[:])
    c.run_computer([1])

    c = Computer(arr[:])
    c.run_computer([5])

if __name__=="__main__":
    main()