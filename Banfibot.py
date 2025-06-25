from config import Config
from webexpythonsdk import WebexAPI
class BanfiBot(object):
    def __init__(self):
        #create a Config object
        self.configuration=Config()
        self.DEMO_ROOM_NAME = self.configuration.get_name()
        self.DEMO_PEOPLE = ["alessandro.pellicone@liceobanfi.eu", "riccardo.camisa@liceobanfi.eu"]
        self.DEMO_MESSAGE = "Webex rocks!  \ud83d\ude0e"
        self.DEMO_FILE_URL = (
            "https://www.webex.com/content/dam/wbx/us/images/dg-integ/teams_icon.png"
        )
    
    def start(self):
        # Create a WebexAPI connection object; uses your WEBEX_ACCESS_TOKEN
        #api = WebexAPI()
        # Inserisci qui il tuo token personale
        token = self.configuration.get_token()

        # Crea l'istanza dell'API con il token
        api = WebexAPI(access_token=token)

        #!/usr/bin/env python
#  -*- coding: utf-8 -*-



        # Clean up previous demo rooms
        print("Searching for existing demo rooms...")

        # Create a generator container (iterable) that lists the rooms where you are
        # a member
        rooms = api.rooms.list()

        # Build a list of rooms with the name DEMO_ROOM_NAME
        existing_demo_rooms = [room for room in rooms if room.title == self.DEMO_ROOM_NAME]
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
        demo_room = api.rooms.create(self.DEMO_ROOM_NAME)

        # Print the room details (formatted JSON)
        print(demo_room)

        for person_email in self.DEMO_PEOPLE:
            # Add people to the room
            api.memberships.create(demo_room.id, personEmail=person_email)

        # Create a message in the new room
        message = api.messages.create(demo_room.id, text=self.DEMO_MESSAGE)

        # Print the message details (formatted JSON)
        print(message)

        # Post a file in the new room from test_url
        message = api.messages.create(demo_room.id, files=[self.DEMO_FILE_URL])

        # Print the message details (formatted JSON)
        print(message)