'''
section 1

Problem 1: Extra Treats
In a pet adoption center, there are two groups of volunteers: the "Cat Lovers" and the "Dog Lovers."

The center is deciding on which type of pet should be receive extra treats that week, and the voting takes place in a round-based procedure. In each round, each volunteer can exercise one of the two rights:

Ban one volunteer's vote: A volunteer can make another volunteer from the opposite group lose all their rights in this and all the following rounds.
Announce the victory: If a volunteer finds that all the remaining volunteers with the right to vote are from the same group, they can announce the victory for their group and prioritize their preferred pet for extra treats.
Given a string votes representing each volunteer's group affiliation. The character 'C' represents "Cat Lovers" and 'D' represents "Dog Lovers". The length of the given string represents the number of volunteers.

Predict which group will finally announce the victory and prioritize their preferred pet for extra treats. The output should be "Cat Lovers" or "Dog Lovers".



Understand:
count the max votes, the one that has more votes wins. if there is a tie the first voter wins.

Match:
we don't need extra memory, we just need 2 variables
-dog_count
-cat_count

Plan:
edge case: if there is a tie, we need to return the first voter. 

edge case: if nobody votes, return None

edge case: if other animals or things that are not dogs or cats vote, we continue

edge case: every char should be low()



if len(string) == 0: return None

dog_count = 0
cat_count = 0


for c in string:
    if lower(c) == 'c':
        cat_count += 1
    elif lower(c) == 'd':
        dog_count += 1

        

if dog_count == 0 and cat_count == 0:
    return None

if dog_count == cat_count:
    if low(string[0]) == 'c':
        print("cats")
    if low(string[0]) == 'd':
        print("dogs")

if cat_count > dog_count:
    print("cats")
else:
    print("dogs")
    

'''
#Implement:
def predictAdoption_victory(votes):

    CAT_WIN = "Cat Lovers"
    DOG_WIN = "Dog Lovers"

    if len(votes) == 0: return None

    dog_count = 0
    cat_count = 0

    for c in votes:
        if c.lower() == 'c':
            cat_count += 1
        elif c.lower() == 'd':
            dog_count += 1
    
    if dog_count == 0 and cat_count == 0: return None

    if dog_count == cat_count:
        if votes[0].lower() == 'c':
            return CAT_WIN
        elif votes[0].lower() == 'd':
            return DOG_WIN
    
    if cat_count > dog_count:
        return CAT_WIN
    else:
        return DOG_WIN

print(predictAdoption_victory("")) 
