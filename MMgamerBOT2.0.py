import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
	embed=discord.Embed(title="Stats for {}".format(user.name), description="Show {} stats".format(user.name), color=0x66009D)
	embed.add_field(name="Name: ", value=user.name, inline=False)
	embed.add_field(name="ID: ", value=user.id, inline=False)
	embed.add_field(name="Status: ", value=user.id, inline=False)
	embed.add_field(name="Top role: ", value=user.top_role, inline=False)
	embed.add_field(name="Joined at: ", value=user.joined_at, inline=False)
	await bot.say(embed=embed)
@client.command(pass_context=True)
async def warn(ctx, userName: discord.Member, , reason: str):
    if "Staff" in [role.name for role in ctx.message.author.roles] or ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(title="Warned", description="{} You have been warned for **{}***".format(userName.mention, reason))
        embed.set_thumbnail(url=userName.avatar_url)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await client.say(embed=embed)
    else:
        await client.say("{} :x: You are not allowed to use this command!".format(ctx.message.author.mention))

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

@bot.event
async def on_message(message):
	await bot.process_commands(message)
bot.run("NDM3NjU3MDUzNzU5MDEyODY0.Db5UQA.PEoybWlGnQTzEPB6XfeQhrJFvlM")
