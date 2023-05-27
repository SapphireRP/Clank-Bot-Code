import guilded
from guilded import File, Color, Member
from guilded.ext import commands
from easy_pil import Editor, load_image_async, Font
import os

log_channel_id = None  # Variable to store the log channel ID

class Joining(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #import os

    # Joining System
    @commands.Cog.listener()
    async def on_member_join(self, event: guilded.MemberJoinEvent):
        channel = event.server.default_channel
        background = Editor("./assets/pic1.jpg")
        image_path = os.path.abspath("./assets/Clank_Logo.png")
        profile_image = await load_image_async(image_path)
        profile = Editor(profile_image).resize((150, 150)).circle_image()
        poppins = Font.poppins(size=50, variant="bold")

        background.paste(profile, (325, 90))
        background.ellipse((325,90), 150, 150, outline="white",stroke_width=5)
        background.text((400, 320), f"{event.member.display_name} Welcome to {event.server.name}!", font=poppins, color="green", align="center")

        file = File(fp=background.image_bytes, filename="./assets/pic1.jpg")
        await channel.send(file=file)

    # Leaving System
    @commands.Cog.listener()
    async def on_member_remove(self, event: guilded.MemberRemoveEvent):
        if event.server.default_channel:
            channel = event.server.default_channel
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
            description=f'{event.member.display_name} {cause} the server.',
            color=color
        )
        await channel.send(embed=leaving_embed)





def setup(bot):
    bot.add_cog(Joining(bot))
