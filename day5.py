from computer import Computer

def main():
    fname = "5.1.in"
    arr = map(int, open(fname).readline().split(","))
    
    c = Computer(arr[:])
    c.run_computer()

if __name__=="__main__":
    main()