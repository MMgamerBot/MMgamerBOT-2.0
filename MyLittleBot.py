import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord import game
import random
import asyncio
import time
import os
 
Client = discord.Client() #Initialise Client
client = commands.Bot(command_prefix = "!") #Initialise client bot
 
chat_filter = ["FUCK", "CRAP", "SHIT", "CYKA BLYAT", "HOLY SHIT", "ASSHOLE", "HTTPS://DISCORD.GG/"] #you can alter the chat filter as you please!
bypass_list = ["361436146317918220", "432258796556124160"]


@client.event
async def on_ready():
    print("Bot is online and connected to Discord")
    await client.change_presence(game=discord.Game(name="mmgamer.eu"))

    
@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")
    if message.content.upper() == "CHOCOLATE CHIP COOKIE":
        await client.send_message(message.channel, ":cookie:")
    if message.content.upper().startswith('!SAY'):
        if message.author.id == "279714095480176642":
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, " :x: You do not have permission")
    if message.content.upper().startswith("!AMIOWNER"):
        if "422335818330275840" in [role.id for role in message.author.roles]:
             await client.send_message(message.channel,"Yea your my owner!")
        else:
            await client.send_message(message.channel,":x: You Wish")
    if message.content.upper().startswith("!LEGHELP"):
            await client.send_message(message.channel,"My Commands are: !say; !help; !ping")
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** You're not allowed to sware or advertise here!")
                except discord.errors.NotFound:
                    return
    if message.content.upper().startswith('!HELP'):
        emb = (discord.Embed(description="My commands are:\n `!help`- Gets you this list\n `!say`- The bot says what you tell it to say\n `!amiowner` - Checks Bot Ownership status\n `!cat` - Cat Gif\n `!clear` - Clears ALL messages in a channel\n `!invite` - Gets the bots invite link\n `!github` - Gets the bots GitHUB repo\n `!ping` - Time to render the command in ms\n `!8ball` - The magic ball awnsers you\n `!dog` - Dog Gif\n Need more help? Join our support server: https://discord.gg/dENQG9u", colour=0x66009D))
        emb.set_author(icon_url='http://mmgamer.eu/assets/images/mmgamer-3507x2480.png', name="Help")
        await client.send_message(message.channel, embed=emb)
    if message.content.upper().startswith('!INFO'):
        emb = (discord.Embed(description="**Developed by:**\n MMgamer#3477 & HugoFk#0001\n **Other Developers:**\n EpicShardGamingYT#9597 & Alpha#8978\n **Bot Prefix:**\n `!`\n **Commands:**\n Do `!help`"))
        emb.set_author(icon_url="http://mmgamer.syte.host/MMgamerBOT.png", name="Bot Info")
        await client.send_message(message.channel, embed=emb)
    if message.content.upper().startswith('!INVITE'):
        emb = (discord.Embed(description="Wanna invite me cool! Here is the link: https://goo.gl/FLPW5b have fun!", colour=0x66009D))
        emb.set_author(name="Invite", icon_url='https://www.iconsdb.com/icons/preview/purple/link-xxl.png')
        await client.send_message(message.channel, embed=emb)
    if message.content.upper().startswith('!GITHUB'):
        emb = (discord.Embed(description="That GitHUB repo: https://github.com/MM-coder/mmgamerbot", colour=0x66009D))
        emb.set_author(name="Github", icon_url='https://major.io/wp-content/uploads/2014/08/github.png')
        await client.send_message(message.channel, embed=emb)
    if message.content.upper().startswith('!CAT'):
        emb = discord.Embed(colour=0x66009D)
        emb.set_image(url="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
        await client.send_message(message.channel, embed=emb)
    if message.content.upper().startswith('!CLEAR'):
        tmp = await client.send_message(message.channel, 'Clearing Stuff Up...')
        async for msg in client.logs_from(message.channel):
            await client.delete_message(msg)
    if message.content.upper().startswith('!DOG'):
        emb = discord.Embed(colour=0x66009D)
        emb.set_image(url="https://media.giphy.com/media/RQSuZfuylVNAY/giphy.gif")
        await client.send_message(message.channel, embed=emb)
    if message.content.upper().startswith("!PING"):
        t1 = time.perf_counter()
        t2 = time.perf_counter()
        await client.send_message(message.channel, ":ping_pong: | Pong! Yes, I am alive... - Time taken: {}ms".format(round((t2-t1)*1000)))
    if message.content.upper().startswith("!8BALL"):
        msg = await client.send_message(message.channel, ":8ball:")
        await asyncio.sleep(1)
        await client.edit_message(msg, new_content=":8ball: :8ball:")
        await asyncio.sleep(1)
        await client.edit_message(msg, new_content=":8ball: :8ball: :8ball:")
        await asyncio.sleep(1)
        await client.delete_message(msg)
        await client.send_message(message.channel, random.choice(["It is certain :8ball: ", "It is decidedly so :8ball: ", "Without a doubt :8ball:", "Yes definitely :8ball: ", "You may rely on it :8ball: ", "As I see it, yes :8ball: ", "Most likely :8ball: ", "Outlook good :8ball: ", "Yes :8ball: ", "Signs point to yes :8ball: ", "Reply hazy try again :8ball: ", "Ask again later :8ball: ", "Better not tell you now :8ball: ", "Cannot predict now :8ball: ", "Concentrate and ask again :8ball: ", "Don't count on it :8ball: ", "My reply is no :8ball: ", "My sources say no :8ball: ", "Outlook not so good :8ball: ", "Very doubtful :8ball:"]))

@client.event
async def on_member_join(member):
  canal = client.get_channel("422083182167588866")
  regras = client.get_channel("422083232855621632")
  msg = "Welcome {}\ read the {}".format(member.mention, regras.mention)
  await client.send_message(canal, msg) #Repalce Canal with member to DM the message

@client.event
async def on_member_remove(member):
   canal = client.get_channel("423328604911304708")
   msg = "Bye! {}".format(member.mention)
   await client.send_message(canal, msg) #Repalce Canal with member to DM the message
    
 
client.run(os.getenv('TOKEN')) #For heroku only
