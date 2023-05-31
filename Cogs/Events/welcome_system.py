import guilded
from guilded.ext import commands

class Welcome_System(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Welcoming System
    @commands.Cog.listener()
    async def on_member_join(self, event: guilded.MemberRemoveEvent):
        server = event.server
        if server.default_channel_id:
            channel = server.default_channel or await server.fetch_default_channel()
        else:
            return
        embed = guilded.Embed(
            title="Member Joined",
            description=f"{event.member.mention} joined {server.name}",
            color= 0x2ecc71
        )
        await channel.send(embed=embed)

    # Leaving System
    @commands.Cog.listener()
    async def on_member_remove(self, event: guilded.MemberRemoveEvent):
        server = event.server
        if server.default_channel_id:
            channel = server.default_channel or await server.fetch_default_channel()
        else:
            return
        # Extra metadata
        if event.banned:
            cause = 'Was Banned From'
            title = 'Member Banned'
            color = 0x800000
        elif event.kicked:
            cause = 'Has Been Kicked From'
            title = 'Member Kicked'
            color = 0xff0000
        else:
            cause = 'Has Left'
            title = 'Member Left'
            color = 0x006400
        embed = guilded.Embed(
            title=title,
            description=f"{event.member.mention} {cause} {server.name}",
            color=color
        )
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Welcome_System(bot))
