from main import Embed, commands

# Define a new cog for Bug Reporting
class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def help(self, ctx, page: int = 1):
        if page == 1:
            help_embed = Embed(
            title=":Clank_Logo: Welcome To Clank Bot",
            description="Clank Bot offers multiple features for servers. Including moderation, logging, economy, and interaction commands. While prioritizing community satisfaction above all else.\n\n",
            color=0x64CC8C,
            )
            help_embed.add_field(name=":textchannel_CB: Page 2:", value="`General Commands`", inline=True)
            help_embed.add_field(name=":certifiedmoderator_CB: Page 3:", value="`Moderation Commands`", inline=True)
            help_embed.add_field(name=":library_CB: Page 4:", value="`Farming Commands`", inline=True)
            help_embed.add_field(name=":shop_CB: Page 5:", value="`Profile & XP Commands`", inline=True)
            help_embed.add_field(name=":settings_CB: Page 6:", value="`Developer Commands`", inline=True)
            help_embed.set_footer(text="📄Page: 1/6, 👑Owner: SapphireRP 🆘Support: gg/Clank-Bot")
            await ctx.send(embed=help_embed)
            #message = await ctx.send(embed=help_embed)
            #await message.add_reaction("90002144")
            #await message.add_reaction("90002140")
        elif page == 2:
            help_embed = Embed(
            title="[WIP] General Commands",
            color=0x64CC8C,
            )
            help_embed.add_field(name=":partner_CB: **General Commands**", value="", inline=False)

            help_embed.add_field(name="Help", value="`Brings you to the help menu`", inline=True)
            help_embed.add_field(name="About", value="`Get info about the bot`", inline=True)
            help_embed.add_field(name="Report", value="`Report a bug`", inline=True)
            help_embed.add_field(name="Suggest", value="`Suggest a feature`", inline=True)
            help_embed.add_field(name="Ping", value="`Pong!`", inline=True)

            help_embed.add_field(name=":star_CB: **Premium Commands**", value="", inline=False)

            help_embed.add_field(name="Premium", value="`WIP, Coming Soon`", inline=True)

            help_embed.set_footer(text="📄Page: 2/6, 👑Owner: SapphireRP 🆘Support: gg/Clank-Bot")
            await ctx.send(embed=help_embed)
            #message = await ctx.send(embed=help_embed)
            #await message.add_reaction("90002144")
            #await message.add_reaction("90002140")
        elif page == 3:
            help_embed = Embed(
            title="[WIP] Moderation Commands",
            color=0x64CC8C,
            )
            help_embed.add_field(name=":certifiedmoderator_CB: **Moderation Commands**", value="", inline=False)

            help_embed.add_field(name="Warn", value="`Warn a user`", inline=True)
            help_embed.add_field(name="Unwarn", value="`Unwarn a user`", inline=True)
            help_embed.add_field(name="Warns", value="`Get a list of warns of a user`", inline=True)

            help_embed.add_field(name="Ban", value="`Ban a user`", inline=True)
            help_embed.add_field(name="Unban", value="`Unban a user`", inline=True)
            help_embed.add_field(name="Bans", value="`Get a list of banned users`", inline=True)

            help_embed.add_field(name="Kick", value="`Kick a user`", inline=True)

            help_embed.add_field(name="Mute", value="`Mute a user`", inline=True)
            help_embed.add_field(name="Unmute", value="`Unmute a user`", inline=True)

            help_embed.add_field(name="Purge", value="`Purge certain amount of messages`", inline=True)

            help_embed.add_field(name=":rules_CB: **Case Commands**", value="", inline=False)

            help_embed.add_field(name="Case", value="`Get info about a case`", inline=True)
            help_embed.add_field(name="Deletecase", value="`Delete a case`", inline=True)
            help_embed.add_field(name="Caseinfo", value="`Get info about a case`", inline=True)

            help_embed.add_field(name=":link_CB: Role Commands", value="", inline=False)

            help_embed.add_field(name="Roleinfo", value="`Get info about a role`", inline=True)
            help_embed.add_field(name="Rolecreate", value="`Create a role`", inline=True)
            help_embed.add_field(name="AddRole", value="`Add a role to a user`", inline=True)
            help_embed.add_field(name="RemoveRole", value="`Remove a role from a user`", inline=True)

            help_embed.set_footer(text="📄Page: 3/6, 👑Owner: SapphireRP 🆘Support: gg/Clank-Bot")
            await ctx.send(embed=help_embed)
            #message = await ctx.send(embed=help_embed)
            #await message.add_reaction("90002144")
            #await message.add_reaction("90002140")
        elif page == 4:
            help_embed = Embed(
            title="[WIP] Farming Commands",
            color=0x64CC8C,
            )
            help_embed.set_footer(text="📄Page: 4/6, 👑Owner: SapphireRP 🆘Support: gg/Clank-Bot")
            await ctx.send(embed=help_embed)
            #message = await ctx.send(embed=help_embed)
            #await message.add_reaction("90002144")
            #await message.add_reaction("90002140")
        elif page == 5:
            help_embed = Embed(
            title="Profile & XP Commands",
            color=0x64CC8C,
            )
            help_embed.set_footer(text="📄Page: 5/6, 👑Owner: SapphireRP 🆘Support: gg/Clank-Bot")
            await ctx.send(embed=help_embed)
            #message = await ctx.send(embed=help_embed)
            #await message.add_reaction("90002144")
            #await message.add_reaction("90002140")
        elif page == 6:
            help_embed = Embed(
            title="[WIP] Developer Commands",
            color=0x64CC8C,
            )
            help_embed.set_footer(text="📄Page: 6/6, 👑Owner: SapphireRP 🆘Support: gg/Clank-Bot")
            await ctx.send(embed=help_embed)
            #message = await ctx.send(embed=help_embed)
            #await message.add_reaction("90002144")
            #await message.add_reaction("90002140")
        else:
            await ctx.send("Invalid help page.")

def setup(bot):
    bot.add_cog(Help(bot))