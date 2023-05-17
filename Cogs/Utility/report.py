from main import GUILD_ID, BugReportChannel, bot, Embed, commands, CB_Not_Found, CB_Nothing_Here

# Bug Report Command
# Define a new cog for Bug Reporting
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
                description=f"Author: `{ctx.author.name} ({ctx.author.id})`\nServer: `{ctx.guild.name} ({ctx.guild.id})`\n\n`{bug_report}`",
                color=0xFF9999,
            )
            report_embed.set_footer(text=f"Reported in #{ctx.channel.name} ({ctx.channel.id})")
            report_embed.set_thumbnail(url=f"{CB_Not_Found}")
            await channel.send(embed=report_embed)
            await ctx.reply(f"{ctx.author}, Thank you for bringing the bug to our attention. We greatly appreciate your diligence in reporting it promptly.", private=True)
        except Exception as e:
            error_embed = Embed(
                title="An error occurred!",
                description=f"An error occurred while trying to send your bug report: {e}",
                color=0xFF9999,
            )
            error_embed.set_thumbnail(url=f"{CB_Nothing_Here}")
            await ctx.reply(private=True, embed=error_embed)

# Add the Bug Reporting cog to the bot
def setup(bot):
	bot.add_cog(BugReport(bot))