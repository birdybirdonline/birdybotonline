from discord.ext import commands

@commands.command()
async def command_name(ctx):
    """"""
    pass

def setup(bot):
    """"""
    bot.add_command(command_name)