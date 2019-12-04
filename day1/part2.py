import math

def calReqFuel(mass):
    ''' Calculate the required fuel for a given mass, taking into consideration 
        the fuel's own mass.'''
    fuel = int(math.floor(mass / 3.0) - 2)
    
    if (fuel > 0):
        fuel += calReqFuel(fuel)
    else:
        fuel = 0

    return fuel


reqfuel = 0

with open("input", 'r') as fp:
    for cnt, line in enumerate(fp):
        mass = int(line)
        fuel = calReqFuel(mass)
        reqfuel += fuel
        print("Module {} of mass {} requires {} fuel.".format(cnt, mass, fuel))

print("Total fuel required: " + str(reqfuel))