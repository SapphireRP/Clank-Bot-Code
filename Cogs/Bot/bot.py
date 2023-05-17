from main import GUILD_ID, requests, CaseInsensitiveDict, SuggestChannel, BugReportChannel, bot, guilded, Embed, commands, config


# Define a new cog for Bug Reporting

# Define a new cog for Bug Reporting
class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingRequiredArgument):
            command = ctx.command.qualified_name
            param = error.param.name
            error_message = f"Missing argument: `{param}` for command `{command}`."
            error_embed = Embed(
                title="Command Error",
                description=error_message,
                color=0xFF9999
            )
            await ctx.reply(embed=error_embed)
        else:
            if isinstance(error, commands.CommandInvokeError):
                error = error.original  # Get the original exception from CommandInvokeError
            if isinstance(error, guilded.Forbidden):
                error_message = "I don't have permission to perform that action."
            elif isinstance(error, guilded.HTTPException):
                error_message = "An error occurred while executing the command. Please try again later."
            else:
                error_message = "An unknown error occurred while executing the command."
            error_embed = Embed(
                title="Command Error",
                description=error_message,
                color=0xFF9999
            )
            error_embed.set_thumbnail(url="https://img.guildedcdn.com/asset/GenericMessages/nothing-here.png")
            await ctx.reply(embed=error_embed)

    @commands.command()
    async def help(self, ctx):
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
	
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {bot.user.name} ({bot.user.id})')
        emoteid = 1851862  # use an id that in your server or is a global emoji
        content = 'Currently in development, please report bugs to gg/Clank-Bot'
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

def setup(bot):
	bot.add_cog(Bot(bot))