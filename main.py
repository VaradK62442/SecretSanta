from pprint import pprint
import random

def secret_santa(names, gifts=1, seed=None):
    # set random seed if specified
    if seed:
        random.seed(seed)

    # Shuffle the list of names
    random.shuffle(names)
    
    # Assign each person Secret Santa recipients
    # equal to number of gifts
    assignments = {}
    for i in range(len(names)):
        assignments[names[i]] = [names[(i+j) % len(names)] for j in range(1, gifts+1)]
    
    # Return the assignments
    return names, assignments


def checkName(name, names):
    # name must be one word
    return len(name.split(" ")) == 1 and name.capitalize() in names


def main():
    names = []
    names, assigned = secret_santa(names=names, gifts=2, seed=413)
    myName = input("Enter your name: ")
    if checkName(myName, names):
        print(assigned[myName.capitalize()])
    else:
        print("Invalid name, please try again.")


main()
