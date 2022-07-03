"""   Copyright (C) 2022  birdybirdonline - see LICENSE.md
    @ https://github.com/birdybirdonline/birdybotonline
    Contact via Github in the first instance
    """
    
from discord.ext import commands

@commands.command()
async def command_name(ctx):
    """"""
    pass

def setup(bot):
    """"""
    bot.add_command(command_name)
