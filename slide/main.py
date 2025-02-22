'''
#Understand

remove duplicates from sorted list

[1, 1, 1, 1, 1, 1, 1, 1,   2 , 3]
 p                         

[1, 2 , 3]


#Match


'''

def remove_duplicate(nums):

    res = 1

    i = 0
    j = 1

    while j < len(nums):

        while j < len(nums) and nums[i] == nums[j]:
            j += 1
        i = j
        j += 1
        res += 1



    return res


print(remove_duplicate([1, 1, 1, 2, 3]))




