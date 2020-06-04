import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
from discord import Game
from discord.ext import commands, tasks
import datetime
from itertools import cycle


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()
client.remove_command('help')
status = cycle(['Naar twitch.tv/rensjuhgamed kijken!', 'Op de bongo spelen!'])


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
        randomlist = ["je ademt vandaag", "je stoot vandaag je kleine teen", "je eet vandaag een frikandelbroodje", "je gaat vandaag Roblox spelen", "Je wint een potje Skywars", "Rens doet vandaag een stream <:pog:693880370256412803>"]
        await message.channel.send(random.choice(randomlist))
    if message.content.startswith('!vsco'):
        randomlist = ["sksksk", "and i oop", "SAVE THE TURTLES"]
        await message.channel.send(random.choice(randomlist))
    if message.content == '!ewa':
        await message.channel.send(f'{message.author.name} ewa niffo!')
    if message.content.startswith('!pingme'):
        await message.channel.send(f'{message.author.mention} fakka')
    if message.content == '!author':
        await message.channel.send(f'https://www.twitch.tv/rensjuhgamed')
    if message.content == '!moskau':
        await message.channel.send(f'https://bit.ly/2pKs9SN')
    if message.content.startswith('!lenny'):
        randomlist = ["( ͡° ͜ʖ ͡°)", "( ͡ʘ ͜ʖ ͡ʘ)", "(ง ͠° ͟ل͜ ͡°)ง", "( ͡ಥ ͜ʖ ͡ಥ)"]
        await message.channel.send(random.choice(randomlist))
    if message.content == '!twitch':
        await message.channel.send(f'https://www.twitch.tv/rensjuhgamed')
    if message.content == '!poep':
        await message.channel.send(f'https://bit.ly/306vlYE')
    if message.content == '!youtube':
        await message.channel.send(f'https://bit.ly/2MSjshZ') 
    if message.content == '!bongo':
        await message.channel.send(f'https://bit.ly/2z2H27q')
        

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
    embed.add_field(name='!poep', value='P O E P!', inline=False)
    embed.add_field(name='!moskau', value='Het goddelijkste lied op deze aardebol!', inline=False)
    embed.add_field(name='!twitch', value=':wink:', inline=False)
    embed.add_field(name='!youtube', value=':100:', inline=False)
    embed.add_field(name='!vsco', value='rEd De sChIlDpAdPaDdEn', inline=False)
    embed.add_field(name='!lenny', value=' ͡° ͜ʖ ͡°', inline=False)
    embed.add_field(name='!author', value=':wink:', inline=False)
    embed.add_field(name='!ewa', value=':sunglasses:', inline=False)
    embed.add_field(name='!pingme', value='fakka:sunglasses:', inline=False)
    embed.add_field(name='***Staff commands***', value='~~-------------------~~', inline=False)
    embed.add_field(name='!kick', value='Kickt de persoon die stout doet', inline=False)
    embed.add_field(name='!ban', value='Bant de persoon die stout doet', inline=False)
    embed.add_field(name='!verwijder [aantal berichten]', value='Verwijder het aantal berichten dat jij invoert!', inline=False)
    
    
    await author.send(embed = embed)

client.run(os.getenv('TOKEN'))
