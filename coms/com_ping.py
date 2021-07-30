from discord.ext import commands

@commands.command()
async def ping(ctx):
    """I'm sure you need this explaining!

    defines ping command.
    """
    await ctx.send("pong!")

def setup(bot):
    """extension loader - required
    """
    bot.add_command(ping)