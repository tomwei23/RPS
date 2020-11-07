import random

arena = {}

async def play(message):

        channel = message.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('C:\music\polish_cow_short.mp3'))
        while vc.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        vc.stop()
        await vc.disconnect()

async def join(message):
    channel = message.author.voice.channel
    vc = await channel.connect()

async def arenaPlay(message, games, wins, winstreak):

    author = str(message.author)

    result = int(games[author]) + 1
    games[author] = str(result)

    if message.content == "!rps pc":
        await play(message)

    if author not in arena:
        arena[author] = "0"

    if message.content == ("!rps Rock a"):
        counter = 0

        for i in range(10):
            counter+=1

            ssps = ["Scissors", "Paper"]
            help = ssps[random.randint(0, 1)]

            if help == "Scissors":
                embedVar = discord.Embed(title="Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name="Result", value="WIN!!", inline=False)

                result = int(arena[author]) + 1
                arena[author] = str(result)
                result = int(winstreak[author]) + 1
                winstreak[author] = str(result)
                result = int(wins[author]) + 1
                wins[author] = str(result)

                await message.channel.send(embed=embedVar)

            elif help == "Paper":
                embedVar = discord.Embed(title="Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name="Result", value="Lose :(", inline=False)

                winstreak[author] = "0"

                await message.channel.send(embed=embedVar)

                break

            if counter == 10:
                await play(message)

    elif message.content == ("!rps Scissors a"):
        counter = 0

        for i in range(10):
            counter += 1

            ssps = ["Rock", "Paper"]
            help = ssps[random.randint(0, 2)]

            if help == "Rock":
                embedVar = discord.Embed(title="Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name="Result", value="Lose :(", inline=False)

                winstreak[author] = "0"

                await message.channel.send(embed=embedVar)

                break

            elif help == "Paper":
                embedVar = discord.Embed(title="Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name="Result", value="WIN!!", inline=False)

                result = int(arena[author]) + 1
                arena[author] = str(result)
                result = int(winstreak[author]) + 1
                winstreak[author] = str(result)
                result = int(wins[author]) + 1
                wins[author] = str(result)

                await message.channel.send(embed=embedVar)

                if counter == 10:
                    await play(message)

    elif message.content == ("!rps Paper a"):
        counter = 0

        for i in range(10):
            counter += 1

            ssps = ["Scissors", "Rock"]
            help = ssps[random.randint(0, 2)]

            if help == "Rock":
                embedVar = discord.Embed(title="Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name="Result", value="WIN!!", inline=False)

                result = int(arena[author]) + 1
                arena[author] = str(result)
                result = int(winstreak[author]) + 1
                winstreak[author] = str(result)
                result = int(wins[author]) + 1
                wins[author] = str(result)

                await message.channel.send(embed=embedVar)

            elif help == "Scissors":
                embedVar = discord.Embed(title="Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name="Result", value="Lose :(", inline=False)

                winstreak[author] = "0"

                await message.channel.send(embed=embedVar)

                break

            if counter == 10:
                await play(message)
