# Used for Days 2, 5, 7
class Computer:
    def __init__(self, filearr):
        self.paramaters_per_operation = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0}
        self.operation_name = {1: "add", 2: "mult", 3: "input", 4: "output", 5: "jit", 6: "jif", 7: "<", 8: "==", 99: "RET"}
        self.log = []
        self.arr = filearr
        self.isp = 0
        self.mem_pointer = 0
        self.inputs = []
        self.outputs = []
        self.can_continue = True

    def get_param(self, param, mode):
        if mode == 0:
            return self.arr[param]
        elif mode == 1:
            return param
        else:
            print("get param received mode %d for param %d" % (mode, param))
            return 0

    def add(self, first, second, position):
        self.arr[position[0]] = self.get_param(*first) + self.get_param(*second)
        self.log.append("arr[%d] = %d + %d" % (position[0], self.get_param(*first), self.get_param(*second)))

    def mult(self, first, second, position):
        self.arr[position[0]] = self.get_param(*first) * self.get_param(*second)

    def input(self, first):
        # self.arr[first[0]] = int(raw_input())
        if self.inputs:
            self.arr[first[0]] = self.inputs.pop(0)
            return True
        else:
            self.mem_pointer = first[0]
            return False

    def output(self, first):
        # print(self.get_param(*first))
        self.outputs.append(self.get_param(*first))

    def jump_if_true(self, first, second):
        if self.get_param(*first) != 0:
            self.isp = self.get_param(*second)
    
    def jump_if_false(self, first, second):
        if self.get_param(*first) == 0:
            self.isp = self.get_param(*second)
    
    def less_than(self, first, second, position):
        if self.get_param(*first) < self.get_param(*second):
            self.arr[position[0]] = 1
        else:
            self.arr[position[0]] = 0
    
    def equals(self, first, second, position):
        if self.get_param(*first) == self.get_param(*second):
            self.arr[position[0]] = 1
        else:
            self.arr[position[0]] = 0

    def parse_opcode(self, full_number):
        opcode = full_number % 100
        codes = []
        curr = full_number // 100
        while len(codes) < self.paramaters_per_operation[opcode]:
            codes.append(curr % 10)
            curr //= 10
        return opcode, codes

    def perform_action_on_array(self):
        position = self.isp
        operation, codes = self.parse_opcode(self.arr[position])
        self.isp += self.paramaters_per_operation[operation] + 1
        params = zip(self.arr[position+1:position+1+self.paramaters_per_operation[operation]], codes)
        log = "operation %s with params %s" % (self.operation_name[operation], str(params))
        if operation == 1:
            self.add(*params)
        if operation == 2:
            self.mult(*params)
        if operation == 3:
            return self.input(*params)
        if operation == 4:
            self.output(*params)
        if operation == 5:
            self.jump_if_true(*params)
        if operation == 6:
            self.jump_if_false(*params)
        if operation == 7:
            self.less_than(*params)
        if operation == 8:
            self.equals(*params)
        if operation == 99:
            self.can_continue = False
            return False
        return True
    
    def nounverb(self, noun, verb):
        self.arr[1] = noun
        self.arr[2] = verb

    def dump(self):
        print("memory: %s" % self.arr)
        print("isp: %d" % self.isp)
        print("inputs: %s" % self.inputs)
        print("log: %s" % self.log)

    def reset(self):
        self.isp = 0

    def run_computer(self, inputs=[]):
        if not self.inputs:
            self.inputs = inputs
        else:
            self.inputs.extend(inputs)
        try:
            while self.perform_action_on_array():
                pass
            return self.arr[0], self.outputs, self.arr[:]
        except:
            self.dump()
            raise
    
    def continue_run(self, inputs):
        self.arr[self.mem_pointer] = inputs[0]
        return self.run_computer(inputs[1:])
