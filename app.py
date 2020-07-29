# standard libs
import os
import time

# third party libs
from pypresence import Presence
from dotenv import load_dotenv

# loading
load_dotenv()

# enivronment variables
discord_client_id = os.getenv("DISCORD_CLIENT_ID")

# initiating our discord presence doohickey
discord_presence = Presence(discord_client_id)  # Initialize the client class
discord_presence.connect()

def presence_process():
    current_time = time.ctime()
    discord_presence.update(state=f'{current_time}',
               details="what the fuck you looking at?")
    time.sleep(15)  # Can only update rich presence every 15 seconds, don't want to annoy daddy discord

# it's the main event
def main():
    try:
        while True:
            presence_process()

    except KeyboardInterrupt:
        print('aight we done here')

if __name__ == '__main__':
    main()