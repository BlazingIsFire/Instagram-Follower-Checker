import json

# Opens both files.
followers_file = open('./files/followers.json', 'r');
following_file = open('./files/following.json', 'r');
not_following_back_file = open('./notfollowing.txt', 'w');

# Loads JSON Data and first data list
followers = [];
following = [];
not_following_back = [];
followers_Data = json.load(followers_file);
following_Data = json.load(following_file);
followers_Data_Json = followers_Data['relationships_followers'];
following_Data_Json = following_Data['relationships_following'];

def checkFollowing():
    for person in following_Data_Json:
        following.append(person['string_list_data'][0]['value']);
    for follower in followers_Data_Json:
        followers.append(follower['string_list_data'][0]['value']);
    for user in following:
        if user not in followers:
            not_following_back.append(user);
    for notFollowingUser in not_following_back:
        not_following_back_file.write(notFollowingUser+'\n');
    print('\033[1;32;40m Follow check complete. Log file can be found in this directory called "notfollowing.txt".')

checkFollowing();

# Closes both files.
following_file.close();
followers_file.close();

# Created by Andrew Schweitzer