
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import datetime

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

#Check list
#Spam filter
#Level system
#Currency system


#doesn't show images
@client.event
async def on_message_edit(before, after):
    if before.author == client.user:
        return
    if before.author.bot:
        return
    await client.send_message(client.get_channel('419978620535046144'), "**{0}** edited: {1} **in {2}**".format(before.author, before.content, before.channel))
    await client.send_message(client.get_channel('419978620535046144'), "**To**: {0}".format(after.content))

#doesn't show images
@client.event
async def on_message_delete(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return
    await client.send_message(client.get_channel('419978620535046144'), "**{0}'s** message was deleted in **{1}:** {2}".format(message.author, message.channel, message.content))



@client.event
async def on_member_join(member):
    embed = discord.Embed(title="Member Joined", description="{0} has joined".format(member.mention), timestamp = datetime.datetime.utcnow(), color=0x42f4dc)
    await client.send_message(client.get_channel('419357471379816480'), embed=embed)


@client.event
async def on_member_remove(member):
    embed = discord.Embed(title="Member Left", description="{0} has left".format(member.mention), timestamp = datetime.datetime.utcnow(), color=0x42f4dc)
    await client.send_message(client.get_channel('419357471379816480'), embed=embed)

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return
    if message.author.bot:
        return
    #doesn't show image only links
    #if message.attachments != []:
     #   await client.send_message(client.get_channel('473267074714697761'), message.attachments)
    
        
                   
@client.event
async def on_ready():
    print("Bot is ready")
    embed=discord.Embed(title="Ready", description="Ultron is online and ready to hack", timestamp = datetime.datetime.utcnow(), color=0x42f4dc) 
    #await client.send_message(client.get_channel('452324747926175746'), embed=embed)

#invoke by doing ?hack @user
@client.command(pass_context=True)
@commands.has_any_role("Mod", "Admin")
async def hack(ctx, user: discord.Member):
    e1=discord.Embed(title="Hacking...", description="Gathering data... please wait", timestamp = datetime.datetime.utcnow(), color=0x42f4dc)
    e2=discord.Embed(title="Hacked", description="Data gathered and sent to your dm **{0}**".format(ctx.message.author), timestamp = datetime.datetime.utcnow(), color=0x42f4dc)
    e3=discord.Embed(title="Hacked", description="Your data has been gathered **{}**".format(user), timestamp = datetime.datetime.utcnow(), color=0x42f4dc)
    e4=discord.Embed(title="Data", description="pteranondon has the Data, message him", timestamp = datetime.datetime.utcnow(), color=0x42f4dc)
    msg = await client.say(embed=e1) 
    await asyncio.sleep(3)
    await client.edit_message(msg, embed=e2)
    await client.send_message(user, embed=e3)
    await client.send_message(ctx.message.author, embed=e4)
    
#kick command
#needs to be formatted in a embed    
@client.command(pass_context=True)
@commands.has_any_role("Mod", "Admin")
async def kick(ctx, user: discord.Member):
    await client.say(":thumbsup: {} was successfully kicked.".format(user.name))
    await client.kick(user)
    
#ban command
#needs to be formatted in a embed  
@client.command(pass_context=True)
@commands.has_role("Admin")
async def ban(ctx, user: discord.Member):
    await client.say(":thumbsup: {} was successfully banned.".format(user.name))
    await client.ban(user)
    
#say command
@client.command(pass_context=True)
@commands.has_any_role("Mod", "Admin")
async def say(ctx, *args):
    mesg = ' '.join(args)
    await client.delete_message(ctx.message)
    return await client.say(mesg)

#Custom check EX
def my_custom_check():
    def predicate(ctx):
        return ctx.message.author.id
    return commands.check(predicate)

#working with custom check
@client.command(pass_context=True)
@my_custom_check()
async def hi(ctx):
   await client.say("Hi")
   
#invoke command by typing ?mute @user time reason
@client.command(pass_context = True)
@commands.has_any_role("Mod", "Admin")
async def mute(ctx, member: discord.Member, arg1, *args2):
    time = int(arg1) * 60
    dtime = int(arg1)
    reason = ' '.join(args2)
    embed2=discord.Embed(title="Muted", description="You were muted for **{0}** and for **{1}** minutes by **{2}**.".format(reason, dtime, ctx.message.author), timestamp = datetime.datetime.utcnow(), color=0x42f4dc) 
    role = discord.utils.get(member.server.roles, name='Muted')
    await client.delete_message(ctx.message)
    await client.add_roles(member, role)
    embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}** for **{2}** minutes! and **{3}**".format(member, ctx.message.author, dtime, reason), timestamp = datetime.datetime.utcnow(), color=0x42f4dc)
    #await client.say(embed=embed)
    await client.send_message(member, embed=embed2)
    await client.send_message(client.get_channel('419978620535046144'), embed=embed)
    await asyncio.sleep(time)
    await client.remove_roles(member, role)

#invoke by doing ?unmute @user
@client.command(pass_context = True)
@commands.has_any_role("Mod", "Admin")
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(member.server.roles, name='Muted')
    await client.remove_roles(member, role)
    await client.delete_message(ctx.message)
    embed=discord.Embed(title="Unmuted", description="**{0}** was unmuted by **{1}**".format(member, ctx.message.author), timestamp = datetime.datetime.utcnow(), color=0x42f4dc)
    #await client.say(embed=embed)
    await client.send_message(client.get_channel('419978620535046144'), embed=embed)

#invoke by using ?warn @user reason
@client.command(pass_context = True)
@commands.has_any_role("Mod", "Admin")
async def warn(ctx, member: discord.Member, *args):
    wreason = ' '.join(args)
    embed=discord.Embed(title="Warned", description="**{0}** was warned by **{1}** for **{2}**".format(member, ctx.message.author, wreason),  timestamp = datetime.datetime.utcnow(), color=0x42f4dc)
    embed2=discord.Embed(title="Warned", description="You've been warned for **{0}** by **{1}**.".format(wreason, ctx.message.author), timestamp = datetime.datetime.utcnow(), color=0x42f4dc)
    await client.delete_message(ctx.message)
    #await client.say(embed=embed)
    await client.send_message(member, embed=embed2)
    await client.send_message(client.get_channel('419978620535046144'), embed=embed)

#purge command ex: ?purge 2-100
@client.command(pass_context = True)
@commands.has_any_role("Mod", "Admin")
async def purge(ctx, number):   
    mgs = [] #Empty list to put all the messages in the log
    number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)
    embed=discord.Embed(title="Purge", description="**{0}** purged **{1}** messages in **{2}**.".format(ctx.message.author, number, ctx.message.channel), timestamp = datetime.datetime.utcnow(), color=0x42f4dc)
    await client.say(embed=embed)
    await client.send_message(client.get_channel('419978620535046144'), embed=embed)

#invoke by doing ?avatar @user
@client.command(pass_context = True)
async def avatar(ctx, member: discord.Member):
    av = member.avatar_url
    embed=discord.Embed(title="Avatar", color=0x42f4dc)
    embed.set_image(url=av)
    await client.say(embed=embed) 


client.run("Xm8SGF1wm7F2PXJKzVoaJlYjDq8MZfus")


