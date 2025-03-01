'''
section 2
Problem 1: Blueprint Approval Process
You are in charge of overseeing the blueprint approval process for various architectural designs. Each blueprint has a specific complexity level, represented by an integer. Due to the complex nature of the designs, the approval process follows a strict order:

Blueprints with lower complexity should be reviewed first.
If a blueprint with higher complexity is submitted, it must wait until all simpler blueprints have been approved.
Your task is to simulate the blueprint approval process using a queue. You will receive a list of blueprints, each represented by their complexity level in the order they are submitted. Process the blueprints such that the simpler designs (lower numbers) are approved before more complex ones.

Return the order in which the blueprints are approved.

def blueprint_approval(blueprints):
    pass
Example Usage:

print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 
Example Output:

[1, 2, 3, 4, 5]
[2, 4, 5, 6, 7]

#plan:

first create additional list called extra

iterate over the blueprints list
    if current element is a number
        We add to the extra list

heapify the extra list

and then we pop from the extra heap until is empty



'''

import heapq


def blueprint_approval(blueprints):
    extra = []


    for n in blueprints:
        if isinstance(n, int):
            extra.append(n)
    
    heapq.heapify(extra)
    
    res = []
    while extra:
        res.append(heapq.heappop(extra))
    return res

print(blueprint_approval([3, 5, 2, 1, 4]))
print(blueprint_approval([7, 4, 6, 2, 5])) 