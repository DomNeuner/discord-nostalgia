# standard libs
import os
import time

# third party libs
from pypresence import Presence
from dotenv import load_dotenv

# my libs are cooler than your libs
import spotifyer
import msnifier

# loading...
load_dotenv()

# enivronment variables
discord_client_id = os.getenv("DISCORD_CLIENT_ID")

# initiating our discord presence doohickey
discord_presence = Presence(discord_client_id)  # Initialize the client class
discord_presence.connect()

def presence_process():
    current_time = time.ctime()
    print(f"Beginning process at {current_time}")
    current_title, current_artist, current_song_URL = spotifyer.check()
    formatted_title, formatted_artist = msnifier.processor(current_title,current_artist)
    discord_presence.update(state=f'by {formatted_artist}',
               details=formatted_title)
    time.sleep(15)  # Can only update rich presence every 15 seconds, don't want to annoy big daddy discord

# it's the main event
def main():
    try:
        while True:
            presence_process()

    except KeyboardInterrupt:
        print('aight we done here')

if __name__ == '__main__':
    main()