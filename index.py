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


# ----------------------------------------------------
# user_name = 'jarnocodes'
# password = 'Jarno0412'

# api = Client(user_name, password)

# user_id = api.authenticated_user_id
# user_name = api.authenticated_user_name
# user_followers = api.user_followers(user_id, str(uuid.uuid4()))

# updates = []
# updates.extend(user_followers.get('users', []))

# next_max_id = user_followers.get('next_max_id')

# while next_max_id:
#     user_followers = api.user_followers(user_id, str(uuid.uuid4()))
#     updates.extend(user_followers.get('users', []))
#     if len(updates) >= 30:       # get only first 30 or so
#             break

#     next_max_id = user_followers.get('next_max_id')

# for user in updates:
#     print(user.get('username'))


# f = open("followers2.json", "r")
# f.read()
# f.close()
