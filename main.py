# Imports
import guilded
import config
from guilded.ext import commands
from guilded import Embed
import os
import requests
from requests.structures import CaseInsensitiveDict
import json

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

# Load the prefix data from prefixes.json file
def load_prefixes():
    try:
        with open('prefixes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save the prefix data to prefixes.json file
def save_prefixes(prefixes):
    with open('prefixes.json', 'w') as file:
        json.dump(prefixes, file)

# Function to retrieve the prefix for a guild
def get_prefix(bot, message):
    prefixes = load_prefixes()
    guild_prefix = prefixes.get(str(message.guild.id), '!')
    return guild_prefix

# Bot Initialization
bot = commands.Bot(f"{config.PREFIX}", help_command=None, experimental_event_style=True)

# Bot Joined Server
@bot.event
async def on_bot_add(event: guilded.BotAddEvent, member: guilded.Member, guild: guilded.server):
    bot_add_embed = Embed(
        title = f"Thanks for adding me in {guilded.name}!", 
        description = f"Hello {member.mention}, thanks for adding me to {guilded.name}, I am happy to assist you in anything! Start with %help to get to know more about me!",
        color = 0x64CC8C,
    )
    bot_add_embed.set_footer(text="👑 Owner: SapphireRP 🆘 Support: gg/Clank-Bot")
    channel = await guild.fetch_default_channel()
    await channel.send(embed=bot_add_embed)

# Bot Left Server
@bot.event
async def on_bot_remove(guild):
    prefixes = load_prefixes()
    del prefixes[str(guild.id)]
    save_prefixes(prefixes)

# Bot Prefix Message
@bot.event
async def on_message(event: guilded.MessageEvent):
    message = event.message
    author = message.author
    bot_author = author.bot
    if not bot_author:
        prefixes = load_prefixes()
        guild_prefix = prefixes.get(str(message.guild.id), '!')
        if not message.content.startswith(guild_prefix) and message.content.startswith('!'):
            await message.channel.send(f"You used the default prefix. This server has updated its prefix. Please use the updated prefix `{guild_prefix}` instead.")
    await bot.process_commands(message)

# Set Prefix Command
@bot.command()
async def setprefix(ctx, prefix):
    prefixes = load_prefixes()
    prefixes[str(ctx.guild.id)] = prefix
    save_prefixes(prefixes)
    await ctx.send(f"The prefix for this server has been updated to `{prefix}`.")

# Load extensions from each subfolder inside the Cogs folder
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

# Bot Commands
@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

# Status Update
try:
    emoteid = 1851862  # use an id that in your server or is a global emoji
    content = 'Currently in development, please report bugs to gg/Clank-Bot'
    botuserid = 'AQ1r1vgA'
    token = f'{config.TOKEN}'

    import requests;
    from requests.structures import CaseInsensitiveDict

    url = f"https://www.guilded.gg/api/v1/users/{botuserid}/status"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer {token}"
    headers["Accept"] = "application/json"
    headers["Content-type"] = "application/json"

    data = {"content": content, "emoteId": emoteid}

    resp = requests.put(url, headers=headers, json=data)
except Exception as e:
    import traceback

    print(''.join(traceback.format_exception(e, e, e.__traceback__)))


# Run the bot
bot.run(f"{config.TOKEN}")
