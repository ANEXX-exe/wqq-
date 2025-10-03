import os
import discord
from discord.errors import Forbidden
from discord import Intents

# التوكن من متغير بيئة
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# نص القوانين بالإنجليزي
RULES_TEXT = """**Server Rules**
1. Be respectful to everyone.
2. No spamming or advertising.
3. No hate speech or harassment.
4. Use channels for their intended purposes.
5. Follow Discord Terms of Service.
"""

WELCOME_DM = """Hello {member_name} 👋

Welcome to **{server_name}**!

Here are the server rules:
{rules}

Enjoy your stay! 🌟
"""

intents = Intents.default()
intents.members = True  # مهم عشان يعرف الأعضاء الجدد

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user} (ID: {client.user.id})")

@client.event
async def on_member_join(member: discord.Member):
    try:
        dm_text = WELCOME_DM.format(
            member_name=member.display_name,
            server_name=member.guild.name,
            rules=RULES_TEXT
        )
        await member.send(dm_text)
        print(f"📩 Sent welcome DM to {member}")
    except Forbidden:
        print(f"❌ Couldn't DM {member} (they may have DMs disabled).")

if __name__ == "__main__":
    if not TOKEN:
        print("❌ ERROR: Set DISCORD_BOT_TOKEN environment variable.")
    else:
        client.run(TOKEN)
