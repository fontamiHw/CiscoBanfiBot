#!/usr/bin/env python
#  -*- coding: utf-8 -*-


#declare a class Config
class Config(object):
    
    def __init__(self):
        self.token = "M2IwNDU0OWItYTg1ZC00YjQyLTkwMDMtODQyZDMyYzA1M2U2NmQ1MjdlOTktNWFi_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
        self.name = "MikExperiment"
        self.uniqueId = "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OLzI5ODFhMjhjLTQ0MTUtNDcwMy1iOWRjLTViNmJlNzlkNjg0MQ"
        self.proxies=None


    def get_token(self):
        return self.token

    def get_name(self):
        return self.name

    def get_uniqueId(self):
        return self.uniqueId  

    def get_proxies(self):
        return self.proxies

from webexpythonsdk import WebexAPI

#create a Config object
configuration=Config()



DEMO_ROOM_NAME = configuration.get_name()
DEMO_PEOPLE = ["alessandro.pellicone@liceobanfi.eu", "riccardo.camisa@liceobanfi.eu"]
DEMO_MESSAGE = "Webex rocks!  \ud83d\ude0e"
DEMO_FILE_URL = (
    "https://www.webex.com/content/dam/wbx/us/images/dg-integ/teams_icon.png"
)


# Create a WebexAPI connection object; uses your WEBEX_ACCESS_TOKEN
#api = WebexAPI()
# Inserisci qui il tuo token personale
token = configuration.get_token()

# Crea l'istanza dell'API con il token
api = WebexAPI(access_token=token)


# Clean up previous demo rooms
print("Searching for existing demo rooms...")

# Create a generator container (iterable) that lists the rooms where you are
# a member
rooms = api.rooms.list()

# Build a list of rooms with the name DEMO_ROOM_NAME
existing_demo_rooms = [room for room in rooms if room.title == DEMO_ROOM_NAME]
if existing_demo_rooms:
    print(
        "Found {} existing room(s); deleting them." "".format(
            len(existing_demo_rooms)
        )
    )
    for room in existing_demo_rooms:
        # Delete the room
        api.rooms.delete(room.id)
        print("Room '{}' deleted.".format(room.id))


# Create a new demo room
demo_room = api.rooms.create(DEMO_ROOM_NAME)

# Print the room details (formatted JSON)
print(demo_room)

for person_email in DEMO_PEOPLE:
    # Add people to the room
    api.memberships.create(demo_room.id, personEmail=person_email)

# Create a message in the new room
message = api.messages.create(demo_room.id, text=DEMO_MESSAGE)

# Print the message details (formatted JSON)
print(message)

# Post a file in the new room from test_url
message = api.messages.create(demo_room.id, files=[DEMO_FILE_URL])

# Print the message details (formatted JSON)
print(message)