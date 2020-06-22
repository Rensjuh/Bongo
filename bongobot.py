import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
from discord.ext import commands, tasks
import datetime
from itertools import cycle
import os
 
 
Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()
client.remove_command('help')
status = cycle(['Naar twitch.tv/rensjuhgamed kijken!', 'Op de bongo!', '!help'])
 
 
@client.event
async def on_ready():
    change_status.start()
    print('Klaar om op de bongo te spelen')
   
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))
 
 
@client.event
async def on_member_join(member):
    await member.send(f"{member.mention} Welkom op **{member.guild}**:tada:. *Klik op deze link voor belangrijke informatie:* https://discord.gg/hRxeYVS")
 
   
@client.event
async def on_message(message):  
    await client.process_commands(message)
    if message.content.startswith('!gelukskoekje'):
        randomlist = ["je ademt vandaag", "je stoot vandaag je kleine teen", "je eet vandaag een frikandelbroodje", "je gaat vandaag Roblox spelen", "Je wint een potje Skywars", "Rens doet vandaag een stream <:pog:693880370256412803>", "Je stinkt naar bedorven kaas", "Rens upload een <:yt:638120086229483524> video!", "Je wordt gebackseatgamed door Michiel <:feelsbadman:718811535622799370>", "wipwap", "Je stinkt, sorry", "Je wordt uitgescholden door ToxicGOD<:pepehands:720552286572511243>", "Stijn doet knophoofd<:kekw:719842435168993310>", "Victor steelt je ace<:sad:718811355733557368>", "Pim is een ei:egg:", "Victor admin aboest<:feelsbadman:718811535622799370>", "ToxicGOD vind zichzelf weer te leuk<:kekw:719842435168993310>", "Victor fietst weg van een beef<:lul:640154268409659393>", "Jens steelt je koekje<:what:718811593500131381>", "Jan-Julius steelt je lolly<:what:718811593500131381>"]
        await message.channel.send(random.choice(randomlist))
    if message.content.startswith('!coinflip'):
        randomlist = ["Kop<:kop:720560457391276052>", "Munt<:munt:720560561154424932>"]
    if message.content.startswith('!rustchance'):
        randomlist = ["<:blauw:721459552746340475>", "<:rood:721459537172758558>"]
        await message.channel.send(random.choice(randomlist))
    if message.content.startswith('!cf'):
        randomlist = ["Kop<:kop:720560457391276052>", "Munt<:munt:720560561154424932>"]
        await message.channel.send(random.choice(randomlist))
    if message.content == '!author':
        await message.channel.send(f'https://www.twitch.tv/rensjuhgamed')
    if message.content == '!moskau':
        await message.channel.send(f'https://bit.ly/2pKs9SN')
    if message.content == '!twitch':
        await message.channel.send(f'https://www.twitch.tv/rensjuhgamed')
    if message.content == '!youtube':
        await message.channel.send(f'https://bit.ly/2MSjshZ')
    if message.content == '!bongo':
        await message.channel.send(f'https://bit.ly/2z2H27q')
    if message.content == '!twitter':
        await message.channel.send(f'https://bit.ly/2UjS5AN')
    if message.content == '!ping':
        await message.channel.send(f'Pong! {round(client.latency * 1000})ms')
       
 
@client.command()
@commands.has_role('📌Staff')
async def verwijder(ctx, amount=5):
 amount = int(amount)
 await ctx.channel.purge(limit=amount+1)
 amount = str(amount)
 await ctx.send(amount+" bericht(en) verwijderd!", delete_after=3)
 
 
@client.command()
@commands.has_role('📌Staff')
async def kick(ctx, member : discord.Member, * , reason=None):
 await member.kick(reason=reason)
 await ctx.send("Gekicked!", delete_after=3)
 
 
@client.command()
@commands.has_role('📌Staff')
async def ban(ctx, member: discord.Member, *, reason = None):
 await member.ban(reason=reason)
 await ctx.send("Gebanned!", delete_after=3)
 
 
@client.command()
@commands.has_role('📌Staff')
async def unban(ctx, userx: int):
 ban_list = await ctx.guild.bans()
 
 for users in ban_list:
 
   user = users.user
 
   if user.id == userx:
   
     await ctx.guild.unban(user)    
 await ctx.send("Geunbanned!", delete_after=3)
 
 
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
   
    embed = discord.Embed(
        colour = discord.Colour.greyple()
    )
   
    embed.set_author(name='Help')
    embed.add_field(name='***Member commands***', value='~~-------------------~~', inline=False)
    embed.add_field(name='!gelukskoekje', value='Wat ga jij vandaag meemaken?', inline=False)
    embed.add_field(name='!bongo', value='🥁', inline=False)
    embed.add_field(name='!help', value='Laat dit zien!', inline=False)
    embed.add_field(name='!rustchance', value='Voor de verslaafde onder ons!', inline=False)
    embed.add_field(name='!ping', value='🏓', inline=False)                                        
    embed.add_field(name='!twitter', value='<:twitter:640157206464954368>', inline=False)
    embed.add_field(name='!moskau', value='Het goddelijkste lied op deze aardebol!', inline=False)
    embed.add_field(name='!twitch', value='<:twitch:638119216968630283>', inline=False)
    embed.add_field(name='!youtube', value='<:yt:638120086229483524>', inline=False)
    embed.add_field(name='!author', value=':wink:', inline=False)
    embed.add_field(name='!coinflip', value='Kun je niet beslissen? Laat het lot voor je beslissen!<:kop:720560457391276052>', inline=False)
    embed.add_field(name='***Staff commands***', value='~~-------------------~~', inline=False)
    embed.add_field(name='!kick', value='Kickt de persoon die stout doet', inline=False)
    embed.add_field(name='!ban', value='Bant de persoon die stout doet', inline=False)
    embed.add_field(name='!verwijder [aantal berichten]', value='Verwijder het aantal berichten dat jij invoert!', inline=False)
   
   
    await author.send(embed = embed)
    await ctx.message.add_reaction("✅")
 
client.run(os.getenv('TOKEN'))
