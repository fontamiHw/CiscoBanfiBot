from config import Config
from webexpythonsdk import WebexAPI
from command import CommandImage
from webex_bot.webex_bot import WebexBot

class BanfiBot(object):
    def __init__(self):

        print("ingresso costruttore")
        #create a Config object
        self.configuration=Config()
        self.bot = WebexBot(teams_bot_token=self.configuration.get_token(),
                   #approved_domains=['cisco.com'],
                   approved_rooms=['b69a0c50-3fa8-11f0-b7d6-5d17b726561b'],
                   bot_name=self.configuration.get_name(),
                   include_demo_commands=True,
                   proxies=self.configuration.get_proxies())
        token = self.configuration.get_token()
        self.api = WebexAPI(access_token=token)
        self.bot.add_command(CommandImage(self.api))
        
        

        self.DEMO_ROOM_NAME = self.configuration.get_name()
        self.DEMO_PEOPLE = ["alessandro.pellicone@liceobanfi.eu", "riccardo.camisa@liceobanfi.eu"]
        self.DEMO_MESSAGE = "Webex rocks!  \ud83d\ude0e"
        print("uscita costruttore")

        #self.DEMO_FILE_URL = (
        #    "https://www.webex.com/content/dam/wbx/us/images/dg-integ/teams_icon.png"
        #)

    def start(self):
        print("before run")
        self.bot.run()
        print("after run")

        

    