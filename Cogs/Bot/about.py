from main import Embed, commands

# Define a new cog for Bug Reporting
class About(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def about(self, ctx):
        
        about_embed = Embed(
            title=":members_CB: About Clank-Bot",
            description="Clank Bot provides a range of features for servers, including Moderation, Logging, Economy/Farming, Interactions, and Profile, XP commands and features.\n\nOur top priority is ensuring community satisfaction and we strive to deliver the best experience for your server.",
            color=0x64CC8C,
        )
        about_embed.add_field(name=":integration_CB: Owner:", value="`SapphireRP`", inline=True)
        about_embed.add_field(name=":support_CB: Support Server:", value="'.gg/Sunk-Bar'", inline=True)
        about_embed.add_field(name=":link_CB: Prefix:",value="`C% or c%`", inline=True)
        about_embed.add_field(name=":link_CB: Written in:",value="`Python`", inline=True)
        about_embed.add_field(name=":link_CB: Library:",value="`Guilded.py`", inline=True)
        about_embed.set_footer(text="👑Owner: SapphireRP 🆘Support: .gg/Sunk-Bar")
        await ctx.send(embed=about_embed)


def setup(bot):
    bot.add_cog(About(bot))