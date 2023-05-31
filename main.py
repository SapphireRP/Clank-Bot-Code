# Imports
import guilded
import config
from guilded.ext import commands
from guilded import File, Embed
import os
import requests
from requests.structures import CaseInsensitiveDict
from easy_pil import Editor, load_image_async, Font
import os
import PIL

# Global Constants
BugReportChannel = "50e7c931-a9bf-4029-a45a-5c0843e272ea"
GUILD_ID = "NRgbbqvj"
SuggestChannel = "ad12dc31-90e6-4440-b6cc-277cc5b9ffd1"

# Images
CB_Members = "https://img.guildedcdn.com/asset/TabEmptyStates/gil_members.png"
CB_Recruitment = "https://img.guildedcdn.com/asset/TabEmptyStates/gil_recruitment.png"
CB_Overview = "https://img.guildedcdn.com/asset/TabEmptyStates/gil_overview.png"
CB_Forums = "https://img.guildedcdn.com/asset/TabEmptyStates/gil_forums.png"
CB_Calendar = "https://img.guildedcdn.com/asset/TabEmptyStates/gil_calendar.png"
CB_Docs = "https://img.guildedcdn.com/asset/TabEmptyStates/gil_docs.png"
CB_Media = "https://img.guildedcdn.com/asset/TabEmptyStates/gil_media.png"
CB_Streams = "https://img.guildedcdn.com/asset/TabEmptyStates/gil_streams.png"
CB_Matches = "https://img.guildedcdn.com/asset/TabEmptyStates/gil_matches.png"
CB_Nothing_Here = "https://img.guildedcdn.com/asset/GenericMessages/nothing-here.png"
CB_Not_Found = "https://img.guildedcdn.com/asset/GenericMessages/not-found.png"
CB_Gilmoji = "https://img.guildedcdn.com/asset/GenericMessages/gilmoji.png"
CB_Denied = "https://img.guildedcdn.com/asset/GenericMessages/denied.png"
CB_Stonks_Rising = "https://img.guildedcdn.com/asset/GenericMessages/stonks-rising.png"

# Initialize the Bot object with the default prefix
bot = commands.Bot(command_prefix=["C%", "c%"], help_command=None, experimental_event_style=True)

# Bot Joined Server
@bot.event
async def on_bot_add(bot):
    server = bot.server
    if server.default_channel_id:
            channel = server.default_channel or await server.fetch_default_channel()
    else:
        return
    bot_add_embed = Embed(
        title = f"Thanks for adding me!", 
        description = f"Thanks for adding me in {server.name}!, I am happy to assist you in anything! Start with %help to get to know more about me!",
        color = 0x64CC8C,
    )
    bot_add_embed.set_footer(text="👑 Owner: SapphireRP 🆘 Support: .gg/Sunk-Bar")
    await channel.send(embed=bot_add_embed)


# Ping Commands
@bot.command()
async def ping(ctx):
    latency = bot.latency
    latency_embed = Embed(
        title = "Clank Bot's Ping",
        description = f"My ping is `{round(latency * 1000)}ms`",
        color = 0x64CC8C
    )
    latency_embed.set_footer(text="👑 Owner: SapphireRP 🆘 Support: .gg/Sunk-Bar")
    await ctx.send(embed=latency_embed)

# Status Commands
@bot.command()
async def status(ctx, *, status: str = None):
        if ctx.author.id != 'dODKnlPm':  # replace with your user ID
            await ctx.send("This command is only for the owner of the bot.")
            return
        if status is None:
            status = "Currently in development, please report bugs to .gg/Sunk-Bar"
        else:
            prefix = ctx.prefix
            status = status.replace(prefix + "status ", "")

        print(f'Logged in as {bot.user.name} ({bot.user.id})')
        emoteid = 1913999  # use an id that in your server or is a global emoji
        content = f"{status}"  # use a status that in your server or is a global status"
        botuserid = 'AQ1r1vgA'
        token = f'{config.TOKEN}'

        url = f"https://www.guilded.gg/api/v1/users/{botuserid}/status"

        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {token}"
        headers["Accept"] = "application/json"
        headers["Content-type"] = "application/json"

        data = {"content": content, "emoteId": emoteid}

        try:
            resp = requests.put(url, headers=headers, json=data)
        except Exception as e:
            import traceback
            print(''.join(traceback.format_exception(e, e, e.__traceback__)))

# Cogs Loading
cogs_path = os.path.join(os.getcwd(), "Cogs")
for foldername in os.listdir(cogs_path):
    folder_path = os.path.join(cogs_path, foldername)
    if os.path.isdir(folder_path):
        cogs_folder = 'Cogs'
        for filename in os.listdir(folder_path):
            if filename.endswith('.py'):
                if foldername == '__pycache__':
                    continue  # Skip any "__pycache__" folders if present
                module = f'{cogs_folder}.{foldername}.{filename[:-3]}'  # Module name without the ".py" extension
                try:
                    bot.load_extension(module)
                    print(f'Loaded extension: {module}')
                except Exception as e:
                    print(f'Failed to load extension: {module}\n{type(e).__name__}: {str(e)}')

# Run the bot
bot.run(f"{config.TOKEN}")
