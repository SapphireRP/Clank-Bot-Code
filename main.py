# Imports
import guilded
import config
from guilded.ext import commands
from guilded import Embed

# Global Constants
BugReportChannel = "50e7c931-a9bf-4029-a45a-5c0843e272ea"
GUILD_ID = "NRgbbqvj"
SuggestChannel = "ad12dc31-90e6-4440-b6cc-277cc5b9ffd1"


# Bot Initialization
bot = commands.Bot(f"{config.PREFIX}")
bot.remove_command('help')  # Remove the built-in help command


# Bot Commands
@bot.command()
async def ping(ctx):
    await ctx.send('pong!')


# Event Handlers
@bot.event
async def on_member_join(member: guilded.Member):
    # Get the welcome channel
    welcome_channel = guilded.Server.default_channel

    # Send a welcome message
    await welcome_channel.send(f"Welcome to the guild, {member.mention}!")


# Bot Commands
# Help Command
@bot.command()
async def help(ctx):
    help_embed = Embed(
        title="Welcome To Clank Bot",
        description="Clank Bot offers multiple features for servers, including moderation, logging, economy, and interaction commands, while prioritizing community satisfaction above all else.\n\n"
                    "<📚 Commands>\n\n"
                    "**[optional] • <required>**\n\n"
                    "• Filter A Page Using The REACTIONS On This Message\n\n"
                    "• General - Enable\n"
                    "<📚 Commands>",
        color=0x64CC8C,
    )
    help_embed.set_footer(text="👑 Owner: SapphireRP 🆘 Support: gg/Clank-Bot")
    await ctx.send(embed=help_embed)


# Bug Report Command
# Define a new cog for Bug Reporting
class BugReport(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Create a new command for Bug Reporting
    @commands.command()
    async def report(self, ctx, *, bug_report):
        guild = await bot.fetch_server(GUILD_ID)
        if guild is None:
            await ctx.send("Sorry, I couldn't find the Support Server.")
            return

        channel = await bot.fetch_channel(BugReportChannel)
        if channel is None:
            await ctx.send("Sorry, I couldn't find the Bug Report channel.")
            return

        try:
            # Create an embed containing the Bug Report
            report_embed = Embed(
                title="New Bug Report",
                description=f"By **{ctx.author}:**\n`{bug_report}`",
                color=0xFF9999,
            )
            report_embed.set_thumbnail(url="https://img.guildedcdn.com/asset/GenericMessages/not-found.png")
            report_embed.set_footer(text=f"Reported in #{ctx.channel.name} by {ctx.author}")
            await channel.send(embed=report_embed)
            await ctx.send("Thank you for reporting the bug. We will look into it!")
        except Exception as e:
            error_embed = Embed(
                title="An error occurred!",
                description=f"An error occurred while trying to send your bug report: {e}",
                color=0xFF9999,
            )
            error_embed.set_thumbnail(url="https://img.guildedcdn.com/asset/GenericMessages/nothing-here.png")
            await ctx.reply(private=True, embed=error_embed)


# Add the Bug Reporting cog to the bot
bot.add_cog(BugReport(bot))

# Suggest Command
# Define a new cog for Suggestions
class Suggestion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Create a new command for Suggestions
    @commands.command()
    async def suggest(self, ctx, *, suggestion):
        guild = await bot.fetch_server(GUILD_ID)
        if guild is None:
            await ctx.send("Sorry, I couldn't find the Support Server.")
            return

        channel = await bot.fetch_channel(SuggestChannel)
        if channel is None:
            await ctx.send("Sorry, I couldn't find the Suggestion channel.")
            return

        try:
            # Create an embed containing the Suggestion
            suggest_embed = Embed(
                title="New Suggestion",
                description=f"By **{ctx.author}:**\n`{suggestion}`",
                color=0x7272BF,
            )
            suggest_embed.set_thumbnail(url="https://img.guildedcdn.com/asset/TabEmptyStates/gil_forums.png")
            suggest_embed.set_footer(text=f"Suggested in #{ctx.channel.name} by {ctx.author}")
            await channel.send(embed=suggest_embed)
            await ctx.send("Thank you for reporting the bug. We will look into it!")
        except Exception as e:
            error_embed = Embed(
                title="An error occurred!",
                description=f"An error occurred while trying to send your bug report: {e}",
                color=0xFF9999,
            )
            error_embed.set_thumbnail(url="https://img.guildedcdn.com/asset/GenericMessages/nothing-here.png")
            await ctx.reply(private=True, embed=error_embed)


# Add the Suggestion cog to the bot
bot.add_cog(Suggestion(bot))

# Error Message
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    else:
        try:
            error_embed = Embed(
                title="An error occurred!",
                description=f"An error occurred while trying to send your bug report: {e}",
                color=0xFF9999
            )
            error_embed.set_thumbnail(url="https://img.guildedcdn.com/asset/GenericMessages/nothing-here.png")
            await ctx.reply(private=True, embed=error_embed)
        except:
            print(error)


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
