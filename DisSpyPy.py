import discord
from discord.ext import commands

# Configuration
TOKEN_A = 'acc token here'  # Token for the account
GUILD_A_ID = 6969696969420  # The ID of the source server (Bot A's server)
CHANNEL_A_ID = 6969696969430  # The ID of the target channel (Bot A's channel)

# Bot B's token and channel to send the data
TOKEN_B = 'bot token here'  # Token for Bot B
GUILD_B_ID = 6969696969  # The ID of the target server (Bot B's server)
CHANNEL_B_ID = 69696969699  # The ID of the channel to send the message to (Bot B's channel)

# Unless you know what your doing, do NOT touch anything past this area!

# Create Bot A Client (Self-Bot)
client_a = discord.Client()

# Create Bot B Client
client_b = discord.Client()

# Bot B initialization function
async def init_bot_b():
    await client_b.start(TOKEN_B)

@client_a.event
async def on_ready():
    print(f'Logged in account')
    # Once Bot A is ready, initialize Bot B
    await init_bot_b()

@client_a.event
async def on_message(message):
    # Check if the message is from the specified channel and in Bot A's specified guild
    if message.guild and message.guild.id == int(GUILD_A_ID) and message.channel.id == int(CHANNEL_A_ID):
        print(f"Message received: {message.content}")
        
        # Ensure Bot B is already connected before sending the message
        if client_b.is_ready():
            # Get the guild where Bot B will send the message
            guild_b = client_b.get_guild(int(GUILD_B_ID))
            if guild_b:
                # Get the channel where the message should be sent
                channel_b = guild_b.get_channel(int(CHANNEL_B_ID))
                if channel_b:
                    # Get the author's name or username
                    author_name = message.author.name  # You can also use message.author.display_name for nickname
                    # Send message with the author's name
                    await channel_b.send(f"Message from {author_name} in {CHANNEL_A_ID} (Guild {message.guild.name}): {message.content}")
                else:
                    print("Bot: Channel not found!")
            else:
                print("Bot: Guild not found!")
        else:
            print("Bot: Not connected!")

# Start Bot A (Self-Bot)
client_a.run(TOKEN_A, bot=False)
