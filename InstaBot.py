from instagram_private_api import Client, ClientCompatPatch
from dotenv import load_dotenv
import uuid
import os
import json
load_dotenv()

username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')


class InstaBot:
    def __init__(self):
        super().__init__()
        self.api = Client(username, password)

    def get_user_id(self):
        return self.api.authenticated_user_id

    def get_uuid(self):
        return str(uuid.uuid4())

    def get_followers(self):
        user_id = self.get_user_id()
        uuid = self.get_uuid()

        user_followers = self.api.user_followers(user_id, uuid)

        updates = []
        updates.extend(user_followers.get('users', []))

        next_max_id = user_followers.get('next_max_id')

        while next_max_id:
            user_followers = self.api.user_followers(user_id, uuid)
            updates.extend(user_followers.get('users', []))

            next_max_id = user_followers.get('next_max_id')
        return updates

    def write_followers(self, followers, filename='followers.json'):
        print('Writing followers to file...')
        f = open(filename, "w")
        f.write(json.dumps(followers))
        f.close()

    def read_followers(self, filename='followers.json'):
        is_file = os.path.isfile(filename)
        if not is_file:
            # Create file
            f = open(filename, 'w')
            f.write("[]")
            f.close()
            return []
        if self.is_file_empty(filename):
            print('file is empty')
            self.write_to_file(filename, json.dumps([]))
        with open(filename) as json_file:
            arr = json.load(json_file)
        return arr

    def write_unfollowed(self, unfollowed, filename='unfollowed.json'):
        is_file = os.path.isfile(filename)
        if not is_file:
            # Create file
            f = open(filename, 'w')
            f.write("[]")
            f.close()
        if self.is_file_empty(filename):
            print('file is empty')
            self.write_to_file(filename, json.dumps([]))

        prev_unfollowed = json.loads(self.read_file(filename))
        prev_unfollowed.extend(unfollowed)
        self.write_to_file(filename, json.dumps(prev_unfollowed))
        
    
    def is_file_empty(self, filename):
        return os.path.exists(filename) and os.stat(filename).st_size == 0

    def write_to_file(self, filename, string):
        f = open(filename, 'w')
        f.write(string)
        f.close

    def read_file(self, filename):
        f = open(filename, 'r')
        content = f.read()
        f.close()
        return content
