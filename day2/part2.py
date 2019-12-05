
def main():
    intcode = []

    # Read Intcode program as list of integers
    with open("input", 'r') as fp:
        for line in fp:
            intcode.extend(map(int, line.split(',')))
    
    ans = ""
    for noun in range(100):
        for verb in range(100):
            tempintcode = list(intcode)
            tempintcode[1] = noun
            tempintcode[2] = verb
            result = processIntcode(tempintcode)

            if (result == 19690720):
                ans = str(100 * noun + verb)
                break
        
        if (ans != ""):
            break
    
    print(ans)  


def processIntcode(intcode):
    ''' Process the Intcode program and returns value in position 0. '''
    idx_code = idx_op1 = idx_op2 = idx_rslt = 0
    proglen = len(intcode)

    while (idx_code < proglen and intcode[idx_code] != 99):
        idx_op1 = intcode[idx_code + 1]
        idx_op2 = intcode[idx_code + 2]
        idx_rslt = intcode[idx_code + 3]

        if (intcode[idx_code] == 1):
            intcode[idx_rslt] = intcode[idx_op1] + intcode[idx_op2]
        elif (intcode[idx_code] == 2):
            intcode[idx_rslt] = intcode[idx_op1] * intcode[idx_op2]
        
        idx_code += 4
    
    return intcode[0]


if __name__ == "__main__":
    main()