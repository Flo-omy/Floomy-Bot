
import discord
import os
import math
import time
token = os.environ.get("TOKEN")
from discord.ext import commands

client = commands.Bot(command_prefix = "fl!")


@client.event

async def on_ready():
  await client.change_presence(activity=discord.Game(name='fl!'))




@client.command()

async def ping(ctx):
  await ctx.send("Pong! {}ms".format(round(client.latency * 1000)))
  pass

@client.command()
@commands.has_role('King')
async def purge(ctx, amount=10):
  await ctx.channel.purge(limit=amount+1)


@client.command()
@commands.has_role('King')
async def troll(ctx):
  for i in range(1379323232324928420484):
    channel = client.get_channel(888610463556964363)
    await channel.send('<@!778577087241125908> :suh_dude:') 

  

# suggest command
@client.command()
async def suggest(ctx,*,suggestion):
  author=ctx.message.author
  file=open("suggestions.txt","a+")
  file.write(str(author)+" : "+suggestion+"\n")
  embed = discord.Embed(
    title = 'Suggestion',
    description = "This Was Suggested By",
    colour = discord.Colour.orange()
  )

  embed.set_footer(text = "Made By @floomy with .py")
  embed.set_author(name = "floomy#0006")
  embed.add_field(name = author, value = suggestion)
  await ctx.send("Suggestion Submitted")
  channel = client.get_channel(888610463556964363)
  msg = await channel.send(embed=embed)
  await msg.add_reaction('👍')
  await msg.add_reaction('👎')

# kick command
@client.command()
@commands.has_role('King')
async def kick(ctx,member:discord.Member,*,reason=None):
  await member.kick(reason=reason)
  await channel.send(f"cry about it {member.mention} just got kicked for {reason}.")

# BANNED BAHAHA LOSER
@client.command()
@commands.has_role('King')
async def ban(ctx,member:discord.Member,*,reason='no reason'):
  await member.ban(reason=reason)
  await ctx.send(f'cry about it, this bozo {member} just got banned for {reason}')


# unbanned 
@client.command()
@commands.has_role('King')
async def unban(ctx,*,member):
  BanList = await ctx.guild.bans()
  MemberName, MemberDiscrim = member.split('#')
  for BanEntry in BanList:
    user = BanEntry.user
    if (MemberName,MemberDiscrim) == (user.name,user.discriminator): 
      await ctx.guild.unban(user)
      await ctx.send(f'{user.mention} has been unbanned ig idk')
      return

# add roles
@client.command()
@commands.has_role('King')
async def create_role(ctx,name,*,reason=None):
  role = await ctx.guild.create_role(name=name,colour=discord.Colour.orange(),hoist=True,mentionable=True,reason=reason)
  await ctx.send(f'{ctx.guild.owner.mention}, {ctx.author} has made the role {role.mention}')
# join
@client.event
async def on_member_join(member):
  channel = client.get_channel(887358079107207258)
  await channel.send(f"Welcome {member.mention} to our server, hope you like it here.")
# leave
@client.event
async def on_member_remove(member):
  channel = client.get_channel(887358079107207258)
  await channel.send(f" bye {member.mention}, bozo...")







client.run(token)
print("Floomy Online and Running")