def add(arr, first, second, position):
    arr[position] = arr[first] + arr[second]

def mult(arr, first, second, position):
    arr[position] = arr[first] * arr[second]

def perform_action_on_array(arr, position):
    operation = arr[position]
    if operation == 1:
        add(arr, *arr[position+1:position+4])
    if operation == 2:
        mult(arr, *arr[position+1:position+4])
    if operation == 99:
        return False
    return True

def run_computer(arr, noun=0, verb=0):
    instruction_pointer = 0
    arr[1] = noun
    arr[2] = verb
    while perform_action_on_array(arr, instruction_pointer):
        instruction_pointer += 4
    return arr[0], arr[:]

def main():
    fname = "2.1.in"
    arr = map(int, open(fname).readline().split(","))
    
    for n in xrange(100):
        for v in xrange(100):
            ret, dump = run_computer(arr[:], n, v)
            if ret == 19690720:
                print("Noun: %d / Verb: %d / Ans: %d" % (n,v, 100*n+v))
                print("Dump: %s" % str(dump))
    
    

main()