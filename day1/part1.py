import math

reqfuel = 0

with open("input", 'r') as fp:
    for cnt, line in enumerate(fp):
        mass = int(line)
        fuel = math.floor(mass / 3.0)
        reqfuel += int(fuel - 2)
        print("Module {} of mass {} requires {} fuel.".format(cnt, mass, fuel))

print("Total fuel required: " + str(reqfuel))