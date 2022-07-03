import os
import logging
from dotenv import load_dotenv

from discord.ext import commands


# establish TOKEN, PREFIX (for commands)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('DISCORD_PREFIX')

# establish bot and logging
bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX))
logging.basicConfig(level=logging.INFO)


def main():
    """initiate bot and load all extensions.

    for loop checks all modules in coms; convention to start module names 
    with com_ so that we can ignore other key files in this dir if necessary.

    load the com_ modules as extensions into the bot then run the bot
    with the token from .env
    """
    for module in os.listdir('coms'):
        ext = os.path.splitext(module)[0]
        if ext.startswith("com_"):
            bot.load_extension("commands_."+ext)
            print("success")
    bot.run(TOKEN)


# .event wrappers from discord.py; listeners for events
# as core functionality of discord.py
@bot.event
async def on_ready():
    """
    confirm bot is ready
    """
    print(f'{bot.user} connected')

# perfunctory
if __name__ == "__main__":
    main()
