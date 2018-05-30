

@bot.command(pass_context=True)
async def pfp(ctx, member: discord.Member):
     embed=discord.Embed(title="The users profile picture", color=0x66009D)
     embed.set_image(url=member.avatar_url)
     embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="MMgamerBOT by MMgamer#3477 & EpicShardGamingYT#9597")
     await bot.say(embed=embed)



@bot.command(pass_context=True)
async def help(ctx, module="all"):
    module = module.lower()
    if module == "info":
                embed=discord.Embed(title="Help", description="""
                Info Commands:
                • `!ftn pc <player>` - Gets fortnite players status.
                •`!info <@mention>` - Gets some info on the server.
                •`!all_servers` - Shows all servers the bot is in.
                •`!urban <querey>` -Searches the urbandic for your query
                """)
                await bot.say(embed=embed)
    elif module == 'all':
        embed=discord.Embed(title="All Help", description="""
        Info Commands:
        •`!ftn pc <player>` - Gets fortnite players status (pc only).
        •`!info <@mention>` - Gets some info on the server.
        •`!all_servers` - Shows all servers the bot is in.
        •`!urban <querey>` -Searches the urbandic for your query
        •`!pfp <@user>` - Shows a users's profile picture
        •`!all_servers` - Shows all servers the bot is in.
        Fun commands:
         •`!cat` - Gets you a select cat GIF.
         •`!dog` - Gets you a cool dog GIF.
         •`!slap` - Slapy Slpay Scratchy Bitey.
         •`!add` - Adds two numbers.
         •`!multipy` - Multipys two numbers.
        Moderation Commands:
        •`!warn <user> <reason>` - Warns a user (Also DM's)
        •`!kick <@user>` - Kicks the user from the server
        •`!ban <@user>` - Bans a user for the server
        •`!mute <@user>` - Mutes a user
        •`!leave` - Makes the bot leave the server
        Misc Commands:
        •`!ami <@role>|<rolename>` - Tells you if you have that specific role in the server
        •`!github` - Gets you the bot's github repo
        """, color=0x66009D)
        embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="MMgamerBOT by MMgamer#3477 & EpicShardGamingYT#9597")
        await bot.say(embed=embed)
    elif module == 'info':
            embed=discord.Embed(title="Help", description="""
            Fun commands:
            •`!cat` - Gets you a select cat GIF.
            •`!dog` - Gets you a cool dog GIF.
            •`!slap` - Slapy Slpay Scratchy Bitey.
            •`!add` - Adds two numbers.
            •`!multipy` - Multipys two numbers.
         """, colour=0x66009D)   
        embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="MMgamerBOT by MMgamer#3477 & EpicShardGamingYT#9597")
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
async def invite(ctx):
    embed=discord.Embed(title="Invite The Bot To Your Server!",description="The bot's invite link: https://goo.gl/FLPW5b", color=0x66009D)
    embed.set_author(icon_url="http://www.roofscreen.com/mediafiles/product_category_icons/10_strong-chain-icon.png",name="Link")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def mute(ctx, member: discord.Member, time: int, *, reason):
    if ctx.message.author.server_permissions.administrator != True:
        return await bot.say("No perms!")
    await bot.send_message(member, f"You have been muted for {time} Seconds in {ctx.message.server.name}! Be sure to read the rules again! ")
    role = discord.utils.get(ctx.message.server.roles, name="Muted")
    await bot.add_roles(member, role)
    embed = discord.Embed(title="MUTED", description="{} You have been Muted for **{}** Seconds. Reason: {}".format(member.mention, time, reason), color=0x66009D)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)
    await asyncio.sleep(time)
    await bot.remove_roles(member, role)
    await bot.send_message(member, f"You have been unmuted! Be careful!")
    embed = discord.Embed(title="Member unmuted", description="{} Has been UnMuted".format(member.mention), color=0x66009D)
    embed.set_author(name=member.name, icon_url=member.avatar_url)
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
    embed = discord.Embed(color=0xE9A72F)
    embed.set_author(icon_url=user.avatar_url, name="Here's some info about {}".format(user.name))
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Name:", value=user.name, inline=True)
    embed.add_field(name="Status:", value=user.status, inline=True)
    embed.add_field(name="Users ID:", value=user.id, inline=True)
    embed.add_field(name="Users Highest role:", value=user.top_role.mention, inline=True)
    embed.add_field(name="Discriminator:", value=user.discriminator, inline=True)
    embed.add_field(name="Playing:", value=user.game, inline=True)
    embed.add_field(name="Joined", value=user.joined_at, inline=True)
    embed.add_field(name="Account Creation:", value=user.created_at, inline=True)
    embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="MMgamerBOT by MMgamer#3477 & EpicShardGamingYT#9597")
    await client.say(embed=embed)



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
    embed.set_author(name="MMgamer")
    embed.add_field(name="This is a field", value="no it isn't", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def get_inv(ctx):
    for i in bot.servers:
        var = await bot.create_invite(i.channels[0])
        await bot.say(str(var))

@bot.command(pass_context=True)
async def ball(ctx, question):
    await bot.say(random.choice(["NO", "Ofc", "Magic dosen't have all the awnsers", "No Idea"]))

@bot.command(pass_context=True)
async def leave(ctx):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '397745647723216898':
        if ctx.message.author != bot.user:
            await bot.leave_server(ctx.message.server)
        else:
            await bot.say(":x: No Perms")
    else:
        await bot.say("To low perms")
@bot.command(pass_context=True)
async def remove_all_servers(ctx):
    if ctx.message.author.id == '279714095480176642':
        tmp = bot.servers
        for server in tmp:
            await bot.leave_server(server)
        await bot.say("Operation completed")
@bot.command(pass_context=True)
async def say(ctx, *, message):
    if ctx.message.author.id == bot.user.id:
        return
    else:
        await bot.say(message)

@bot.command(pass_context=True)
async def reboot(ctx):
    if not (ctx.message.author.id == '279714095480176642' or ctx.message.author.id == '449641568182206476'):
        return await bot.say(":x: You **Must** Be Bot Owner Or Developer")
    await bot.logout()
@bot.event
async def on_message(message):
    await bot.process_commands(message)
@bot.event
async def on_member_join(member: discord.Member):
    if member.server.id == '422083182167588864':
        embed = discord.Embed(title="User Joined!", description="{} Has Just Joined Us! Welcome them!".format(member.name), color=0x66009D)
        embed.set_thumbnail(url=member.avatar_url)
        await bot.send_message(bot.get_channel('437163805512826899'), embed=embed)
    else:
        for i in member.server.channels:
            if i.name.upper() == 'Welcome':
                chl = i

        embed = discord.Embed(title="User Joined!", description="{} Has Just Joined Us! Welcome them!".format(member.name), color=0x66009D)
        embed.set_thumbnail(url=member.avatar_url)
        try:
            await bot.send_message(chl, embed=embed)
        except Exception as e:
            print(e)







bot.run(os.getenv('TOKEN'))
