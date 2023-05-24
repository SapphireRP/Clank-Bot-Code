import guilded
from guilded.ext import commands
import json

class EventLogging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Message Edit
    #@commands.Cog.listener()
    #async def on_message_update(self, event: guilded.MessageUpdateEvent):
    #    before = event.before
    #    after = event.after
    #    message = event.message
    #    if before.author.bot:
    #6        return  # Ignore messages edited by bots#
        #em = guilded.Embed(
        #    embed_title = "f{before.author.name} Edited A Message In #{before.channel.name}",
        #    embed_color = 0x32343D
        #    embed_description = f"{before.author.name} Edited A Message In #{before.channel.name}:",
        #    )
        #em.add_field(name="Before", value=f"`{before.content}`")
        #em.add_field(name="After", value=f"`{after.content}`")
        #await message.channel.send(embed=em)

    # Nickname Change
    @commands.Cog.listener()
    async def on_member_update(self, event: guilded.MemberUpdateEvent):
        before = event.before
        after = event.after
        message = event.message
        if before.nick != after.nick:
            # Log the message deletion event
            with open("config.json", "r") as f:
                config = json.load(f)
                embed = guilded.Embed()
                if after.nick is not None:
                    embed.title = f"{before.name} Changed Their Nickname:"
                else:
                    embed.title = f"{before.name} Resetted Their Nickname:"
                if before.nick is not None:
                    embed.add_field(name="Before", value=f"`{before.nick}`")
                else:
                    embed.add_field(name="Before", value=f"`{before.name}`" + " (Default name)")
                if after.nick is not None:
                    embed.add_field(name="After", value=f"`{after.nick}`")
                else:
                    embed.add_field(name="After", value=f"`{before.name}`" + " (Default name)")
                await message.channel.send(embed=embed)

    # Message Delete
    #@commands.Cog.listener()
    #async def on_message_delete(self, event: guilded.MessageDeleteEvent):
        #message = event.message
        #if message.author.bot:
        #    return  # Ignore messages deleted by bots

        # Log the message deletion event
        #with open("config.json", "r") as f:
        #    config = json.load(f)
            
            #em = guilded.Embed(
            #    embed_title = "A Message Has Been Deleted:",
            #    embed_description = f"{message.author.name} Deleted A Message In #{message.channel.name}:"
            #    embed_color = 0x32343D
            #)
        #em.add_field(name="Content", value=f"{message.content}")
        #await message.channel.send(embed=em)




def setup(bot):
    bot.add_cog(EventLogging(bot))