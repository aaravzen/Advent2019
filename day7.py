from computer import Computer
from itertools import permutations

def check_amps(amps):
    for amp in amps:
        if not amp.can_continue:
            return False
    return True

def run_through_amp(amp, phase_setting=-1, input_signal=0):
    if phase_setting == -1:
        ret,outputs,dump = amp.continue_run([input_signal])
    else:
        ret,outputs,dump = amp.run_computer([phase_setting, input_signal])
    return outputs[-1]

def run_through_amps(code=[], ordering=[], signal=0, in_amps=[]):
    amps = []
    if not code and not in_amps:
        raise Exception("Can't run through amps with no code or amps")
    if in_amps:
        amps.extend(in_amps)
    else:
        for i in xrange(5):
            amps.append(Computer(code[:]))
    
    if ordering:
        for i,amp in enumerate(amps):
            signal = run_through_amp(amp, phase_setting=int(ordering[i]), input_signal=signal)
    else:
        for i,amp in enumerate(amps):
            signal = run_through_amp(amp, input_signal=signal)
    
    return signal, amps

def part1(code):
    best = -1
    ordering = None
    for perm in permutations(range(5)):
        output,amps = run_through_amps(code, perm)
        if output > best:
            best = output
            ordering = perm
    print("Max output %d by using ordering: %s" % (best, ordering))

def part2(code):
    best = -1
    ordering = None
    for perm in permutations(range(5,10)):
        output,amps = run_through_amps(code, perm)
        for i in xrange(10):
            # print("output: %d" % output)
            if output > best:
                best = output
                ordering = perm
            if not check_amps(amps):
                break
            output,amps = run_through_amps(in_amps=amps, signal=output)
    print("Max output %d by using ordering: %s" % (best, ordering))

def main():
    fname = "Input/7.1.in"
    arr = map(int, open(fname).readline().split(","))
    part1(arr)
    part2(arr)

if __name__=="__main__":
    main()