# Imports
import guilded
import config
from guilded.ext import commands
from guilded import Embed
import os

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

# Run the bot
bot.run(f"{config.TOKEN}")
