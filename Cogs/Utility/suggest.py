from main import GUILD_ID, SuggestChannel, bot, Embed, commands, CB_Forums, CB_Nothing_Here

# Suggest Command
# Define a new cog for Suggestions
class Suggest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
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
                    description=f"Author: `{ctx.author.name} ({ctx.author.id})`\nServer: `{ctx.server.name} ({ctx.server.id})`\n\n`{suggestion}`",
                    color=0x7272BF,
            )
            suggest_embed.set_footer(text=f"Suggested in #{ctx.channel.name} ({ctx.channel.id})")
            suggest_embed.set_thumbnail(url=f"{CB_Forums}")
            await channel.send(embed=suggest_embed)
            await ctx.send("Thank you for reporting the bug. We will look into it!")
        except Exception as e:
            error_embed = Embed(
                title="An error occurred!",
                description=f"An error occurred while trying to send your suggestion: {e}",
                color=0xFF9999,
            )
            error_embed.set_thumbnail(url=f"{CB_Nothing_Here}")
            await ctx.reply(private=True, embed=error_embed)

def setup(bot):
	bot.add_cog(Suggest(bot))