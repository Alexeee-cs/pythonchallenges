import random
action_A = ['confess','silence']
action_B = ['confess','silence']

if random.choice(action_A) == 'confess':
    if random.choice(action_B) == 'silence':
        print("Prisoner A confesses, Prisoner B stays silence")
        print("Prisoner B in prison for 20 years")
    else:
        print("Prisoner A confesses, Prisoner B confesses")
        print("Both prisoners in prison for 5 years")
else:
    if random.choice(action_B) == 'silence':
        print("Prisoner A stays silence, Prisoner B stays silence")
        print("Both prisoners in prison for 1 years")
    else:
        print("Prisoner A stays silence, Prisoner B confesses")
        print("Prisoner A in prison for 20 years")
