from discord.ext import commands

class CogTemplate(commands.Cog):
    """"""
    @commands.command()
    async def command_name(self):
        pass
    
    # Other methods

def setup(bot):
    """"""
    bot.add_cog(CogTemplate)