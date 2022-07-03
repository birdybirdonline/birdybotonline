"""   Copyright (C) 2022  birdybirdonline - see LICENSE.md
    @ https://github.com/birdybirdonline/birdybotonline
    
    Contact via Github in the first instance
    https://github.com/birdybirdonline
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>."""

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
