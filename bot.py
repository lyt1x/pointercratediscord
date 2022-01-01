import discord
from discord_buttons_plugin import *
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Activity, ActivityType
import requests
import json
import random
from colorama import init, Fore, Back, Style

init(convert=True)
intents = discord.Intents.default()
intents.members = True
Bot = commands.Bot(command_prefix='.', intents=intents)
Bot.remove_command('help')
buttons = ButtonsClient(Bot)

with open('token.txt', 'r') as f:
    token = f.readline()


@Bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.guild is None:
        print(
            f'{Fore.GREEN}{message.author}{Fore.RESET} sent me something in dms, his message: {Fore.CYAN}{message.content}{Fore.RESET}'
        )
        await message.author.send('sadly I dont respond to dms bozo')
        return
    await Bot.process_commands(message)


@Bot.event
async def on_ready():
    print('')
    print('[=========================================================================================]')
    print('')
    print(
        f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Successfully logged in account [{Fore.LIGHTMAGENTA_EX}{Bot.user}{Fore.RESET}]')
    print('')
    print('[=========================================================================================]')
    print('')
    #await Bot.change_presence(activity= discord.Streaming(name="lyt1xxx",url='https://www.twitch.tv/lyt1x'))


@Bot.command()
async def help(ctx):
    await ctx.send('''All the commands:
.player <player name>

.country <country code>

.profile <ping whose profile you want to open, if yours - then type nothing>

.edit youtube_channel <link> или же .edit pointercrate <pointercrate name>

.top <after which place I should sent the top players>

.position <position on the demonlist>

.demon <demon name>

.records <demon name>''')


@Bot.command()
async def records(ctx,*, name=None):
    try:
        if None==None:
            if name == None:
                await ctx.send('You have to use .records <demon name>')
            elif name == "Bloodbath":
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
                j = 0
                for i in data["data"]["records"]:
                    j += 1
                    if j % 25 == 0:
                        await ctx.send(f'Чекаю номер {j}, {i["player"]["name"]}')
                    if i["nationality"] == None:
                        nationality = ''
                    else:
                        nationality = f':flag_{i["nationality"]["country_code"].lower()}:'
                    recordss += f'{nationality} {i["player"]["name"]} - **{i["progress"]}%**\n'
                color = discord.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                emb = discord.Embed(description=recordss, color=color)
                await ctx.send(embed=emb)
                print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .records {name}')
    except Exception as e:
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
            for i in json.loads(r.text):
                if i["name"].lower() == name.lower():
                    data = i
                    break
            text = r.text.replace('[', '')
            text = text.replace(']', '')
            if data == None:
                data = json.loads(text)
            top = int(data["position"])
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
                video = "нету"
            else:
                video = data["video"]
            description = f'''
                Demon name: **{data["name"]}**
    
                List placement: **{top}**
    
                List percent: **{data["requirement"]}%**
    
                Published by: **{data["publisher"]["name"]}**
    
                Verified by: **{data["verifier"]["name"]}**
    
                Video: {video}'''
            color = discord.Color.from_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))
            emb = discord.Embed(description=description, color=color)
            if video != "None":
                await buttons.send(content=None, channel=ctx.channel.id, embed=emb, components=[
                    ActionRow([Button(style=ButtonType().Link, label='👾 Verification', url=data["video"])])])
            else:
                await ctx.send(embed=emb)
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .demon {name}')
    except Exception as e:
        await ctx.send(f'Got an error, code error: {e}')


@Bot.command()
async def position(ctx,position=None):
    try:
        if position == None:
            await ctx.send('No position sent, use .position <demon position>')
        else:
            position = int(position)
            url = f"https://pointercrate.com/api/v2/demons/listed?after={position-1}&before={position+1}"
            r = requests.get(url)
            text = r.text.replace('[', '')
            text = text.replace(']', '')
            data = json.loads(text)
            top = int(data["position"])
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
            description = f'''
    Demon name: **{data["name"]}**
    
    List placement: **{top}**
    
    List percent: **{data["requirement"]}%**
    
    Published by: **{data["publisher"]["name"]}**
    
    Verified by: **{data["verifier"]["name"]}**
    
    Видео: {data["video"]}'''
            emb = discord.Embed(description=description, color=0x3cd10c)
            await buttons.send(content=None, channel=ctx.channel.id, embed=emb, components=[ActionRow([Button(style=ButtonType().Link, label='👾 Верификация', url=data["video"])])])
            print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .position {top}')
    except Exception as e:
        await ctx.send(f'Got an error, code error: {e}')


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
            players += f'#{i["rank"]} {nationality} {i["name"]} - {round(float(i["score"]),2)}, **{hardest}**\n'
        emb = discord.Embed(description=players, color=0x674ea7)
        await ctx.send(embed=emb)
        print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .top {top}')
    except Exception as e:
        await ctx.send(f'Got an error, code error: {e}')


@Bot.command()
async def edit(ctx, argument=None, arg=None):
    try:
        if arg == None:
            await ctx.send('Example: .edit youtube_channel <link> or .edit pointercrate <name>')
        if argument == None:
            await ctx.send('Example: .edit youtube_channel <link> or .edit pointercrate <name>')
        elif argument == "youtube_channel":
            if "https://www.youtube.com" not in arg:
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
            data[str(ctx.author.id)]["pointercrate"] = arg
            with open('profiles.json', 'w') as f:
                json.dump(data, f, indent=4, sort_keys=True)
            await ctx.send(
                'I updated it, please use .profile')
        else:
            await ctx.send('Example: .edit youtube_channel <link> or .edit pointercrate <name>')
        print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .edit {argument} {arg}')
    except Exception as e:
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
        embed = discord.Embed(color=0xFF0000, description=f'''YouTube channel: {data[str(memberr.id)]["youtube_channel"]}
    Pointercrate account: {data[str(memberr.id)]["pointercrate"]}''')
        await buttons.send(content=None, channel=ctx.channel.id, embed=embed, components=[ActionRow(
            [Button(style=ButtonType().Link, label='📕 YouTube', url=data[str(memberr.id)]["youtube_channel"])])])
        print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .profile {member}')
    except Exception as e:
        await ctx.send(f'Something went wrong, and here is what did: {e}')


@Bot.command()
async def country(ctx, *, country=None):
    if country == None:
        await ctx.send('You have to use **.country <country code>**')
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
            playerss += f'#{j}-{i["rank"]} :flag_{i["nationality"]["country_code"].lower()}: {i["name"]} - {round(float(i["score"]),2)}, **{hardest}**\n'
        emb = discord.Embed(description=playerss, color=0xcdff00)
        await ctx.send(embed=emb)
        print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .country {country}')
    except Exception as e:
        await ctx.send(
            f'Got an error, probably you sent a wrong country code (or nobody lives in that country), an example of a country code: RU (you can use lower letters), error code: {e}')


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
                text = r.text.replace('[', '')
                text = text.replace(']', '')
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
                    ban = ":warning: This account is banned on pointercrate"
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
                            completed += f'**{i["demon"]["name"]} - #{i["demon"]["position"]} :hot_face: **\n'
                        elif i["demon"]["position"] < 11:
                            completed += f'**{i["demon"]["name"]} - #{i["demon"]["position"]} :smiling_imp: **\n'
                        elif i["demon"]["position"] < 26:
                            completed += f'**{i["demon"]["name"]} - #{i["demon"]["position"]} :fire: **\n'
                        elif i["demon"]["position"] < 76:
                            completed += f'**{i["demon"]["name"]} - #{i["demon"]["position"]}**\n'
                        elif i["demon"]["position"] < 151:
                            completed += f'{i["demon"]["name"]} - #{i["demon"]["position"]}\n'
                        else:
                            completed += f'*{i["demon"]["name"]} - #{i["demon"]["position"]}*\n'
                for i in test["data"]["verified"]:
                    if i["position"] < hardestnumber:
                        hardestnumber = int(i["position"])
                        hardestid = int(i["id"])
                    if i["position"] < 4:
                        verified += f'**{i["name"]} - #{i["position"]} :hot_face: **\n'
                    elif i["position"] < 11:
                        verified += f'**{i["name"]} - #{i["position"]} :smiling_imp: **\n'
                    elif i["position"] < 26:
                        verified += f'**{i["name"]} - #{i["position"]} :fire: **\n'
                    elif i["position"] < 76:
                        verified += f'**{i["name"]} - #{i["position"]}**\n'
                    elif i["position"] < 151:
                        verified += f'{i["name"]} - #{i["position"]}\n'
                    else:
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
                    hardest = f'{htext["data"]["name"]} - #{htext["data"]["position"]}'
                else:
                    hardest = 'None'
                dataa = f'''
            {ban}
    Name: {playerr}
    Country: {nationality}
    Demonlist rank: {rank}
    Demonlist score: {round(float(score),2)}
    
    `Demons completed`: 
    {completed}
    Progress on: 
    {progresses}
    Demons verified:
    {verified}
    **Hardest demon**:
    {hardest}
            '''
                emb = discord.Embed(description=dataa, color=0x73ffdb)
                await ctx.send(embed=emb)
                print(f'{ctx.guild}, #{ctx.channel}, {ctx.author}, .player {playerr}')
        except Exception as e:
            await ctx.send(
                f'I got an error, I think you just sent a wrong nickname **(or this guy has too much completed demons (Luqualizer for example))**, error code: {e}'
            )

Bot.run(token)
#I want 500 strings
#I want 500 strings
#I want 500 strings
#I want 500 strings
#I want 500 strings
#I want 500 strings
#I want 500 strings
