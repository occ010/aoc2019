intcode = []

# Read Intcode program as list of integers
with open("input", 'r') as fp:
    for line in fp:
        intcode.extend(map(int, line.split(',')))

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

print(intcode)