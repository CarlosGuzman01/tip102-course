
'''
Problem 1: Track Screen Time Usage
In the digital age, managing screen time is crucial for maintaining a healthy balance between online and offline activities. You need to track how much time users spend on different apps throughout the day.

Write the track_screen_time() function, which takes a list of logs, where each log contains an app name and the number of minutes spent on that app during a specific hour. The function should return the app names and the total time spent on each app.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def track_screen_time(logs):
    pass
Example Usage:

logs = [("Instagram", 30), ("YouTube", 20), ("Instagram", 25), ("Snapchat", 15), ("YouTube", 10)]
logs_2 = [("Twitter", 10), ("Reddit", 20), ("Twitter", 15), ("Instagram", 35)]
logs_3 = [("TikTok", 40), ("TikTok", 50), ("YouTube", 60), ("Snapchat", 25)]

print(track_screen_time(logs))
print(track_screen_time(logs_2))
print(track_screen_time(logs_3))
Example Output:

{'Instagram': 55, 'YouTube': 30, 'Snapchat': 15}
{'Twitter': 25, 'Reddit': 20, 'Instagram': 35}
{'TikTok': 90, 'YouTube': 60, 'Snapchat': 25}

#understand:
we get list of tuples, index[0] string with the app name and index[1] is going to be screen time
and we return a hashmap (dictionary) with the app names and each time spent

edge cases:
1- return empty hashmap

#match:
since we are making one value to another, that is essencially a hashmap (dictionary)

#plan:

declare an empty hashmap

iterate over the logs list

check if the social media app is in the map 
    if it is we increment the value
    if it is not we set the first value to the index[1]

    
return hashmap



'''

def track_screen_time(logs):
    map1 = {}

    for arr in logs:
        name, hours = arr

        if name in map1:
            map1[name] += hours
        else:
            map1[name] = hours

    return map1

logs = [("Instagram", 30), ("YouTube", 20), ("Instagram", 25), ("Snapchat", 15), ("YouTube", 10)]
print(track_screen_time(logs))