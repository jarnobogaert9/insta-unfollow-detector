from instagram_private_api import Client, ClientCompatPatch
import uuid
import json
from InstaBot import InstaBot

instaBot = InstaBot()

prev_followers = instaBot.read_followers()
now_followers = instaBot.get_followers()
# We use this later on
now_followers_to_write = now_followers

# This step is when their are no followers in the file
if len(prev_followers) == 0:
    print('no followers in file')
    prev_followers = now_followers
    instaBot.write_followers(now_followers)


unfollowed = []
prev_followers = [user.get('username') for user in prev_followers]
now_followers = [user.get('username') for user in now_followers]

for user in prev_followers:
    if user not in now_followers:
        unfollowed.append(user)

print(unfollowed)

instaBot.write_unfollowed(unfollowed)


instaBot.write_followers(now_followers_to_write)
