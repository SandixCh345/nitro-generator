from cgitb import text
from dis import dis
from distutils import command
from http.client import responses
from operator import le
from os import name, read
from pydoc import cli
from random import choice, randint, random
from sqlite3 import adapt
from tkinter import Variable
from turtle import color, st, title
from webbrowser import get
from attr import has
import discord
from discord import colour
from discord import channel
from discord import embeds
from discord import role
from discord import guild
from discord.ext import commands
import json
from discord.ext.commands.core  import has_guild_permissions
import asyncio
import random
import os
import datetime
from typing import ValuesView


        


client = commands.Bot(command_prefix = '*')




intents = discord.Intents().all()
client = commands.Bot(command_prefix = '*')






@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"Gleda 50+ usera"))
    print('Bot je uspjesno pokrenut. Devolper=!                Mastour#3351')




@client.command(aliases=['p'])
async def ping(ctx):
    await ctx.send('Pong brate!')

@client.command(aliases=['w'])
async def wlcm(ctx):
    await ctx.send ('Dobrodosao') 
#kick
@client.command(aliases=['boot'])
async def kick(ctx, member:discord.Member, *, resason=None):
    if(not ctx.author.guild_permissions.kick_members):
        await ctx.send('Za ovo ti treba permisija "Izbacivanje clanova" ')
        return
    await member.kick(reason=resason)
    await ctx.send(f'{member.mention} je kikovan iz nekog razloga ')

#ban
@client.command(aliases=['hammer'])
async def ban(ctx, member:discord.Member, *, reason=None):
    if(not ctx.author.guild_permissions.ban_members):
        await ctx.send('Treba ti permisija  "Banovanje clanova "')
        return
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} je banovan zbog krsenja pravila')
    await member.send(f"Ti si banovan na serveru od strane {guild.name} bota zbog {reason}")

#unban
@client.command(aliases=['forgive'])
async def unban(ctx, *, member):
   
     




    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name,user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanovan je  {user.mention}')
            return


#brisanje

@client.command(aliases=['purge'])
async def obrisi(ctx, *, amount=11):
    if(not ctx.author.guild_permissions.manage_messages):
        await ctx.send('Za dovrsavanje ove komande trebas imati dozvolu "Upravljane porukama"')
        return
    amount = amount+1
    if amount > 201:
        await ctx.send('Ne mozes obrisati vise od 200 poruka.')
    else:
        await ctx.channel.purge(limit=amount)
        await ctx.send('Poruke su uspijesno obrisane')





#slowmode

@client.command(case_insensitive=True)
async def slowmode(ctx, time:int):
    if(not ctx.author.guild_permissions.manage_messages):
        await ctx.send('Ne mozes pokreniti komandu jer nemas permisiju "Postavljane slowdowna"')
        return
    if time == 0:
        await ctx.send('Slowmode je trenutno maknut')
        await ctx.channel.edit(slowmode_delay = 0 )
    elif time > 21600:
            await ctx.send('Ne mozes staviti Slowmode veci od 6 sati')
            return
    else:
        await ctx.channel.edit(slowmode_delay = time)
        await ctx.send(f"Slowmode je postavljen na '{time}' sekundi")

#profile

@client.command()
@commands.has_permissions(kick_members=True)
async def profil(ctx, member : discord.Member):
    embed = discord.Embed(title = member.name, description = member.mention, colour = discord.Color.blue())
    embed.add_field(name = "Njegov Id", value =member.id, inline = True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url=ctx.author.avatar_url, text = f"Trazeno od {ctx.author.name}")
    await ctx.send(embed=embed)



#customhelp

@client.command(name='komande')
async def komande(ctx):
    embed = discord.Embed(
        title = 'Komande',
        description = 'Ovdje su komande',
        colour = discord.Colour.purple()
    )
    embed.set_footer(text=f'Trazeno od {ctx.author}',icon_url=ctx.author.avatar_url)
    embed.add_field(name='Generalno' ,value='`*ping`, `*profil` , `*wlcm` , `*info` ,`*informacije`,`*korona`,`*profilna`')
    embed.add_field(name='Za staff team',value='`*ban`, `*kick`, `*unban`, `*purge`, `*slowmode`, `*mutiraj`')
    await ctx.send(embed=embed )

@client.command()
async def info(ctx):
    embed=discord.Embed(
        title ='Info',
        description = 'O nasem serveru'
    )

    embed.set_footer(text=f'Trazeno je od korisnika {ctx.author} ova informacija' , icon_url=ctx.author.avatar_url)
    embed.add_field(name='Sve opcenito o serveru' ,value='`Nas server je napravljen 11.10.2021 godine sa ciljem da okupi puno ljudi sa prostora bivse Jugoslavije.Cilj nam je dodzi do za sada do 100 membera.Staff team ce uvijek biti aktivan 24/7 za pomoc nasim clanovima te cemo se pobrinuti da svaki member pamti ovaj server po svemu lijepom.Uzivajte`')
    await ctx.send(embed=embed)

#mute
@client.command(despriction="Mutiraj")
@commands.has_permissions(manage_messages=True)
async def mutiraj(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Mutiran")
    

    if not mutedRole:
        mutedRole = await guild.create_role(name="Mutiran")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=False, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Mutiran je {member.mention} zbog razloga {reason}")
    await member.send(f"Ti si mutiran na serveru od strane {guild.name} bota zbog {reason}")





@client.command(pass_context = True)
async def covid(ctx):
    embed = discord.Embed(title = "Kolke su sanse da se zarazis od Corone u ovom mjesecu od 1/100", description = (random.randint(1, 101)), color = (0xF85252))
    await ctx.send(embed = embed)






@client.event
async def kurac(ctx,*,question):
    responses =["Pozitivan",
                "nEGATIVAN",]
    await ctx.send(f"Question: {question}\nAnswer:{random,choice(responses)}")





@client.command()
async def profilna(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author

        memberAvatar = member.avatar_url

        avaEmbed = discord.Embed(title = f"{member.name} i njegova profilna")
        avaEmbed.set_image(url= memberAvatar)

        await ctx.send(embed = avaEmbed)





@client.command()
async def korona(ctx):
    korona_lista = ["Pozitivan","Negativan","Omikron","Izolacija","Kuga","Pasha jebac"]
    embed = discord.Embed(title="Test na Koronu",description=f"Tvoj nalaz je {random.choice(korona_lista)}")
    await ctx.send(embed = embed)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Ukuco si krivu komandu koja nije nadena,da vidis komande ukucaj  ``*komande``')




   

     
   












 





@client.command(pass_context=True)
async def informacije(ctx):
    embed = discord.Embed(title="Server Informacije",color=0x9208ea)
    
    
    
    
    
    
    
    
    
    embed.add_field(name="Ime servera",value=ctx.message.guild.name, inline=True)
    
    
    
    
    
    
    embed.add_field(name="Memberi",value=len(ctx.message.guild.members,))
    
    
    
    
    
    embed.add_field(name="Kanali", value=len(ctx.message.guild.channels))
    
    
    
    
    
    embed.add_field(name="Trazeno od ", value=str(ctx.message.author.mention))
    
    
    
    
    
    
    
    embed.set_footer(text="Napravlejno by Mastour#3351")
    
    
    
    
    
    
    await ctx.send(embed=embed)



    









    

















    



   












   









                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    












client.run ('OTEyMzYyNjc1NjU1Mjc4NTky.YZu19A.c1Log6GuoWOr8tO3jVjH6oNM8Y0')