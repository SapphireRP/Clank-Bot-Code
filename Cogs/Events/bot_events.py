import guilded
from guilded.ext import commands

log_channel_id = None  # Variable to store the log channel ID

class Joining(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Joining System
    @commands.Cog.listener()
    async def on_member_join(self, event: guilded.MemberJoinEvent):
        server = event.server
        member = event.member
        if server.default_channel_id:
            channel = server.default_channel or await server.fetch_default_channel()
        else:
            return
        welcome_embed = guilded.Embed(
            title="New Member!",
            description=f"{member.mention} has joined {member.guild.name}!",
            color=guilded.Color.green()
            )
        await channel.send(embed=welcome_embed)

    # Leaving System
    @commands.Cog.listener()
    async def on_member_remove(self, event: guilded.MemberRemoveEvent):
        if event.server.default_channel_id:
            channel = event.server.default_channel or await event.server.fetch_default_channel()
        else:
            return
        # Extra metadata
        if event.banned:
            cause = 'Was Banned From'
            title = 'Member Banned'
            color = guilded.Color.dark_red()
        elif event.kicked:
            cause = 'Has Been Kicked From'
            title = 'Member Kicked'
            color = guilded.Color.red()
        else:
            cause = 'Has Left'
            title = 'Member Left'
            color = guilded.Color.teal()
        leaving_embed = guilded.Embed(
            title=title,
            description=f'{event.member.mention} {cause} the server.',
            color=color
        )
        await channel.send(embed=leaving_embed)

def setup(bot):
    bot.add_cog(Joining(bot))
