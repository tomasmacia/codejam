import sys

def calculateMinimumDamage(actions):
    # minimum damage occurs with every S to the left
    return actions.count('S')

def calculateCurrentDamage(actions):
    damage, power = [0, 1]
    for action in actions:
        if action == 'C':
            power *= 2
        else:
            damage += power
    return damage

def swap(s, i, j):
    lst = list(s);
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def presidentSwap(actions):
    # send rightmost S with left adjacent C to the left
    posRightmostCS = actions.rfind('CS')
    if(posRightmostCS in xrange(0, len(actions)-1)):
        actions = swap(actions, posRightmostCS, posRightmostCS+1)
    return actions

inputCases = sys.stdin.readlines()
firstLine = True
cases = []
cases = [line.strip() for line in inputCases][1:]

i = 0
for case in cases:
    i += 1
    shield, actions = [int(case.split(" ")[0]), str(case.split(" ")[1])]
    minimumDamage = calculateMinimumDamage(actions)
    if minimumDamage > shield:
        print "Case #{}: IMPOSSIBLE".format(i)
        continue
    currentDamage = calculateCurrentDamage(actions)
    swaps = 0
    while(currentDamage > shield):
        actions = presidentSwap(actions)
        swaps += 1
        currentDamage = calculateCurrentDamage(actions)

    print "Case #{}: {}".format(i, swaps)
