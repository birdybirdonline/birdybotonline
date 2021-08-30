<<<<<<< HEAD
# `main.py`

A basic skeleton / factory for a discord bot, triggering the key initializations and populating the bot's command list. It doesn't and shouldn't do much else, but does operate a single event handler to confirm bot ready status. 

- Initiates bot and loads extensions from the commands, calls env variables to define TOKEN and COMMAND_PREFIX
- makes use of [discord.ext's](https://discordpy.readthedocs.io/en/latest/index.html#extensions) 'commands' module which allows us to define our agent as type ```Bot``` as opposed to ```Client```, which gives a number of useful functions.
- Also does the preliminary work to set up a db if required.

<<<<<<< HEAD
### `.env`:
    environmental variables to determine our TOKEN and command PREFIX. Referenced by main.py.
=======
#### `.env`: environmental variables to determine our TOKEN and command PREFIX. Referenced by main.py

I've not gitignore'd it here, just so it can be seen as an example. This should be added to gitignore locally so that tokens are not pushed to repo.
>>>>>>> 2361e6d (Update README.md)

# Command modules

Rather than having a monolithic `CommandHandler` class containing all commands, individual `commands` (and `cogs`) can be written as individual `modules`.

As long as they meet a couple of simple criteria, each module won't require modification of any other area of the codebase.


### `coms` package

A folder containing modular `commands`. This allows us to write commands on the fly without changing any other area of our bot's codebase. 

*Note: Because of Python3's namespace this can also function as a package of modules, but discord.ext doesn't properly load them into the bot this way so we do this via the bot.load_extension() method in main.py.*

### Types

There are two types of module we can employ - `commands` and `cogs` (both strictly defined in the `Discord API`).

##### `Commands` are singular, individual commands as you would expect. 

With each command as an individual .py `module`, we must load each into the bot individually as an "extension" (this is handled in main.py).

##### [Each `cog` is a `Class` that subclasses `commands.Cog`](https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html#ext-commands-cogs). 

`Cogs` are `Classes` which have collections of related `commands` as `methods` and can be called via `inter-command protocol`, meaning their methods (which can be
both commands, events and otherwise) can be called by other commands too.

They are loaded as `extentions` in the same way as our individual `commands`.


### Requirements and Conventions

#### Requirements

##### `Commands`

Each `command` module *must* take the following format:

```
from discord.ext import commands

@commands.command()
async def command_name(ctx):
    #action

def setup(bot):
    bot.add_command(command_name)
```

The command can have any name you want and perform any tasks you want, but these key features must be present.

##### `Cogs`

Quite similar to `commands`, cogs *must* take the following format:

from discord.ext import commands

```
from discord.ext import commands

class CogName(commands.Cog):
    @commands.command()
    async def command_name(self):
        #action
    
    #other methods

def setup(bot):
    bot.add_cog(CogName)
```

#### Conventions

For this build we *should* use a couple of conventions which will make sure that any new modules we add will work accordingly
and are consistent from contributor to contributor.

* `Commands` should be named with the prefix `com_`, for example `com_ping.py`
* `Cogs` should be named with the prefix `com_` and the suffix `_cog`
* The implementation of any `command` or `cog` should not involve direct rewrites of or amendments to any other area of our codebase

<<<<<<< HEAD
## A template / example of a `command` and `cog` are each included in the coms folder in this repo.
=======
# birdybotonline
A basic Python 3 discord bot template for modular commands
>>>>>>> 95f06bc (Initial commit)
=======

#### A template / example of a `command` and `cog` are each included in the coms folder in this repo.
>>>>>>> 891d6b5 (Update README.md)
