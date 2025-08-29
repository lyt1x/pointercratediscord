import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Activity, ActivityType, app_commands
import requests
import collections
import json
import sys
import asyncio
import random
import time
import datetime
import traceback
from colorama import init, Fore, Back, Style
from math import exp, log

init(convert=True)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
Bot = commands.Bot(command_prefix='.', intents=intents)
Bot.remove_command('help')

with open('token.txt', 'r') as f:
    token = f.readline()

def list_progress(position, progress, requirement):
    return (score_old(position) * (5 ** ((progress - requirement) / (100 - requirement)))) / 10


def score_old(position):
    if (55 < position) & (position <= 150):
        return 56.191 * 2 ** ((50.947 - position) * (log(50) / 99)) + 6.273
    elif (35 < position) & (position <= 55):
        return 212.61 * 1.036 ** (1 - position) + 25.071
    elif (20 < position) & (position <= 35):
        return 166.611 * 1.0099685 ** (2 - position) - 31.152
    elif (0 < position) & (position <= 20):
        return 149.61 * (1.168 ** (1 - position)) + 100.39
    else:
        return 0


def score_old2(position):
    position = int(position)
    if (125 < position) & (position <= 150):
        return 150 * exp((1 - position) * log(1 / 30) / (-149))
    elif (50 < position) & (position <= 125):
        return 60 * (2.333 ** ((51 - position) * (log(30) / 99))) + 1.884
    elif (20 < position) & (position <= 50):
        return -100 * (1.01327 ** (position - 26.489)) + 200
    elif (0 < position) & (position <= 20):
        return 149.61 * (1.168 ** (1 - position)) + 100.39
    else:
        return 0


def exceptionn():
    ex_type, ex_value, ex_traceback = sys.exc_info()
    trace_back = traceback.extract_tb(ex_traceback)
    stack_trace = list()

    for trace in trace_back:
        stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))

    print("Exception type : %s " % ex_type.__name__)
    print("Exception message : %s" % ex_value)
    print("Stack trace : %s" % stack_trace)


def premiumcheck(name):
    with open('premium.json', 'r') as f:
        premium = json.load(f)
    if name in premium:
        return f"\n\n{premium[name]}"
    else:
        return ""


def admincheck(id):
    list = [736345968429105224, 317293763640950784]
    if id in list:
        return True
    else:
        return False

class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

@Bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith('.'):
        pass
    else:
        #sk = ["ск","сакупен серклз","сакупен сёрклз"]
        #for i in sk:
            #if i in message.content:
                #await message.delete()
                #print('dasd')
        return
    if message.channel.id != 950344047711617034:
        if message.channel.id == 1192310541566365698 or message.channel.id == 1049026645970927730 or message.channel.id == 1010097225814261810 or message.channel.id == 977445612595343402 or message.channel.id == 885098980344733727:
            with open('profiles.json', 'r') as f:
                        data = json.load(f)
            if str(message.author.id) not in data:
                if message.content != ".profile":
                    await message.channel.send('прежде чем юзать бота пропиши 1) .profile 2) .edit pointercrate <ник> (если нет в поинтере первой комманды будет достаточно чтобы юзать бота)\n before using the bot do 1) .profile 2) .edit pointercrate <name> (if you dont have a pointercrate account just do the first command that is enough to use the bot)')
                    return
            await Bot.process_commands(message)
            return
        else:
            return
    # else:
    # print('gg')
    # if message.author.id == 854623342711930910:
    # if random.randint(1,2) == 2:
    # await message.channel.send('<@854623342711930910> https://cdn.discordapp.com/attachments/878916911415582761/887014182053089361/transtw.mp4')
    # return
    # else:
    # print('gg')
    # if message.author.id == 450637380555374594:
    # a = random.randint(1,3)
    # if a == 2:
    # await message.channel.send('<@450637380555374594> https://cdn.discordapp.com/attachments/885098980344733727/927268796731895838/video.mp4')
    # return
    # else:
    # print(a)
    clowns = []
    #clowns = [870386608040464416, 457172397905412096, 518764352929660928, 854623342711930910, 625745446114951183, 667785032038875156]
    if message.author.id in clowns:
        try:
            print(message.content)
            if "<" in message.content:
                content = message.content = f"<@{message.author.id}>"
            else:
                content = message.content
            try:
                content += message.attachments[0].url
            except Exception as e:
                pass
            await message.channel.send(f"<@450637380555374594>: {content}")
        except Exception:
            await message.channel.send(message.attachments[0].url)
        await message.delete()
        print('удалено сообщение', message.author)
        return
    if message.guild is None:
        print(
            f'{Fore.GREEN}{message.author}{Fore.RESET} sent me something in dms, his message: {Fore.CYAN}{message.content}{Fore.RESET}'
        )
        await message.author.send('sadly I dont respond to dms bozo')
        return
    await Bot.process_commands(message)


@Bot.event
async def on_member_join(member):
    with open('gnillist.json','r') as f:
        data = json.load(f)
    list_of_muted_members = data["gnil"]
    print(list_of_muted_members.split(','))
    if (str(member.id) in list_of_muted_members.split(',')):
        muterole = discord.utils.get(member.guild.roles, id=996826394011111555)
        await member.add_roles(muterole)


@Bot.event
async def on_ready():
    print('')
    print('[=========================================================================================]')
    print('')
    print(f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Successfully logged in account [{Fore.LIGHTMAGENTA_EX}{Bot.user}{Fore.RESET}]')
    print('')
    print('[=========================================================================================]')
    print('')
    synced = await Bot.tree.sync()
    print(f'synced {synced} commands')
    # await Bot.change_presence(activity= discord.Streaming(name="lyt1xxx",url='https://www.twitch.tv/lyt1x'))


@Bot.tree.command(name="test",description="cool")
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message("hello")

@Bot.command()
async def gnil(ctx):
    with open('gnillist.json', 'r') as f:
        data = json.load(f)
    role = discord.utils.get(ctx.guild.roles, id=996826394011111555)
    ids = ""
    names = [m.name for m in role.members if str(m.id) not in data["gnil"].split(',')]
    for m in role.members:
        if str(m.id) not in data["gnil"].split(','):
            ids += f"{m.id},"
    await ctx.send(f"{names} {ids}")
    data["gnil"] += ids
    with open('gnillist.json', 'w') as f:
        json.dump(data, f)

@Bot.command()
async def status(ctx):
    if ctx.author.id != 736345968429105224:
        await ctx.send('соси лол')
        return
    while True:
        i = 0
        for member in ctx.guild.members:
            if len(member.activities) != 0:
                if len(member.activities) > 1 or str(member.activities[0].type) == "ActivityType.playing":
                    if str(member.activities[0].type) == "ActivityType.playing":
                        number = 0
                    else:
                        number = 1
                    if member.activities[number].name != None:
                        try:
                            test = int(member.activities[number].timestamps['start']) / 1000
                            now = datetime.datetime.now()
                            hours = now.hour - int(time.strftime('%H', time.localtime(test)))
                            minutes = now.minute - int(time.strftime('%M', time.localtime(test)))
                            seconds = now.second - int(time.strftime('%S', time.localtime(test)))
                            total = hours * 60 * 60 + minutes * 60 + seconds
                            if "genshin impact" in member.activities[number].name.lower():
                                print(f"{member} {member.activities[0].type} {type(member.activities[0].type)}")
                                conversion = datetime.timedelta(seconds=total)
                                message = await ctx.send(f"<@{member.id}> играет в **{member.activities[number].name}** уже **{str(conversion).split(':')[0]}:{str(conversion).split(':')[1]}:{str(conversion).split(':')[2]}**")
                                i += 1
                                emoji = '🐷'
                                await message.add_reaction(emoji)
                        except Exception as e:
                            print(e)
        if i == 0:
            messagee = await ctx.send('Никто не играет в геншин, победа друзья!')
            emojii = '👑'
            await messagee.add_reaction(emojii)
        else:
            await ctx.send('даю вам 30 минут отмыться от позора и проверяю ещё раз...')
        await asyncio.sleep(1800)


cooldown = []
@Bot.command()
async def hazze(ctx, argument):
    if ctx.author.id != 378602408424767498:
        return
    if ctx.author.id in cooldown:
        return
    if argument == "1":
        if ctx.message.author.id == 378602408424767498:
            for i in range(30):
                a = random.randint(1, 700)
                url = f'https://pointercrate.com/api/v2/demons/{a}'
                r = requests.get(url)
                data = json.loads(r.text)
                try:
                    await ctx.send(f'<@282501994952785920> А у тебя на {data["data"]["name"]} скок?')
                except Exception as e:
                    await ctx.send(f'<@282501994952785920> а у тебя на :transgender_flag: скок, {a}')
                await asyncio.sleep(0.2)
        else:
            await ctx.send('этой коммандой может пользоваться только <@736345968429105224> а ты ЛОЩ')
    elif argument == "2":
        randomchik = random.choice(ctx.guild.members).id
        await ctx.send(f"окей <@{randomchik}> пердолил")
        cooldown.append(ctx.author.id)
        await asyncio.sleep(10)
        cooldown.remove(ctx.author.id)
    else:
        if ctx.author.id == 378602408424767498:
            for i in range(int(argument)):
                await ctx.send(f"окей <@{random.choice(ctx.guild.members).id}> пердолил")
        else:
            await ctx.send('иди нахуй')


@Bot.command()
async def vaize(ctx):
    if ctx.message.author.id == 736345968429105224:
        for i in range(30):
            await ctx.send('<@572835658163421184> ПОШЛИ ПАЛЛЕТЫ АБУЗИТЬ ДАУН БЛДЯТЬ')
            await asyncio.sleep(0.1)
    else:
        await ctx.send('этой коммандой может пользоваться только <@736345968429105224> и линел а ты ЛОЩ')


@Bot.command()
async def help(ctx):
    description ='''All the commands:

.player <player name>

.country <country code>

.countryh <country code> (a version with hardests)

.profile <ping whose profile you want to open, if yours - then type nothing>

.edit youtube_channel <link> or .edit pointercrate <pointercrate name>

.top <after which place I should send the top players>

.position <position on the demonlist>

.demon <demon name>

.records <demon name>

.unbeaten <country code>

.beaten <country code> <level>

.search <player name>

.randomd <spots range> (.randomd 76-150)'''
    statsv = '''.player <player name>
.playerh <player name> (sorted by difficulty)
.search <player name>
.country <country code>
.top <number> (.top 75 will send top 75-125)
.hardest <player name> (top 10 hardest completions)
:warning: .countryh <country code> (w/hardests)
:warning: .toph <number> (w/hardests)
'''
    demonss = '''.position <position on the demonlist>
.demon <demon name>
.records <demon name>
.randomd <spots range> (.randomd 76-150)
.listr <percent> <level>
.listed <placement range> (for example .listed 1-20)
.count <levels> (.count zaphkiel, catalyze)
'''
    nationality = '''.unbeaten <country code>
.beaten <country code> <level>
.unique <country code> (levels beaten by only 1 person)
.uniquep <country code> (players that have .unique demons)
.nations <number> (.nations 1 means top 1-20)
'''
    other = '''
.profile <tag someone> (dont tag urself tho)
.edit youtube_channel <link> or .edit pointercrate <name> or .edit text <text>
.leaderboard (best players of the server)'''
    color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    emb = discord.Embed(title='All commands', description="**:warning: Means that the command is slow and will take a long time to send the result**", color=color)
    emb.add_field(name="Stats Viewer",value=statsv,inline=False)
    emb.add_field(name="List Demons", value=demonss, inline=False)
    emb.add_field(name="Nationality", value=nationality, inline=False)
    emb.add_field(name="Other", value=other, inline=False)
    await ctx.send(embed=emb)


@Bot.command()
async def bazan(ctx):
    if ctx.author.id == 736345968429105224:
        i = 0
        for member in ctx.guild.members:
            if member.id != 572835658163421184:
                role = discord.utils.get(Bot.get_guild(ctx.guild.id).roles, id=940968660539953233   )
                try:
                    await member.add_roles(role)
                except Exception as e:
                    print(f'error: {e}')
                i += 1
                print(f"Роль выдана {member} {i}")
    else:
        await ctx.send('мы учтем')


@Bot.command()
@commands.has_role(915949698181914625)
async def petux(ctx, member):
    await ctx.message.delete()
    member = member.replace('@', '')
    member = member.replace('<', '')
    member = member.replace('!', '')
    member = member.replace('>', '')
    guild = Bot.get_guild(ctx.guild.id)
    user = guild.get_member(int(member))
    petusharnya = Bot.get_channel(926113165203365898)
    role = discord.utils.get(guild.roles, id=944239725068288020)
    await user.add_roles(role)
    await asyncio.sleep(1)
    try:
        await user.move_to(petusharnya)
    except Exception:
        pass
    while True:
        await asyncio.sleep(1)
        if role not in user.roles:
            break
        if user not in petusharnya.members:
            try:
                await user.move_to(petusharnya)
            except Exception:
                continue


@Bot.command()
async def embedyt(ctx):
    url = 'https://youtu.be/eCpHyenRz9E'
    await ctx.message.delete()
    emb = discord.Embed(title="(144hz) Digital Descent by GeoStorm (Кринж Demon)",url=url,color=0xFF0000)
    emb.set_author(name='void')
    emb.set_image(url='https://i.ytimg.com/vi/FfSfQFX7EYI/maxresdefault.jpg')
    print(emb)
    await ctx.send(embed=emb)


@Bot.command()
async def transfer(ctx, country=None, *, playerr=None):
    try:
        if country == None:
            await ctx.send('You have to use **.transfer <country> <player**')
        else:
            urlz = f'https://pointercrate.com/api/v1/players?name={playerr}'
            rrr = requests.get(urlz)
            completeddd = []
            testt = {}
            if rrr.text == "[]":
                await ctx.send(f"No one has the name **{playerr}** in pointercrate")
            else:
                text = rrr.text[1:-1]
                text = json.loads(text)
                playerr = text["name"]
                id = text["id"]
                urll = f'https://pointercrate.com/api/v1/players/{id}'
                rr = requests.get(urll)
                test = json.loads(rr.text)
                if test["data"]["nationality"] == None:
                    nationality = 'None'
                else:
                    nationality = f':flag_{test["data"]["nationality"]["country_code"].lower()}:'
                for i in test['data']['records']:
                    if i['progress'] != 100:
                        continue
                    if i['demon']['position'] > 150:
                        continue
                    name = i['demon']['name']
                    testt[i['demon']['position']] = name
                    completeddd.append(i['demon']['position'])
            url = f'https://pointercrate.com/api/v1/nationalities/{country}/'
            j = requests.get(url)
            data = json.loads(j.text)
            description = ''''''
            listt = []
            tuple = []
            a = 0
            for i in data['data']['records']:
                if i['progress'] != 100:
                    continue
                if i['position'] > 150:
                    continue
                shpagu = False
                for j in data['data']['verified']:
                    if i['demon'] == j['demon']:
                        name = i['demon']
                        top = int(i["position"])
                        testt[top] = name
                        tuple.append(top)
                        listt.append(i['demon'])
                        shpagu = True
                        break
                if shpagu == True:
                    continue
                name = i['demon']
                top = int(i["position"])
                testt[top] = name
                tuple.append(top)
                a += 1
            for k in data['data']['verified']:
                if k['position'] > 150:
                    continue
                if k['demon'] in listt:
                    continue
                name = k['demon']
                top = int(k["position"])
                testt[top] = name
                tuple.append(top)
                a += 1
            total = 0
            for i in range(len(completeddd)):
                if completeddd[i] not in tuple:
                    cyka = int(completeddd[i])
                    description += f"**#{int(completeddd[i])} {testt[int(completeddd[i])]}** - {round(float(score_old(int(completeddd[i]))), 2)} \n"
                    total += round(float(score_old(int(completeddd[i]))), 2)
                    #print(score_old(int(completeddd[i])))
            color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            emb = discord.Embed(title=f"{playerr} ---> :flag_{country}: = {total} point(s)",description=description, color=color)
            await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .transfer {country} {playerr}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'got an error: {e}')


@Bot.command()
async def leaderboard(ctx):
    try:
        await ctx.send('this command is very slow so please be patient')
        with open('profiles.json', 'r') as f:
            data = json.load(f)
        tuple = {}
        for k in data:
            id = k
            if ctx.guild.get_member(int(k)) not in ctx.guild.members:
                continue
            k = data[k]['pointercrate']
            if k == None:
                continue
            k = json.loads(requests.get(f'https://pointercrate.com/api/v1/players/{k}').text)["data"]["name"]
            urlll = f'https://pointercrate.com/api/v1/players/ranking/?name_contains={k}'
            rrr = requests.get(urlll)
            for j in json.loads(rrr.text):
                if j['name'].lower() == k.lower():
                    i = j
                    tuple[j['name'].lower()] = ['','', 0]
                    tuple[j['name'].lower()][0] = i['rank']
                    tuple[j['name'].lower()][1] = i
                    tuple[j['name'].lower()][2] = id
        x = dict(sorted(tuple.items(), key=lambda item: int(item[1][0]), reverse=False))
        description = ''''''
        count = 0
        for l in x:
            count += 1
            i = x[l][1]
            if i["nationality"] != None:
                description += f'#{count} :flag_{i["nationality"]["country_code"].lower()}: #{i["rank"]} **{i["name"]}** <@{x[l][2]}> - {round((i["score"]), 2)}\n'
            else:
                description += f'#{count} :flag_white: #{i["rank"]} **{i["name"]}** <@{x[l][2]}> - {round((i["score"]), 2)}\n'
        color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        emb = discord.Embed(title=f"Server Leaderboard", description=description, color=color)
        emb.timestamp = datetime.datetime.now()
        print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .leaderboard')
        await ctx.send(embed=emb)
    except Exception as e:
        exceptionn()
        await ctx.send(f'got an error: {e}')


@Bot.command()
async def nations(ctx, number="1"):
    try:
        if number == None:
            await ctx.send('You have to use **.nations <number> (.number 2 means top 2-22)**')
        else:
            urlll = f'https://pointercrate.com/api/v1/nationalities/ranking/'
            rrr = requests.get(urlll)
            description = ''''''
            j = 0
            data = json.loads(rrr.text)
            for i in data[int(number)-1:int(number)+19]:
                j += 1
                description += f':flag_{i["country_code"].lower()}: #{i["rank"]} {i["nation"]} - {round(float(i["score"]), 2)}\n'
            color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            emb = discord.Embed(title=f"Nations in top {int(number)}-{int(number)+19}",description=description, color=color)
            await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .nations {number}-{int(number)+19}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'got an error: {e}')



@Bot.command()
async def check(ctx, messageid):
    roles = [915949698181914625,885114993434054667,944921584257347604]
    access = False
    for i in roles:
        role = discord.utils.get(ctx.guild                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               .roles, id=i)
        if role in ctx.author.roles:
            access = True
            break
    if access == False:
        msgg = await ctx.send('no access to this command')
        await asyncio.sleep(4)
        await msgg.delete()
        await ctx.message.delete()
        return
    await ctx.message.delete()
    msg = await ctx.fetch_message(messageid)
    text = msg.content
    text = text.split('\n')
    discordid = text[0].replace('@',''); discordid = discordid.replace('!',''); discordid = discordid.replace('<',''); discordid = discordid.replace('>',''); discordid = discordid.replace(' ','')
    player = text[1]
    demon = text[2]
    percent = text[3].replace('%','')
    link = text[4]
    url = f'https://pointercrate.com/api/v1/players?name={player}'
    r = requests.get(url)
    text = r.text[1:-1]
    text = json.loads(text)
    playerr = text["name"]
    id = text["id"]
    urll = f'https://pointercrate.com/api/v1/players/{id}'
    rr = requests.get(urll)
    test = json.loads(rr.text)
    urlll = f'https://pointercrate.com/api/v1/players/ranking/?name_contains={playerr}'
    rrr = requests.get(urlll)
    hardestnumber = 100000
    hardestid = 0
    currentpr = 0
    try:
        listp = json.loads(rrr.text)[0]['score']
    except Exception:
        listp = 0.00
    for i in test["data"]["records"]:
        if 56 == 55:
            print('ебнутый?')
        else:
            if i["progress"] != 100:
                if i['demon']['name'].lower() == demon.lower():
                    currentpr = i['progress']
                continue
            if i["demon"]["position"] < hardestnumber:
                hardestnumber = int(i["demon"]["position"])
                hardestid = int(i["demon"]["id"])
    for i in test["data"]["verified"]:
        if i["position"] < hardestnumber:
            hardestnumber = int(i["position"])
            hardestid = int(i["id"])
    if hardestid != 0:
        hardest = f'https://pointercrate.com/api/v2/demons/{hardestid}'
        harddest = requests.get(hardest)
        htext = json.loads(harddest.text)
        if htext["data"]["position"] < 4:
            hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]} :hot_face: **\n'
        elif htext["data"]["position"] < 11:
            hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]} :smiling_imp: **\n'
        elif htext["data"]["position"] < 26:
            hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]} :fire: **\n'
        elif htext["data"]["position"] < 76:
            hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]}**\n'
        elif htext["data"]["position"] < 151:
            hardest = f'{htext["data"]["name"]} - #{htext["data"]["position"]}\n'
        else:
            hardest = f'*{htext["data"]["name"]} - #{htext["data"]["position"]}*\n'
    else:
        hardest = 'None'
    color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    emb = discord.Embed(title=f"Requested by: {ctx.author}", color=color)
    if discordid != "-":
        emb.add_field(name="Player (Discord):", value=f"<@{discordid}>", inline=False)
    else:
        emb.add_field(name="Player (Discord):", value=f"-", inline=False)
    emb.add_field(name="Player (Pointercrate):", value=playerr, inline=False)
    emb.add_field(name="The record:", value=f"{demon} {percent}%", inline=False)
    emb.add_field(name="Video:", value=f"{link}", inline=False)
    emb.add_field(name="Current progress on the level", value=f"{currentpr}%", inline=False)
    emb.add_field(name="Their list points:", value=round(float(listp), 2), inline=False)
    emb.add_field(name="Their hardest demon:", value=hardest, inline=False)
    chan = Bot.get_channel(944923267838386196)
    await chan.send(embed=emb)
    print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .check {demon} {percent}')


@Bot.command()
async def uniquep(ctx, country=None):
    try:
        if country == None:
            await ctx.send('You have to use **.uniquep <country code>**')
        else:
            url = f'https://pointercrate.com/api/v1/nationalities/{country}/'
            r = requests.get(url)
            data = json.loads(r.text)
            description = ''''''
            listt = []
            tuple = {}
            a = 0
            for i in data['data']['records']:
                print(i)
                if i['position'] > 150:
                    continue
                shpagu = False
                if i['progress'] != 100:
                    if i['position'] > 75:
                        continue
                    for j in data['data']['verified']:
                        if i['demon'] == j['demon']:
                            listt.append(i['demon'])
                            shpagu = True
                            break
                    if shpagu == True:
                        continue
                    if len(i['players']) == 1:
                        name = i['demon']
                        top = int(i["position"])

                        try:
                            tuple[i['players'][0]][2] += 1
                            tuple[i['players'][0]][1] += list_progress(i['position'], i['progress'],json.loads(requests.get(f'https://pointercrate.com/api/v2/demons/{i["id"]}').text)['data']['requirement'])
                        except Exception:
                            tuple[i['players'][0]] = [0, 0, 0]
                            tuple[i['players'][0]][2] += 1
                            tuple[i['players'][0]][1] += list_progress(i['position'], i['progress'],json.loads(requests.get(f'https://pointercrate.com/api/v2/demons/{i["id"]}').text)['data']['requirement'])
                    continue
                for j in data['data']['verified']:
                    if i['demon'] == j['demon']:
                        listt.append(i['demon'])
                        shpagu = True
                        break
                if shpagu == True:
                    continue
                if len(i['players']) == 1:
                    name = i['demon']
                    top = int(i["position"])
                    try:
                        tuple[i['players'][0]][0] += 1
                        tuple[i['players'][0]][1] += score_old(i['position'])
                    except Exception:
                        tuple[i['players'][0]] = [0, 0, 0]
                        tuple[i['players'][0]][0] += 1
                        tuple[i['players'][0]][1] += score_old(i['position'])
                    a += 1
            for k in data['data']['verified']:
                if k['position'] > 150:
                    continue
                if k['demon'] in listt:
                    continue
                name = k['demon']
                top = int(k["position"])
                try:
                    tuple[k['player']][0] += 1
                    tuple[k['player']][1] += score_old(k['position'])
                except Exception:
                    tuple[k['player']] = [0, 0, 0]
                    tuple[k['player']][0] += 1
                    tuple[k['player']][1] += score_old(k['position'])
                a += 1
            x = dict(sorted(tuple.items(), key=lambda item: item[1][1],reverse=True))
            for i in x:
                demon = 'demon'
                progress = 'progress'
                if x[i][0] > 1:
                    demon += 's'
                if x[i][2] > 1:
                    progress += 'es'
                description += f"**{i}** - **{round(float(x[i][1]), 2)}** ({x[i][0]} {demon}, {x[i][2]} {progress})\n"
            color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            emb = discord.Embed(title=f"How many points a player gives to **{data['data']['nation']['nation']} :flag_{country.lower()}:**",description=description, color=color)
            await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .uniquep {country}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'got an error: {e}')


@Bot.command()
async def unique(ctx, country=None):
    try:
        if country == None:
            await ctx.send('You have to use **.unique <country code>**')
        else:
            url = f'https://pointercrate.com/api/v1/nationalities/{country}/'
            r = requests.get(url)
            data = json.loads(r.text)
            description = ''''''
            listt = []
            list = []
            a = 0
            for i in data['data']['records']:
                if i['progress'] != 100:
                    continue
                if i['position'] > 150:
                    continue
                shpagu = False
                for j in data['data']['verified']:
                    if i['demon'] == j['demon']:
                        listt.append(i['demon'])
                        shpagu = True
                        break
                if shpagu == True:
                    continue
                tuple = {}
                if len(i['players']) == 1:
                    name = i['demon']
                    top = int(i["position"])
                    tuple["name"] = name
                    tuple["top"] = top
                    tuple["verified"] = False
                    tuple['victor'] = i['players'][0]
                    list.append(tuple)
                    a += 1
            for k in data['data']['verified']:
                if k['position'] > 150:
                    continue
                if k['demon'] in listt:
                    continue
                tuple = {}
                name = k['demon']
                top = int(k["position"])
                tuple["name"] = name
                tuple["top"] = top
                tuple["verified"] = True
                tuple['victor'] = k['player']
                list.append(tuple)
                a += 1
            tuple = list
            for i in range(a):
                def myFunc(e):
                    return e["top"]
                tuple.sort(key=myFunc)
            for i in range(a):
                top = tuple[i]['top']
                if top < 4:
                    top = f"**#{top} :hot_face:**"
                    if tuple[i]['verified'] == False:
                        description += f"{top} **{tuple[i]['name']}** - {tuple[i]['victor']}\n"
                    elif tuple[i]['verified'] == True:
                        description += f"{top} **{tuple[i]['name']}** - {tuple[i]['victor']} **(Verifier)**\n"
                elif top < 11:
                    top = f"**#{top} :smiling_imp:**"
                    if tuple[i]['verified'] == False:
                        description += f"{top} **{tuple[i]['name']}** - {tuple[i]['victor']}\n"
                    elif tuple[i]['verified'] == True:
                        description += f"{top} **{tuple[i]['name']}** - {tuple[i]['victor']} **(Verifier)**\n"
                elif top < 26:
                    top = f"**#{top} :fire:**"
                    if tuple[i]['verified'] == False:
                        description += f"{top} **{tuple[i]['name']}** - {tuple[i]['victor']}\n"
                    elif tuple[i]['verified'] == True:
                        description += f"{top} **{tuple[i]['name']}** - {tuple[i]['victor']} **(Verifier)**\n"
                elif top < 76:
                    top = f"**#{top}**"
                    if tuple[i]['verified'] == False:
                        description += f"{top} **{tuple[i]['name']}** - {tuple[i]['victor']}\n"
                    elif tuple[i]['verified'] == True:
                        description += f"{top} **{tuple[i]['name']}** - {tuple[i]['victor']} **(Verifier)**\n"
                elif top < 151:
                    top = f"#{top}"
                    if tuple[i]['verified'] == False:
                        description += f"{top} {tuple[i]['name']} - {tuple[i]['victor']}\n"
                    elif tuple[i]['verified'] == True:
                        description += f"{top} {tuple[i]['name']} - {tuple[i]['victor']} **(Verifier)**\n"
            color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            emb = discord.Embed(title=f"Demons beaten by only 1 person in **{data['data']['nation']['nation']} :flag_{country.lower()}:**",description=description, color=color)
            await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .unique {country}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'got an error: {e}')


@Bot.command()
async def count(ctx, *, value=None):
    try:
        formervalue = value
        value = value.split(',')
        total = 0
        description = ''''''
        for j in value:
            if j[0] == ' ':
                j = j[1:]
            data = None
            url = f'https://pointercrate.com/api/v2/demons?name_contains={j}'
            r = requests.get(url)
            for i in json.loads(r.text):
                if i["name"].lower() == j.lower():
                    data = i
                    break
            text = r.text.replace('[', '')
            text = text.replace(']', '')
            if data == None:
                data = json.loads(text)
            top = int(data["position"])
            score = round(float(score_old(top)), 2)
            total += score
            description += f'**{data["name"]}** - {score} \n'
        color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        emb = discord.Embed(title=f"You will get {round(float(total), 2)} points", description=description, color=color)
        await ctx.send(embed=emb)
        print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .count {formervalue}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'got an error: {e}')


@Bot.command()
async def listed(ctx, number=None):
    try:
        if number == None:
            await ctx.send('You have to use **.listed <placement range>** (for example .listed 1-20)')
        else:
            number = number.split('-')
            url = f"https://pointercrate.com/api/v2/demons/listed?after={int(number[0])-1}&before={int(number[1])+1}"
            r = requests.get(url)
            data = json.loads(r.text)
            description = ''''''
            for i in data:
                top = int(i["position"])
                if top < 4:
                    top = f"**#{top} :hot_face:**"
                elif top < 11:
                    top = f"**#{top} :smiling_imp:**"
                elif top < 26:
                    top = f"**#{top} :fire:**"
                elif top < 76:
                    top = f"**#{top}**"
                elif top < 151:
                    top = f"#{top}"
                else:
                    top = f"*#{top}*"
                description += f'{top} **{i["name"]}** - {i["publisher"]["name"]}, Verifier: **{i["verifier"]["name"]}**, {round(float(score_old(i["position"])), 2)}\n'
            color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            emb = discord.Embed(title=f"Top demons {number[0]}-{number[1]}", description=description, color=color)
            await ctx.send(embed=emb)
            if int(number[1]) - int(number[0]) > 50:
                await ctx.send('you can only request 50 demons with one command')
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .listed {number[0]}-{number[1]}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'got an error: {e}')


@Bot.command()
async def top(ctx, top=None):
    if top == None:
        top = 0
    try:
        url = f'https://pointercrate.com/api/v1/players/ranking/?after={top}'
        r = requests.get(url)
        info = json.loads(r.text)
        players = ''''''
        j = 0
        for i in info:
            j += 1
            if i["nationality"] == None:
                nationality = 'ᅠ'
            else:
                nationality = f':flag_{i["nationality"]["country_code"].lower()}:'
            players += f'{nationality} #{i["rank"]} {i["name"]} - {round(float(i["score"]), 2)}\n'
        color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        emb = discord.Embed(title=f"Top {top}-{int(top)+50}",description=players, color=color)
        await ctx.send(embed=emb)
        print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .top {top}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'Got an error, code error: {e}')


@Bot.command()
async def listr(ctx, percent=None, *, level=None):
    try:
        if level == None or percent == None:
            await ctx.send('You have to use **.listr <percent> <level>**')
        else:
            data = None
            url = f'https://pointercrate.com/api/v2/demons?name_contains={level}'
            r = requests.get(url)
            for i in json.loads(r.text):
                if i["name"].lower() == level.lower():
                    data = i
                    break
            text = r.text.replace('[', '')
            text = text.replace(']', '')
            if data == None:
                data = json.loads(text)
            top = int(data["position"])
            requirement = int(data["requirement"])
            percent = int(percent)
            if top < 76 and percent >= requirement:
                end = round(float(list_progress(top, percent, requirement)), 2)
            else:
                end = 0.00
            color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            emb = discord.Embed(title=f"**{data['name']} - {percent}%**",description=f'You will get {end} points', color=color)
            await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .listr {percent} {level}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'got an error: {e}')


@Bot.command()
async def country(ctx, name=None):
    try:
        if name == None:
            await ctx.send('You have to use **.country <country code>**')
        else:
            urlll = f'https://pointercrate.com/api/v1/players/ranking/?nation={name.upper()}'
            rrr = requests.get(urlll)
            description = ''''''
            j = 0
            nationality = None
            for i in json.loads(rrr.text):
                nationality = i['nationality']['nation']
                j += 1
                if i['nationality']['country_code'].lower() == 'pl':
                    if j == 1:
                        description += f'**#1-1 :flag_pl: empt1ness - 7621.18**\n'
                        continue
                description += f':flag_{i["nationality"]["country_code"].lower()}: #{j}-{i["rank"]} {i["name"]} - {round(float(i["score"]), 2)}\n'
            color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            emb = discord.Embed(title=f"Country: {nationality} :flag_{name.lower()}:",description=description, color=color)
            await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .countryh {country}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'got an error: {e}')


@Bot.command()
async def search(ctx, name=None):
    try:
        if name == None:
            await ctx.send('You have to use **.search <name>**')
        else:
            urlll = f'https://pointercrate.com/api/v1/players/ranking/?name_contains={name}'
            rrr = requests.get(urlll)
            description = ''''''
            for i in json.loads(rrr.text):
                if i["nationality"] != None:
                    description += f':flag_{i["nationality"]["country_code"].lower()}: #{i["rank"]} **{i["name"]}** - {round((i["score"]), 2)}\n'
                else:
                    description += f':flag_white: #{i["rank"]} **{i["name"]}** - {round((i["score"]), 2)}\n'
            color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            emb = discord.Embed(title=f"Searching: *{name}*",description=description, color=color)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .search {name}')
            await ctx.send(embed=emb)
    except Exception as e:
        exceptionn()
        await ctx.send(f'got an error: {e}')


@Bot.command()
async def randomd(ctx, number=None):
    try:
        if number == None:
            await ctx.send('You have to use **.random <placement range>** (for example .random 76-150)')
        else:
            oldnum = number
            number = number.split('-')
            position = random.randint(int(number[0]), int(number[1]))
            position = int(position)
            url = f"https://pointercrate.com/api/v2/demons/listed?after={position - 1}&before={position + 1}"
            r = requests.get(url)
            text = r.text.replace('[', '')
            text = text.replace(']', '')
            data = json.loads(text)
            top = int(data["position"])
            topp = top
            if top < 4:
                top = f"**#{top} :hot_face:**"
            elif top < 11:
                top = f"**#{top} :smiling_imp: **"
            elif top < 26:
                top = f"**#{top} :fire: **"
            elif top < 76:
                top = f"**#{top}**"
            elif top < 151:
                top = f"#{top}"
            else:
                top = f"*#{top}*"
            if data["video"] == None:
                video = "None"
            else:
                video = data["video"]
            description = f'''**{data["name"]}**'''
            color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if data["verifier"]["name"] == data["publisher"]["name"]:
                emb = discord.Embed(title=description,description=f'Verified and published by *{data["verifier"]["name"]}*', color=color)
            else:
                emb = discord.Embed(title=description,description=f'Verified by *{data["verifier"]["name"]}*, published by *{data["publisher"]["name"]}*',color=color)
            emb.add_field(name="List placement:", value=top, inline=True)
            emb.add_field(name="Demonlist score:", value=round(float(score_old(topp)), 2), inline=True)
            emb.add_field(name="List percent:", value=f'{data["requirement"]}%', inline=True)
            try:
                emb.set_image(url=f'https://i.ytimg.com/vi/{data["video"].split("=")[1]}/maxresdefault.jpg')
            except Exception:
                pass
            try:
                view = Buttons()
                view.add_item(discord.ui.Button(label="Verification", style=discord.ButtonStyle.link, url=data["video"],emoji="<:ExtremeDemon:458436386303770636>"))
                await ctx.send(embed=emb, view=view)
            except Exception as e:
                emb = discord.Embed(description=description, color=color)
                await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .randomd {top}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'got an error: {e}')


@Bot.command()
async def beaten(ctx, country=None, *, level=None):
    try:
        if country == None or level == None:
            await ctx.send('You have to use **.beaten <country code> <level name>**')
        else:
            url = f'https://pointercrate.com/api/v1/nationalities/{country}/'
            r = requests.get(url)
            data = json.loads(r.text)
            description = ''''''
            demon = ''
            for i in data['data']['records']:
                if (i['demon'].lower() == level.lower()) and i['progress'] == 100:
                    if i['demon'] == "ErebuS" and level.lower() == "erebus":
                        erebuS = ''''''
                        for j in i['players']:
                            erebuS += f'{j}\n'
                        color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))
                        emb = discord.Embed(title=f"**{data['data']['nation']['nation']} :flag_{country.lower()}: - ErebuS**",description=erebuS, color=color)
                        await ctx.send(embed=emb)
                        continue
                    demon = i['demon']
                    for j in i['players']:
                        description += f'{j}\n'
            for k in data['data']['verified']:
                if (k['demon'].lower() == level.lower()):
                    demon = k['demon']
                    description += f'{k["player"]} **(Verifier)**\n'
            color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if demon != '':
                emb = discord.Embed(title=f"**{data['data']['nation']['nation']} :flag_{country.lower()}: - {demon}**",description=description, color=color)
                await ctx.send(embed=emb)
            else:
                emb = discord.Embed(title=f"**{data['data']['nation']['nation']} :flag_{country.lower()}: - {level}**",description='No victors in this country', color=color)
                await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .beaten {country} {level}')
    except Exception as e:
        await ctx.send(f'got an error: {e}')


@Bot.command()
async def unbeaten(ctx, *, country=None):
    if country == None:
        await ctx.send('You have to use **.unbeaten <country code>**')
    else:
        try:
            url = f'https://pointercrate.com/api/v1/nationalities/{country}/'
            r = requests.get(url)
            data = json.loads(r.text)
            try:
                if data['data']['records'] == []:
                    color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    emb = discord.Embed(title=f"**{data['data']['nation']['nation']} - :flag_{country}:**",description='https://pointercrate.com/demonlist/', color=color)
                    await ctx.send(embed=emb)
            except Exception:
                await ctx.send(data['message'])
            if data['data']['records'] != []:
                list = []
                a = 0
                for i in data['data']['unbeaten']:
                    tuple = {}
                    name = i['name']
                    top = int(i["position"])
                    tuple["name"] = name
                    tuple["top"] = top
                    list.append(tuple)
                    a += 1
                tuple = list
                for i in range(a):
                    def myFunc(e):
                        return e["top"]
                    tuple.sort(key=myFunc)
                description = ''''''
                main = 0
                extended = 0
                mainl = 0
                extendedl = 0
                for i in range(a):
                    top = tuple[i]['top']
                    position = top
                    beaten_score = round(float(score_old(position)), 2)
                    if top < 4:
                        description += f'**{tuple[i]["name"]} - #{top} - `{beaten_score}` :hot_face: **\n'
                        main += 1
                        mainl += beaten_score
                    elif top < 11:
                        description += f'**{tuple[i]["name"]} - #{top} - `{beaten_score}` :smiling_imp: **\n'
                        main += 1
                        mainl += beaten_score
                    elif top < 26:
                        description += f'**{tuple[i]["name"]} - #{top} - `{beaten_score}` :fire: **\n'
                        main += 1
                        mainl += beaten_score
                    elif top < 76:
                        description += f'**{tuple[i]["name"]} - #{top} - `{beaten_score}`**\n'
                        main += 1
                        mainl += beaten_score
                    elif top < 151:
                        description += f'{tuple[i]["name"]} - #{top} - `{beaten_score}`\n'
                        extended += 1
                        extendedl += beaten_score
                mainl = round(float(mainl), 2)
                extendedl = round(float(extendedl), 2)
                description += f'\n**Unbeaten Main List: {main} - `{mainl}`**\n'
                description += f'**Unbeaten Extended List: {extended} - `{extendedl}`**\n'
                color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                if len(description) > 4096:
                    emb = discord.Embed(title=f"**{data['data']['nation']['nation']} - :flag_{country.lower()}:**",description=f"""This will literally kill the bot\n \n**Unbeaten Main List: {main} - `{mainl}`**\n**Unbeaten Extended List: {extended} - `{extendedl}`**\n""", color=color)
                    await ctx.send(embed=emb)
                    return
                emb = discord.Embed(title=f"**{data['data']['nation']['nation']} - :flag_{country.lower()}:**",description=description, color=color)
                await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .unbeaten {country}')
        except Exception as e:
            await ctx.send(e)


@Bot.command()
async def records(ctx, *, name=None):
    try:
        if None == None:
            list = ["bloodbath", "cataclysm", "cataclysm"]
            if name == None:
                await ctx.send('You have to use .records <demon name>')
            elif name.lower() in list:
                recordss = f''':flag_ru: lyt1x - **104%**
        :transgender_flag: sailisy - **15%**'''
                color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                emb = discord.Embed(description=recordss, color=color)
                await ctx.send(embed=emb)
            else:
                data = None
                url = f'https://pointercrate.com/api/v2/demons?name_contains={name}'
                r = requests.get(url)
                for i in json.loads(r.text):
                    if i["name"].lower() == name.lower():
                        data = i
                        break
                text = r.text.replace('[', '')
                text = text.replace(']', '')
                if data == None:
                    data = json.loads(text)
                id = data["id"]
                urll = f'https://pointercrate.com/api/v2/demons/{id}'
                rr = requests.get(urll)
                data = json.loads(rr.text)
                recordss = ''''''
                victors = ''''''
                breakk = 0
                j = 0
                completions = 0
                for i in data["data"]["records"]:
                    j += 1
                    if j % 100 == 0:
                        if j > 75:
                            breakk = 1
                    if i["nationality"] == None:
                        nationality = ''
                    else:
                        nationality = f':flag_{i["nationality"]["country_code"].lower()}:'
                    if i["progress"] < 100:
                        recordss += f'{nationality} {i["player"]["name"]} - {i["progress"]}%\n'
                    else:
                        completions += 1
                        recordss += f'{nationality} {i["player"]["name"]} - **{i["progress"]}%**\n'
                if breakk == 0:
                    color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    emb = discord.Embed(title=f"**{data['data']['name']}, #{data['data']['position']}**",description=f"**{j} records registered,\nout of which {completions} are 100%**\n\n{recordss}", color=color)
                    await ctx.send(embed=emb)
                    print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .records {name}')
                else:
                    color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))
                    emb = discord.Embed(title=f"**{data['data']['name']}, #{data['data']['position']}**",description=f"**{j} records registered,\nout of which {completions} are 100%**\n\n Too much records :(",color=color)
                    await ctx.send(embed=emb)
                    print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .records {name}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'there is either too much records or you just sent a wrong demon name, code error: **{e}**')


@Bot.command()
async def demon(ctx, *, name=None):
    try:
        if name == None:
            await ctx.send('you have to use .demon <demon name>')
        else:
            data = None
            url = f'https://pointercrate.com/api/v2/demons?name_contains={name}'
            r = requests.get(url)
            descriptionn = ''''''
            for i in json.loads(r.text):
                if i["name"].lower() == name.lower():
                    data = i
                    break
                else:
                    top = int(i["position"])
                    if top < 4:
                        top = f"**#{top} :hot_face:**"
                    elif top < 11:
                        top = f"**#{top} :smiling_imp:**"
                    elif top < 26:
                        top = f"**#{top} :fire:**"
                    elif top < 76:
                        top = f"**#{top}**"
                    elif top < 151:
                        top = f"#{top}"
                    else:
                        top = f"*#{top}*"
                    descriptionn += f'{top} **{i["name"]}** - {i["publisher"]["name"]}, Verifier: **{i["verifier"]["name"]}**, {round(float(score_old(i["position"])), 2)}\n'
            descriptionn += '**\n Choose one and send ".demon <selected demon>"**'
            text = r.text.replace('[', '')
            text = text.replace(']', '')
            if data == None:
                try:
                    data = json.loads(text)
                except Exception as g:
                    color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))
                    emb = discord.Embed(title=f"Searching *{name}*",description=descriptionn, color=color)
                    await ctx.send(embed=emb)
                    return
            top = int(data["position"])
            topp = top
            if top < 4:
                top = f"**#{top} :hot_face:**"
            elif top < 11:
                top = f"**#{top} :smiling_imp: **"
            elif top < 26:
                top = f"**#{top} :fire: **"
            elif top < 76:
                top = f"**#{top}**"
            elif top < 151:
                top = f"#{top}"
            else:
                top = f"*#{top}*"
            if data["video"] == None:
                video = "None"
            else:
                video = data["video"]
            description = f'''**{data["name"]}**'''
            color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if data["verifier"]["name"] == data["publisher"]["name"]:
                emb = discord.Embed(title=description,description=f'Verified and published by *{data["verifier"]["name"]}*',color=color)
            else:
                emb = discord.Embed(title=description, description=f'Verified by *{data["verifier"]["name"]}*, published by *{data["publisher"]["name"]}*', color=color)
            emb.add_field(name="List placement:", value=top, inline=True)
            emb.add_field(name="Demonlist score:", value=round(float(score_old(topp)), 2), inline=True)
            emb.add_field(name="List percent:", value=f'{data["requirement"]}%', inline=True)
            try:
                emb.set_image(url=f'https://i.ytimg.com/vi/{data["video"].split("=")[1]}/maxresdefault.jpg')
            except Exception:
                pass
            if video != "None":
                view = Buttons()
                view.add_item(discord.ui.Button(label="Verification", style=discord.ButtonStyle.link, url=data["video"],emoji="<:ExtremeDemon:458436386303770636>"))
                await ctx.send(embed=emb,view=view)
            else:
                await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .demon {name}')
    except Exception as ex:
        exceptionn()
        await ctx.send(f'Got an error: {ex}')


@Bot.command()
async def position(ctx, position=None):
    try:
        if position == None:
            await ctx.send('No position sent, use .position <demon position>')
        else:
            position = int(position)
            url = f"https://pointercrate.com/api/v2/demons/listed?after={position - 1}&before={position + 1}"
            r = requests.get(url)
            text = r.text.replace('[', '')
            text = text.replace(']', '')
            data = json.loads(text)
            top = int(data["position"])
            topp = top
            if top < 4:
                top = f"**#{top} :hot_face:**"
            elif top < 11:
                top = f"**#{top} :smiling_imp: **"
            elif top < 26:
                top = f"**#{top} :fire: **"
            elif top < 76:
                top = f"**#{top}**"
            elif top < 151:
                top = f"#{top}"
            else:
                top = f"*#{top}*"
            if data["video"] == None:
                video = "None"
            else:
                video = data["video"]
            description = f'''**{data["name"]}**'''
            color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if data["verifier"]["name"] == data["publisher"]["name"]:
                emb = discord.Embed(title=description,description=f'Verified and published by *{data["verifier"]["name"]}*', color=color)
            else:
                emb = discord.Embed(title=description,description=f'Verified by *{data["verifier"]["name"]}*, published by *{data["publisher"]["name"]}*',color=color)
            emb.add_field(name="List placement:", value=top, inline=True)
            emb.add_field(name="Demonlist score:", value=round(float(score_old(topp)), 2), inline=True)
            emb.add_field(name="List percent:", value=f'{data["requirement"]}%', inline=True)
            try:
                emb.set_image(url=f'https://i.ytimg.com/vi/{data["video"].split("=")[1]}/maxresdefault.jpg')
            except Exception:
                pass
            try:
                view = Buttons()
                view.add_item(discord.ui.Button(label="Verification", style=discord.ButtonStyle.link, url=data["video"],emoji="<:ExtremeDemon:458436386303770636>"))
                await ctx.send(embed=emb, view=view)
            except Exception as e:
                emb = discord.Embed(description=description, color=color)
                await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .position {top}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'Got an error, code error: {e}')


@Bot.command()
async def toph(ctx, top=None):
    if top == None:
        top = 0
    try:
        url = f'https://pointercrate.com/api/v1/players/ranking/?after={top}'
        r = requests.get(url)
        info = json.loads(r.text)
        players = ''''''
        j = 0
        for i in info:
            j += 1
            urll = f'https://pointercrate.com/api/v1/players/{i["id"]}'
            rr = requests.get(urll)
            hardestnumber = 100000
            hardestid = 0
            for k in json.loads(rr.text)["data"]["records"]:
                if k["progress"] != 100:
                    continue
                if k["demon"]["position"] < hardestnumber:
                    hardestnumber = int(k["demon"]["position"])
                    hardestid = int(k["demon"]["id"])
            for l in json.loads(rr.text)["data"]["verified"]:
                if l["position"] < hardestnumber:
                    hardestnumber = int(l["position"])
                    hardestid = int(l["id"])
            if j % 7 == 0:
                await ctx.send(f'Checking number {j}, {i["name"]}')
            if hardestid != 0:
                hardest = f'https://pointercrate.com/api/v2/demons/{hardestid}'
                harddest = requests.get(hardest)
                htext = json.loads(harddest.text)
                hardest = f'{htext["data"]["name"]} - #{htext["data"]["position"]}'
            else:
                hardest = 'None'
            if i["nationality"] == None:
                nationality = 'ᅠ'
            else:
                nationality = f':flag_{i["nationality"]["country_code"].lower()}:'
            players += f'{nationality} #{i["rank"]} {i["name"]} - {round(float(i["score"]), 2)}, **{hardest}**\n'
        emb = discord.Embed(description=players, color=0x674ea7)
        await ctx.send(embed=emb)
        print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .toph {top}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'Got an error, code error: {e}')


@Bot.command()
async def link(ctx, memberr, *, arg=None):
    if ctx.author.id != 378602408424767498:
        return
    memberr = memberr.replace('<', '')
    memberr = memberr.replace('>', '')
    memberr = memberr.replace('@', '')
    memberr = memberr.replace('!', '')
    guild = Bot.get_guild(ctx.author.guild.id)
    memberr = guild.get_member(int(memberr))
    with open('profiles.json', 'r') as f:
        data = json.load(f)
    urlll = f'https://pointercrate.com/api/v1/players/ranking/?name_contains={arg}'
    rrr = requests.get(urlll)
    for i in data:
        test = data[i]['pointercrate']
        if str(test) == str(json.loads(rrr.text)[0]["id"]) and str(memberr.id) != i:
            user = Bot.get_user(int(i))
            await ctx.send(f'This pointercrate account is already linked to **{user}**')
            return
    try:
        data[str(memberr.id)]["pointercrate"] = json.loads(rrr.text)[0]["id"]
    except Exception as e:
        await ctx.send('use .profile to create your profile first')
        return
    with open('profiles.json', 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
    await ctx.send('I updated it, please use .profile')
@Bot.command()
async def edit(ctx, argument=None, *, arg=None):
    try:
        if arg == None:
            await ctx.send('Example: .edit youtube_channel <link> or .edit pointercrate <name> or .edit text <text>')
        if argument == None:
            await ctx.send('Example: .edit youtube_channel <link> or .edit pointercrate <name> or .edit text <text>')
        elif argument == "youtube_channel":
            if "https://youtube.com" not in arg and "https://www.youtube.com" not in arg:
                await ctx.send('Use a youtube link, please')
                return
            with open('profiles.json', 'r') as f:
                data = json.load(f)
            data[str(ctx.author.id)]["youtube_channel"] = arg
            with open('profiles.json', 'w') as f:
                json.dump(data, f, indent=4, sort_keys=True)
            await ctx.send('Updated it')
        elif argument == "pointercrate":
            with open('profiles.json', 'r') as f:
                data = json.load(f)
            urlll = f'https://pointercrate.com/api/v1/players/ranking/?name_contains={arg}'
            rrr = requests.get(urlll)
            for i in data:
                test = data[i]['pointercrate']
                if str(test) == str(json.loads(rrr.text)[0]["id"]) and str(ctx.author.id) != i:
                    user = Bot.get_user(int(i))
                    await ctx.send(f'This pointercrate account is already linked to **{user}**')
                    return
            try:
                data[str(ctx.author.id)]["pointercrate"] = json.loads(rrr.text)[0]["id"]
            except Exception as e:
                await ctx.send('use .profile to create your profile first')
                return
            try:
                if int(json.loads(rrr.text)[0]["rank"]) < 200:
                    await ctx.send('You are to good for this game so in order to get your account linked dm the owner')
                    return
            except Exception:
                pass
            with open('profiles.json', 'w') as f:
                json.dump(data, f, indent=4, sort_keys=True)
            await ctx.send('I updated it, please use .profile')
        elif argument == "text":
            with open('profiles.json', 'r') as f:
                dataa = json.load(f)
            with open('premium.json', 'r') as f:
                data = json.load(f)
            try:
                argg = dataa[str(ctx.author.id)]["pointercrate"]
                argg = str(argg).lower()
            except Exception as g:
                await ctx.send('you need to link your pointercrate account (or type .profile to get create your profile)')
            if len(arg) > 40:
                await ctx.send('your text has to be <40 symbols')
                if admincheck(ctx.author.id) == True:
                    await ctx.send('...but you have **special access** so... fine')
                else:
                    return
            if argg == "none":
                await ctx.send('you didnt link your pointercrate account')
                return
            data[argg] = arg
            with open('premium.json', 'w') as f:
                json.dump(data, f, indent=4, sort_keys=True)
            await ctx.send('I updated it, please use .player <name>')
        else:
            await ctx.send('Example: .edit youtube_channel <link> or .edit pointercrate <name> or .edit text <text>')
        print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .edit {argument} {arg}')
    except Exception as e:
        exceptionn()
        await ctx.send(f'I have no idea what went wrong, here is the code error: {e}')


@Bot.command()
async def profile(ctx, member=None):
    try:
        memberr = member
        if memberr == None:
            memberr = ctx.author
        else:
            memberr = memberr.replace('<', '')
            memberr = memberr.replace('>', '')
            memberr = memberr.replace('@', '')
            memberr = memberr.replace('!', '')
            guild = Bot.get_guild(ctx.author.guild.id)
            memberr = guild.get_member(int(memberr))
        with open('profiles.json', 'r') as f:
            data = json.load(f)
        if str(memberr.id) not in data:
            data[str(memberr.id)] = {"youtube_channel": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                                     "pointercrate": None}
            with open('profiles.json', 'w') as f:
                json.dump(data, f, indent=4, sort_keys=True)
            with open('profiles.json', 'r') as f:
                data = json.load(f)
        embed = discord.Embed(color=0xFF0000, title=f"{memberr}'s profile", description='''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
        view = Buttons()
        view.add_item(discord.ui.Button(label="Youtube", style=discord.ButtonStyle.link, url=data[str(memberr.id)]["youtube_channel"],emoji="<:ruow_Youtube:436266477016842250>"))
        #print(requests.get(f'https://pointercrate.com/api/v1/players/{data[str(memberr.id)]["pointercrate"]}').text)
        try:
            embed.add_field(name="Pointercrate:", value=json.loads(requests.get(f'https://pointercrate.com/api/v1/players/{data[str(memberr.id)]["pointercrate"]}').text)["data"]["name"], inline=True)
        except Exception:
            embed.add_field(name="Pointercrate:", value="None", inline=True)
        embed.add_field(name="YouTube:", value=f"[Click]({data[str(memberr.id)]['youtube_channel']})", inline=True)
        await ctx.send(embed=embed, view=view)
        print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .profile {member}')
    except Exception as e:
        await ctx.send(f'Something went wrong, and here is what did: {e}')


@Bot.command()
async def countryh(ctx, *, country=None):
    if country == None:
        await ctx.send('You have to use **.countryh <country code>**')
    else:
        try:
            url = f'https://pointercrate.com/api/v1/players/ranking/?nation={country.upper()}'
            r = requests.get(url)
            players = json.loads(r.text)
            playerss = ''''''
            j = 0
            for i in players:
                j += 1
                urll = f'https://pointercrate.com/api/v1/players/{i["id"]}'
                rr = requests.get(urll)
                hardestnumber = 100000
                hardestid = 0
                for k in json.loads(rr.text)["data"]["records"]:
                    if k["progress"] != 100:
                        continue
                    if k["demon"]["position"] < hardestnumber:
                        hardestnumber = int(k["demon"]["position"])
                        hardestid = int(k["demon"]["id"])
                for l in json.loads(rr.text)["data"]["verified"]:
                    if l["position"] < hardestnumber:
                        hardestnumber = int(l["position"])
                        hardestid = int(l["id"])
                if j % 7 == 0:
                    await ctx.send(f'Checking number {j}, {i["name"]}')
                if hardestid != 0:
                    hardest = f'https://pointercrate.com/api/v2/demons/{hardestid}'
                    harddest = requests.get(hardest)
                    htext = json.loads(harddest.text)
                    hardest = f'{htext["data"]["name"]} - #{htext["data"]["position"]}'
                else:
                    hardest = 'None'
                playerss += f':flag_{i["nationality"]["country_code"].lower()}: #{j}-{i["rank"]} {i["name"]} - {round(float(i["score"]), 2)}, **{hardest}**\n'
            emb = discord.Embed(description=playerss, color=0xcdff00)
            await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .countryh {country}')
        except Exception as e:
            await ctx.send(
                f'Got an error, probably you sent a wrong country code (or nobody lives in that country), an example of a country code: RU (you can use lower letters), error code: {e}')


# @Bot.command()
# async def progress(ctx, level=None, progress=None):
# if (level == None) or (progress == None):
# await ctx.send("You have to use **.progress <level name> <your progress>")
# else:


@Bot.command()
async def difference(ctx, *, name=None):
    try:
        if name == None:
            await ctx.send('you have to use **.difference <demon name>**')
        else:
            data = None
            url = f'https://pointercrate.com/api/v2/demons?name_contains={name}'
            r = requests.get(url)
            for i in json.loads(r.text):
                if i["name"].lower() == name.lower():
                    data = i
                    break
            text = r.text.replace('[', '')
            text = text.replace(']', '')
            if data == None:
                data = json.loads(text)
            position = int(data["position"])

            def score_old(position):
                if (125 < position) & (position <= 150):
                    return 150 * exp((1 - position) * log(1 / 30) / (-149))
                elif (50 < position) & (position <= 125):
                    return 60 * (2.333 ** ((51 - position) * (log(30) / 99))) + 1.884
                elif (20 < position) & (position <= 50):
                    return -100 * (1.01327 ** (position - 26.489)) + 200
                elif (0 < position) & (position <= 20):
                    return 149.61 * (1.168 ** (1 - position)) + 100.39
                else:
                    return 0

            def score_new(position):
                if (55 < position) & (position <= 150):
                    return 6.447 + 60 * (2 ** ((46.8 - position) * log(50) / 99))
                elif (50 < position) & (position <= 55):
                    return -100 * (1.01327 ** (position - 26.489)) + 200
                else:
                    return score_old(position)

            description = f"""Очков дают сейчас: {round(float(score_old(position)), 2)}
Очков будут давать после апдейта: {round(float(score_new(position)), 2)}
"""
            # print(f"Очков будут давать после апдейта: {round(float(score_new(position)), 2)}")
            # print(f"Очков дают сейчас: {round(float(score_old(position)), 2)}")
            color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            emb = discord.Embed(description=description, color=color)
            await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .difference {name}')
    except Exception as e:
        await ctx.send(f'Got an error, code error: {e}')


@Bot.command()
async def hardest(ctx, *, playerr=None):
    if playerr == None:
        await ctx.send('You have to use **.hardest <player name>**')
    else:
        try:
            url = f'https://pointercrate.com/api/v1/players?name={playerr}'
            r = requests.get(url)
            if r.text == "[]":
                await ctx.send(f"No one has the name **{playerr}** in pointercrate")
            else:
                text = r.text[1:-1]
                text = json.loads(text)
                playerr = text["name"]
                id = text["id"]
                urll = f'https://pointercrate.com/api/v1/players/{id}'
                rr = requests.get(urll)
                test = json.loads(rr.text)
                if test["data"]["nationality"] == None:
                    nationality = 'None'
                else:
                    nationality = f':flag_{test["data"]["nationality"]["country_code"].lower()}:'
                ban = ''
                if test["data"]["banned"] == True:
                    ban = """**:warning: This account is banned on pointercrate** 
*(that means you can only see their verified demons)*\n"""
                urlll = f'https://pointercrate.com/api/v1/players/ranking/?name_contains={playerr}'
                rrr = requests.get(urlll)
                rank = 'None'
                score = 0
                for i in json.loads(rrr.text):
                    if i["name"] == playerr:
                        rank = i["rank"]
                        score = i["score"]
                        break
                list = []
                a = 0
                for i in test['data']['records']:
                    if int(i["progress"]) != 100:
                        continue
                    tuple = {'demon':{}}
                    name = i['demon']['name']
                    top = int(i["demon"]["position"])
                    progress = int(i["progress"])
                    tuple["demon"]["id"] = i["demon"]["id"]
                    tuple["demon"]["name"] = name
                    tuple["demon"]["position"] = top
                    tuple["progress"] = progress
                    tuple["verification"] = False
                    list.append(tuple)
                    a += 1
                for i in test['data']['verified']:
                    tuple = {'demon':{}}
                    name = i['name']
                    top = int(i["position"])
                    tuple["demon"]["id"] = i["id"]
                    tuple["demon"]["name"] = name
                    tuple["demon"]["position"] = top
                    tuple["progress"] = 100
                    tuple["verification"] = True
                    list.append(tuple)
                    a += 1
                tuple = list
                for i in range(a):
                    def myFunc(e):
                        return e["demon"]["position"]
                    tuple.sort(key=myFunc)
                completed = ''''''
                progresses = ''''''
                verified = ''''''
                hardestnumber = 100000
                hardestid = 0
                main = 0
                extended = 0
                legacy = 0
                if a < 10:
                    a = a
                else:
                    a = 10
                for j in range(a):
                    i = tuple[j]
                    if i["demon"]["position"] < hardestnumber:
                        hardestnumber = int(i["demon"]["position"])
                        hardestid = int(i["demon"]["id"])
                    if i["demon"]["position"] < 4:
                        main += 1
                        if i["verification"] == True:
                            completed += f'{j+1}) **{i["demon"]["name"]} - #{i["demon"]["position"]} :hot_face: ** (Verification)\n'
                        else:
                            completed += f'{j + 1}) **{i["demon"]["name"]} - #{i["demon"]["position"]} :hot_face: **\n'
                    elif i["demon"]["position"] < 11:
                        main += 1
                        if i["verification"] == True:
                            completed += f'{j+1}) **{i["demon"]["name"]} - #{i["demon"]["position"]} :smiling_imp: ** (Verification)\n'
                        else:
                            completed += f'{j + 1}) **{i["demon"]["name"]} - #{i["demon"]["position"]} :smiling_imp: **\n'
                    elif i["demon"]["position"] < 26:
                        main += 1
                        if i["verification"] == True:
                            completed += f'{j + 1}) **{i["demon"]["name"]} - #{i["demon"]["position"]} :fire: ** (Verification)\n'
                        else:
                            completed += f'{j + 1}) **{i["demon"]["name"]} - #{i["demon"]["position"]} :fire: **\n'
                    elif i["demon"]["position"] < 76:
                        main += 1
                        if i['verification'] == True:
                            completed += f'{j+1}) **{i["demon"]["name"]} - #{i["demon"]["position"]}** (Verification)\n'
                        else:
                            completed += f'{j + 1}) **{i["demon"]["name"]} - #{i["demon"]["position"]}**\n'
                    elif i["demon"]["position"] < 151:
                        extended += 1
                        if i['verification'] == True:
                            completed += f'{j+1}) {i["demon"]["name"]} - #{i["demon"]["position"]} (Verification)\n'
                        else:
                            completed += f'{j+1}) {i["demon"]["name"]} - #{i["demon"]["position"]}\n'
                    else:
                        legacy += 1
                        if i['verification'] == True:
                            completed += f'{j+1}) *{i["demon"]["name"]} - #{i["demon"]["position"]}* (Verification)\n'
                        else:
                            completed += f'{j + 1}) *{i["demon"]["name"]} - #{i["demon"]["position"]}*\n'
                if completed == '':
                    completed = 'None\n'
                if verified == '':
                    verified = 'None\n'
                if progresses == '':
                    progresses = 'None\n'
                if hardestid != 0:
                    hardest = f'https://pointercrate.com/api/v2/demons/{hardestid}'
                    harddest = requests.get(hardest)
                    htext = json.loads(harddest.text)
                    if htext["data"]["position"] < 4:
                        hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]} :hot_face: **'
                    elif htext["data"]["position"] < 11:
                        hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]} :smiling_imp: **'
                    elif htext["data"]["position"] < 26:
                        hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]} :fire: **'
                    elif htext["data"]["position"] < 76:
                        hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]}**'
                    elif htext["data"]["position"] < 151:
                        hardest = f'{htext["data"]["name"]} - #{htext["data"]["position"]}'
                    else:
                        hardest = f'*{htext["data"]["name"]} - #{htext["data"]["position"]}*'
                else:
                    hardest = 'None'
                dataa = f'''{ban}
Name: {playerr}
Country: {nationality}
Demonlist rank: {rank}
Demonlist score: {round(float(score), 2)}

`Top 10 Hardest Demons`: 
{completed}
**Hardest demon**:
{hardest}{premiumcheck(playerr.lower())}'''
                emb = discord.Embed(description=dataa, color=0x73ffdb)
                await ctx.send(embed=emb)
                print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .hardest {playerr}')
        except Exception as e:
            exceptionn()
            await ctx.send(
                f'I got an error, I think you just sent a wrong nickname **(or this guy has too much completed demons (Luqualizer for example))**, error code: {e}'
            )


@Bot.command()
async def playerh(ctx, *, playerr=None):
    if playerr == None:
        await ctx.send('You have to use **.playerh <player name>**')
    else:
        try:
            url = f'https://pointercrate.com/api/v1/players?name={playerr}'
            r = requests.get(url)
            if r.text == "[]":
                await ctx.send(f"No one has the name **{playerr}** in pointercrate")
            else:
                text = r.text[1:-1]
                text = json.loads(text)
                playerr = text["name"]
                id = text["id"]
                urll = f'https://pointercrate.com/api/v1/players/{id}'
                rr = requests.get(urll)
                test = json.loads(rr.text)
                if test["data"]["nationality"] == None:
                    nationality = 'None'
                else:
                    nationality = f':flag_{test["data"]["nationality"]["country_code"].lower()}:'
                ban = ''
                if test["data"]["banned"] == True:
                    ban = """**:warning: This account is banned on pointercrate** 
*(that means you can only see their verified demons)*\n"""
                urlll = f'https://pointercrate.com/api/v1/players/ranking/?name_contains={playerr}'
                rrr = requests.get(urlll)
                rank = 'None'
                score = 0
                for i in json.loads(rrr.text):
                    if i["name"] == playerr:
                        rank = i["rank"]
                        score = i["score"]
                        break
                list = []
                a = 0
                for i in test['data']['records']:
                    tuple = {'demon':{}}
                    name = i['demon']['name']
                    top = int(i["demon"]["position"])
                    progress = int(i["progress"])
                    tuple["demon"]["id"] = i["demon"]["id"]
                    tuple["demon"]["name"] = name
                    tuple["demon"]["position"] = top
                    tuple["progress"] = progress
                    list.append(tuple)
                    a += 1
                tuple = list
                for i in range(a):
                    def myFunc(e):
                        return e["demon"]["position"]
                    tuple.sort(key=myFunc)
                completed = ''''''
                progresses = ''''''
                verified = ''''''
                hardestnumber = 100000
                hardestid = 0
                main = 0
                extended = 0
                legacy = 0
                for j in range(a):
                    i = tuple[j]
                    if i["progress"] != 100:
                        if i["demon"]["position"] < 4:
                            progresses += f'**{i["demon"]["name"]} ({i["progress"]}%) - #{i["demon"]["position"]} :hot_face: **\n'
                        elif i["demon"]["position"] < 11:
                            progresses += f'**{i["demon"]["name"]} ({i["progress"]}%) - #{i["demon"]["position"]} :smiling_imp: **\n'
                        elif i["demon"]["position"] < 26:
                            progresses += f'**{i["demon"]["name"]} ({i["progress"]}%) - #{i["demon"]["position"]} :fire: **\n'
                        elif i["demon"]["position"] < 76:
                            progresses += f'**{i["demon"]["name"]} ({i["progress"]}%) - #{i["demon"]["position"]}**\n'
                        elif i["demon"]["position"] < 151:
                            progresses += f'{i["demon"]["name"]} ({i["progress"]}%) - #{i["demon"]["position"]}\n'
                        else:
                            progresses += f'*{i["demon"]["name"]} ({i["progress"]}%) - #{i["demon"]["position"]}*\n'
                    else:
                        if i["demon"]["position"] < hardestnumber:
                            hardestnumber = int(i["demon"]["position"])
                            hardestid = int(i["demon"]["id"])
                        if i["demon"]["position"] < 4:
                            main += 1
                            completed += f'**{i["demon"]["name"]} - #{i["demon"]["position"]} :hot_face: **\n'
                        elif i["demon"]["position"] < 11:
                            main += 1
                            completed += f'**{i["demon"]["name"]} - #{i["demon"]["position"]} :smiling_imp: **\n'
                        elif i["demon"]["position"] < 26:
                            main += 1
                            completed += f'**{i["demon"]["name"]} - #{i["demon"]["position"]} :fire: **\n'
                        elif i["demon"]["position"] < 76:
                            main += 1
                            completed += f'**{i["demon"]["name"]} - #{i["demon"]["position"]}**\n'
                        elif i["demon"]["position"] < 151:
                            extended += 1
                            completed += f'{i["demon"]["name"]} - #{i["demon"]["position"]}\n'
                        else:
                            legacy += 1
                            completed += f'*{i["demon"]["name"]} - #{i["demon"]["position"]}*\n'
                for i in test["data"]["verified"]:
                    if i["position"] < hardestnumber:
                        hardestnumber = int(i["position"])
                        hardestid = int(i["id"])
                    if i["position"] < 4:
                        main += 1
                        verified += f'**{i["name"]} - #{i["position"]} :hot_face: **\n'
                    elif i["position"] < 11:
                        main += 1
                        verified += f'**{i["name"]} - #{i["position"]} :smiling_imp: **\n'
                    elif i["position"] < 26:
                        main += 1
                        verified += f'**{i["name"]} - #{i["position"]} :fire: **\n'
                    elif i["position"] < 76:
                        main += 1
                        verified += f'**{i["name"]} - #{i["position"]}**\n'
                    elif i["position"] < 151:
                        extended += 1
                        verified += f'{i["name"]} - #{i["position"]}\n'
                    else:
                        legacy += 1
                        verified += f'*{i["name"]} - #{i["position"]}*\n'
                if completed == '':
                    completed = 'None\n'
                if verified == '':
                    verified = 'None\n'
                if progresses == '':
                    progresses = 'None\n'
                if hardestid != 0:
                    hardest = f'https://pointercrate.com/api/v2/demons/{hardestid}'
                    harddest = requests.get(hardest)
                    htext = json.loads(harddest.text)
                    if htext["data"]["position"] < 4:
                        hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]} :hot_face: **\n'
                    elif htext["data"]["position"] < 11:
                        hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]} :smiling_imp: **\n'
                    elif htext["data"]["position"] < 26:
                        hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]} :fire: **\n'
                    elif htext["data"]["position"] < 76:
                        hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]}**\n'
                    elif htext["data"]["position"] < 151:
                        hardest = f'{htext["data"]["name"]} - #{htext["data"]["position"]}\n'
                    else:
                        hardest = f'*{htext["data"]["name"]} - #{htext["data"]["position"]}*\n'
                else:
                    hardest = 'None'
                dohua = False
                overdohua = False
                completedd = completed.split('\n')
                if len(completedd) > 10:
                    dohua = True
                if len(completedd) > 100:
                    overdohua = True
                if dohua == True:
                    pass
                if premiumcheck(playerr.lower()) != "":
                    emb = discord.Embed(title=f"{nationality} {playerr}",
                                        description=f"```{premiumcheck(playerr.lower())}```   ", color=0x73ffdb)
                else:
                    emb = discord.Embed(title=f"{nationality} {playerr}", color=0x73ffdb)
                emb.add_field(name=f"Rank: ", value=rank, inline=True)
                emb.add_field(name=f"Score: ", value=round(float(score), 2), inline=True)
                emb.add_field(name=f"Hardest Demon: ", value=hardest, inline=True)
                emb.add_field(name=f"Stats: ", value=f"{main} Main, {extended} Extended, {legacy} Legacy", inline=False)
                a = 3
                if overdohua == True:
                    a = 6
                for i in range(a):
                    if dohua == False:
                        break
                    complete1 = ''''''
                    if a == 6:
                        rangee = [0, len(completedd) // a, len(completedd) // a * 2, len(completedd) // a * 3,
                                  len(completedd) // a * 4, len(completedd) // a * 5, len(completedd)]
                    else:
                        rangee = [0, len(completedd) // a, len(completedd) // a * 2, len(completedd)]
                    for index in range(rangee[i], rangee[i + 1]):
                        complete1 += completedd[index] + "\n"
                    if i == 0:
                        emb.add_field(name=f"Demons Completed: ", value=complete1, inline=True)
                    else:
                        emb.add_field(name=f"⠀", value=complete1, inline=True)
                    # emb.add_field(name="", value=verified, inline=True)
                    # emb.add_field(name="", value=verified, inline=True)
                if dohua == False:
                    emb.add_field(name=f"Demons Completed: ", value=completed, inline=True)
                emb.add_field(name="Demons verified:", value=verified, inline=True)
                emb.add_field(name="Progress on:", value=progresses, inline=True)
                emb.set_footer(text=f"Player ID: {id}")
                await ctx.send(embed=emb)
                print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .playerh {playerr}')
        except Exception as e:
            exceptionn()
            await ctx.send(
                f'I got an error, I think you just sent a wrong nickname **(or this guy has too much completed demons (Luqualizer for example))**, error code: {e}'
            )


@Bot.command()
async def player(ctx, *, playerr=None):
    if playerr == None:
        await ctx.send('You have to use **.player <player name>**')
    else:
        try:
            url = f'https://pointercrate.com/api/v1/players?name={playerr}'
            r = requests.get(url)
            if r.text == "[]":
                await ctx.send(f"No one has the name **{playerr}** in pointercrate")
            else:
                text = r.text[1:-1]
                text = json.loads(text)
                playerr = text["name"]
                id = text["id"]
                urll = f'https://pointercrate.com/api/v1/players/{id}'
                rr = requests.get(urll)
                test = json.loads(rr.text)
                if test["data"]["nationality"] == None:
                    nationality = 'None'
                else:
                    nationality = f':flag_{test["data"]["nationality"]["country_code"].lower()}:'
                ban = ''
                if test["data"]["banned"] == True:
                    ban = """**:warning: This account is banned on pointercrate** 
*(that means you can only see their verified demons)*\n"""
                urlll = f'https://pointercrate.com/api/v1/players/ranking/?name_contains={playerr}'
                rrr = requests.get(urlll)
                rank = 'None'
                score = 0
                for i in json.loads(rrr.text):
                    if i["name"] == playerr:
                        rank = i["rank"]
                        score = i["score"]
                        break
                completed = ''''''
                progresses = ''''''
                verified = ''''''
                hardestnumber = 100000
                hardestid = 0
                main = 0
                extended = 0
                legacy = 0
                for i in test["data"]["records"]:
                    if i["progress"] != 100:
                        if i["demon"]["position"] < 4:
                            progresses += f'**{i["demon"]["name"]} ({i["progress"]}%) - #{i["demon"]["position"]} :hot_face: **\n'
                        elif i["demon"]["position"] < 11:
                            progresses += f'**{i["demon"]["name"]} ({i["progress"]}%) - #{i["demon"]["position"]} :smiling_imp: **\n'
                        elif i["demon"]["position"] < 26:
                            progresses += f'**{i["demon"]["name"]} ({i["progress"]}%) - #{i["demon"]["position"]} :fire: **\n'
                        elif i["demon"]["position"] < 76:
                            progresses += f'**{i["demon"]["name"]} ({i["progress"]}%) - #{i["demon"]["position"]}**\n'
                        elif i["demon"]["position"] < 151:
                            progresses += f'{i["demon"]["name"]} ({i["progress"]}%) - #{i["demon"]["position"]}\n'
                        else:
                            progresses += f'*{i["demon"]["name"]} ({i["progress"]}%) - #{i["demon"]["position"]}*\n'
                    else:
                        if i["demon"]["position"] < hardestnumber:
                            hardestnumber = int(i["demon"]["position"])
                            hardestid = int(i["demon"]["id"])
                        if i["demon"]["position"] < 4:
                            main += 1
                            completed += f'**{i["demon"]["name"]} - #{i["demon"]["position"]} :hot_face: **\n'
                        elif i["demon"]["position"] < 11:
                            main += 1
                            completed += f'**{i["demon"]["name"]} - #{i["demon"]["position"]} :smiling_imp: **\n'
                        elif i["demon"]["position"] < 26:
                            main += 1
                            completed += f'**{i["demon"]["name"]} - #{i["demon"]["position"]} :fire: **\n'
                        elif i["demon"]["position"] < 76:
                            main += 1
                            completed += f'**{i["demon"]["name"]} - #{i["demon"]["position"]}**\n'
                        elif i["demon"]["position"] < 151:
                            extended += 1
                            completed += f'{i["demon"]["name"]} - #{i["demon"]["position"]}\n'
                        else:
                            legacy += 1
                            completed += f'*{i["demon"]["name"]} - #{i["demon"]["position"]}*\n'
                for i in test["data"]["verified"]:
                    if i["position"] < hardestnumber:
                        hardestnumber = int(i["position"])
                        hardestid = int(i["id"])
                    if i["position"] < 4:
                        main += 1
                        verified += f'**{i["name"]} - #{i["position"]} :hot_face: **\n'
                    elif i["position"] < 11:
                        main += 1
                        verified += f'**{i["name"]} - #{i["position"]} :smiling_imp: **\n'
                    elif i["position"] < 26:
                        main += 1
                        verified += f'**{i["name"]} - #{i["position"]} :fire: **\n'
                    elif i["position"] < 76:
                        main += 1
                        verified += f'**{i["name"]} - #{i["position"]}**\n'
                    elif i["position"] < 151:
                        extended += 1
                        verified += f'{i["name"]} - #{i["position"]}\n'
                    else:
                        legacy += 1
                        verified += f'*{i["name"]} - #{i["position"]}*\n'
                if completed == '':
                    completed = 'None\n'
                if verified == '':
                    verified = 'None\n'
                if progresses == '':
                    progresses = 'None\n'
                if hardestid != 0:
                    hardest = f'https://pointercrate.com/api/v2/demons/{hardestid}'
                    harddest = requests.get(hardest)
                    htext = json.loads(harddest.text)
                    if htext["data"]["position"] < 4:
                        hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]} :hot_face: **\n'
                    elif htext["data"]["position"] < 11:
                        hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]} :smiling_imp: **\n'
                    elif htext["data"]["position"] < 26:
                        hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]} :fire: **\n'
                    elif htext["data"]["position"] < 76:
                        hardest = f'**{htext["data"]["name"]} - #{htext["data"]["position"]}**\n'
                    elif htext["data"]["position"] < 151:
                        hardest = f'{htext["data"]["name"]} - #{htext["data"]["position"]}\n'
                    else:
                        hardest = f'*{htext["data"]["name"]} - #{htext["data"]["position"]}*\n'
                else:
                    hardest = 'None'
                dohua = False
                overdohua = False
                completedd = completed.split('\n')
                if len(completedd) > 10:
                    dohua = True
                if len(completedd) > 100:
                    overdohua = True
                if dohua == True:
                    pass
                if premiumcheck(playerr.lower()) != "":
                    emb = discord.Embed(title=f"{nationality} {playerr}", description=f"```{premiumcheck(playerr.lower())}```   ", color=0x73ffdb)
                else:
                    emb = discord.Embed(title=f"{nationality} {playerr}",color=0x73ffdb)
                emb.add_field(name=f"Rank: ", value=rank, inline=True)
                emb.add_field(name=f"Score: ", value=round(float(score), 2), inline=True)
                emb.add_field(name=f"Hardest Demon: ", value=hardest, inline=True)
                emb.add_field(name=f"Stats: ", value=f"{main} Main, {extended} Extended, {legacy} Legacy", inline=False)
                a = 3
                if overdohua == True:
                    a = 6
                for i in range(a):
                    if dohua == False:
                        break
                    complete1 = ''''''
                    if a == 6:
                        rangee = [0,len(completedd)//a,len(completedd)//a * 2, len(completedd)//a * 3, len(completedd)//a * 4, len(completedd)//a * 5, len(completedd)]
                    else:
                        rangee = [0,len(completedd)//a, len(completedd)//a * 2, len(completedd)]
                    for index in range(rangee[i],rangee[i+1]):
                        complete1 += completedd[index] + "\n"
                    if i == 0:
                        emb.add_field(name=f"Demons Completed: ", value=complete1, inline=True)
                    else:
                        emb.add_field(name=f"⠀", value=complete1, inline=True)
                    #emb.add_field(name="", value=verified, inline=True)
                    #emb.add_field(name="", value=verified, inline=True)
                if dohua == False:
                    emb.add_field(name=f"Demons Completed: ", value=completed, inline=True)
                emb.add_field(name="Demons verified:", value=verified, inline=True)
                emb.add_field(name="Progress on:", value=progresses, inline=True)
                emb.set_footer(text=f"Player ID: {id}")
                await ctx.send(embed=emb)
                print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .player {playerr}')
        except Exception as e:
            exceptionn()
            await ctx.send(f'I got an error, I think you just sent a wrong nickname **(or this guy has too much completed demons (Luqualizer for example))**, error code: {e}')
try:
    Bot.run(token)
except Exception as e:
    print("Couldn't login, trying again...")
    time.sleep(30)
