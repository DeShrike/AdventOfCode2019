class IntComputer():
    
    _mem = None
    _ip = 0
    _paramcounts = [0, 3, 3, 1, 1, 2, 2, 3, 3]
    _outputcallback = None
    _program = None
    _debug = False
    _inputix = 0
    _inputs = []

    version = "v7"
    identifier = None
    outputs = []
    lastoutput = None
    finished = False

    def __init__(self, program, outputcb = None, name = "IntComputer"):
        self._program = program
        self._outputcallback = outputcb
        self.identifier = name
        self.reset()

    def reset(self):
        self._ip = 0
        self._mem = [x for x in self._program]
        self.outputs.clear()
        self.lastoutput = None
        self._inputs = []
        self._inputix = 0

    def run(self, inputs):
        self._inputs += inputs
        if self._debug:
            print(self.identifier, end = "|")
            print("RUN with inputs: ", end = "")
            print(inputs)
            print("ALL INPUT: ", end = "")
            print(self._inputs, end = "")
            print(" IX: %d " % self._inputix)
        self._execute()

    def _execute(self):

        il = 0
        op1addr = 0
        op2addr = 0
        op3addr = 0

        val1 = 0
        val2 = 0
        val3 = 0

        while True:
            instruction = self._mem[self._ip]

            opcode = instruction % 100
            instruction = (instruction - opcode) / 100
            mode1 = instruction % 10
            instruction = (instruction - mode1) / 10
            mode2 = instruction % 10
            instruction = (instruction - mode2) / 10
            mode3 = instruction % 10

            if self._debug:
                print(self.identifier, end = "|")
                print("IP: %d I: %d OPCODE: %d  MODE1: %d MODE2: %d MODE3: %d " % (self._ip, self._mem[self._ip], opcode, mode1, mode2, mode3))
                # input("Press...")

            paramcount = self._paramcounts[0 if opcode == 99 else opcode]
            if paramcount >= 1:
                op1addr = self._mem[self._ip + 1]
                val1 = self._mem[op1addr] if mode1 == 0 else op1addr

            if paramcount >= 2:
                op2addr = self._mem[self._ip + 2]
                val2 = self._mem[op2addr] if mode2 == 0 else op2addr

            if paramcount >= 3:
                op3addr = self._mem[self._ip + 3]
                val3 = self._mem[op3addr] if mode3 == 0 else op3addr

            if opcode == 99:	# QUIT
                il = 1
                self.finished = True
                if self._debug:
                    print(self.identifier, end = "|")
                    print("QUIT")
                break

            elif opcode == 1:	# ADD
                self._mem[op3addr] = val1 + val2
                il = 4

            elif opcode == 2:	# MULTIPLY
                self._mem[op3addr] = val1 * val2
                il = 4

            elif opcode == 3:	# INPUT
                if self._inputix < len(self._inputs):
                    inp = self._inputs[self._inputix]
                else:
                    if self._debug:
                        print(self.identifier, end = "|")
                        print("NOT ENOUGH INPUTS")
                    return

                if self._debug:
                    print(self.identifier, end = "|")
                    print("INPUT: %d  (index %d)" % (inp, self._inputix))

                self._mem[op1addr] = inp
                self._inputix += 1
                il = 2

            elif opcode == 4:	# OUTPUT
                self.lastoutput = val1
                self.outputs.append(val1)
                
                if self._outputcallback != None:
                    self._outputcallback(self.lastoutput)
                
                if self._debug:
                    print(self.identifier, end = "|")
                    print("OUTPUT: %d" % self.lastoutput)
                
                il = 2

            elif opcode == 5:	# JUMP IF TRUE
                il = 3
                if val1 != 0:
                    self._ip = val2
                    il = 0

            elif opcode == 6:	# JUMP IF FALSE
                il = 3
                if val1 == 0:
                    self._ip = val2
                    il = 0

            elif opcode == 7:	# LESS THAN
                self._mem[op3addr] = 1 if val1 < val2 else 0
                il = 4

            elif opcode == 8:	# EQUALS
                self._mem[op3addr] = 1 if val1 == val2 else 0
                il = 4

            else:
                print(self.identifier, end = "|")
                print("Invalid opcode %d at position %d" % (opcode, self._ip))

            self._ip += il
        
        return
