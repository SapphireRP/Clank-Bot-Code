import guilded
from guilded.ext import commands

class EventLogging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_update(self, event: guilded.MessageUpdateEvent):
        before = event.before
        after = event.after
        guild = event.server
        if before.author.bot:
            return  # Ignore messages edited by bots
        
        if before.content != after.content:
            # Log the message edit event
            channel = await guild.fetch_channel('790f5bb8-8f1c-4fa5-9ed8-518ebacf50a0')
            if channel:
                embed = guilded.Embed()
                embed.title  = "A message has been edited:"
                embed.description = f"{before.author.name} edited a message in #{before.channel.name}:"
                embed.add_field(name="Before", value=f"`{before.content}`")
                embed.add_field(name="After", value=f"`{after.content}`")
                await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_update(self, event: guilded.MemberUpdateEvent):
        before = event.before
        after = event.after
        guild = event.server
        if before.nick != after.nick:
            # Log the nickname change event
            channel = await guild.fetch_channel('790f5bb8-8f1c-4fa5-9ed8-518ebacf50a0')
            if channel:
                embed = guilded.Embed()
                if after.nick is not None:
                    embed.title = f"{before.name} changed their nickname:"
                else:
                    embed.title = f"{before.name} resetted their nickname:"
                if before.nick is not None:
                    embed.add_field(name="Before", value=f"`{before.nick}`")
                else:
                    embed.add_field(name="Before", value=f"`{before.name}`" + " (Default name)")
                if after.nick is not None:
                    embed.add_field(name="After", value=f"`{after.nick}`")
                else:
                    embed.add_field(name="After", value=f"`{before.name}`" + " (Default name)")
                await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, event: guilded.MemberRemoveEvent):
        author = event.member
        guild = event.server
        kicked = event.kicked
        banned = event.banned
        if author.bot:
            return
        if banned == True:
            channel = await guild.fetch_channel('790f5bb8-8f1c-4fa5-9ed8-518ebacf50a0')
            em = guilded.Embed(title="A member was banned:", description="Username: `{}`\nUser ID: `{}`".format(author.name, author.id), color=0x363942)
            await channel.send(embed=em)
        elif kicked  == True:
            channel = await guild.fetch_channel('790f5bb8-8f1c-4fa5-9ed8-518ebacf50a0')
            em = guilded.Embed(title="A member was kicked:", description="Username: `{}`\nUser ID: `{}`".format(author.name, author.id), color=0x363942)
            await channel.send(embed=em)
        else:
            channel = await guild.fetch_channel('790f5bb8-8f1c-4fa5-9ed8-518ebacf50a0')
            em = guilded.Embed(title="A member has left:", description="Username: `{}`\nUser ID: `{}`".format(author.name, author.id), color=0x363942)
            await channel.send(embed=em)

    @commands.Cog.listener()
    async def on_message_delete(self, event: guilded.MessageDeleteEvent):
        message = event.message
        guild = event.server
        if message.author.bot:
            return  # Ignore messages deleted by bots
        
        # Log the message deletion event
        channel = await guild.fetch_channel('790f5bb8-8f1c-4fa5-9ed8-518ebacf50a0')
        if channel:
            embed = guilded.Embed()
            embed.title = "A message have been deleted:"
            embed.description = f"{message.author.name} deleted a message in #{message.channel.name}:"
            embed.color = 0x32343D
            embed.add_field(name="Content", value=f"{message.content}")
            await channel.send(embed=embed)
    
    # Joining System
    @commands.Cog.listener()
    async def on_member_join(self, event: guilded.MemberJoinEvent, member: guilded.Member): 
        if event.server.default_channel_id:
            channel = event.server.default_channel or await event.server.fetch_default_channel()
        else:
            return
        welcome_embed = Embed(
            title="New Member!",
            description=f"{member.mention} has joined {member.guild.name}!",
            color=guilded.Color.green()
            )
        """Says when a member joined."""
        await channel.send(embed=welcome_embed)

    # Leaving System
    @commands.Cog.listener()
    async def on_member_remove(event: guilded.MemberRemoveEvent, member: guilded.Member):

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
            color = guilded.Color.pink()

        leaving_embed = Embed(
            title=f"{title}",
            description=f'<@{member.name}> {cause} the server.',
            color =f"{color}",
        )
        await channel.send(embed=leaving_embed)
        
def setup(bot):
    bot.add_cog(EventLogging(bot))