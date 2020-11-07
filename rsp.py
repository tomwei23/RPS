import asyncio

import discord
import random
import arena

winstreak = {}
wins = {}
games = {}

class MyClient(discord.Client):

    async def on_ready(self):
        print("Ich habe mich eingeloggt.")

    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            if str(after.channel) == "Bruh":
                try:
                    vc = await after.channel.connect()
                    vc.play(discord.FFmpegPCMAudio('C:\music\movie_1.mp3'))
                    while vc.is_playing():
                        await asyncio.sleep(1)
                    # disconnect after the player has finished
                    vc.stop()
                    await vc.disconnect()
                except discord.errors.ClientException:
                    print("Error")

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        if message.author == client.user:
            return

        author = str(message.author)
        ssps = ["Rock", "Scissors", "Paper"]

        if author not in winstreak:
            winstreak[author] = "0"
            wins[author] = "0"
            games[author] = "0"

        if message.content == ("!rps Rock"):
            result = int(games[author]) + 1
            games[author] = str(result)

            help = ssps[random.randint(0, 2)]

            if help == "Rock":
                embedVar = discord.Embed(title = "Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name = "Result", value="Draw :)", inline=False)
                await message.channel.send(embed = embedVar)

            elif help == "Scissors":
                embedVar = discord.Embed(title="Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name="Result", value="WIN!!", inline=False)

                result = int(winstreak[author]) + 1
                winstreak[author] = str(result)

                result = int(wins[author]) + 1
                wins[author] = str(result)

                await message.channel.send(embed = embedVar)

            elif help == "Paper":
                embedVar = discord.Embed(title="Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name="Result", value="Lose :(", inline=False)

                winstreak[author] = "0"

                await message.channel.send(embed = embedVar)

        elif message.content == ("!rps Scissors"):
            result = int(games[author]) + 1
            games[author] = str(result)

            help = ssps[random.randint(0, 2)]

            if help == "Rock":
                embedVar = discord.Embed(title="Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name="Result", value="Lose :(", inline=False)

                winstreak[author] = "0"

                await message.channel.send(embed=embedVar)

            elif help == "Scissors":
                embedVar = discord.Embed(title="Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name="Result", value="Draw :)", inline=False)
                await message.channel.send(embed=embedVar)

            elif help == "Paper":
                embedVar = discord.Embed(title="Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name="Result", value="WIN!!", inline=False)

                result = int(winstreak[author]) + 1
                winstreak[author] = str(result)

                result = int(wins[author]) + 1
                wins[author] = str(result)

                await message.channel.send(embed=embedVar)

        elif message.content == ("!rps Paper"):
            result = int(games[author]) + 1
            games[author] = str(result)

            help = ssps[random.randint(0, 2)]

            if help == "Rock":
                embedVar = discord.Embed(title="Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name="Result", value="WIN!!", inline=False)

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

            elif help == "Paper":
                embedVar = discord.Embed(title="Rock! Paper! Scissors! GO!")
                embedVar.add_field(name="What bot played", value=help, inline=False)
                embedVar.add_field(name="Result", value="Draw :)", inline=False)

                await message.channel.send(embed=embedVar)

        if message.content == "!rps ws":
            embedVar = discord.Embed(title=author + " has a win streak since restart of: " + str(winstreak[author]) + " wins")

            await message.channel.send(embed=embedVar)

        if message.content == "!rps lbws":
            counter = 0

            embedVar = discord.Embed(title="LEADERBOARD Winstreak")

            for i in sorted(winstreak.items(), key = lambda kv:(kv[1], kv[0]), reverse=True):
                counter+=1
                embedVar.add_field(name="No" + str(counter),value = i,inline=False)

            await message.channel.send(embed = embedVar)

        if message.content == "!rps w":
            embedVar = discord.Embed(title=author + " has wins since restart: " + str(wins[author]) + " wins")

            await message.channel.send(embed=embedVar)

        if message.content == "!rps lbw":
            counter = 0

            embedVar = discord.Embed(title="LEADERBOARD Overall Wins")

            for i in sorted(wins.items(), key = lambda kv:(kv[1], kv[0]), reverse=True):
                counter+=1
                embedVar.add_field(name="No" + str(counter),value = i,inline=False)

            await message.channel.send(embed = embedVar)

        if message.content == "!rps g":
            embedVar = discord.Embed(title=author + " has played rounds since restart: " + str(games[author]) + " games")

            await message.channel.send(embed=embedVar)

        if message.content == "!rps %":
            if int(games[author]) != 0:
                result = (int(wins[author]) / int(games[author])) * 100

                embedVar = discord.Embed(title=author + " has a winning percentage of: " + str(result) + " %")

                await message.channel.send(embed=embedVar)
            else:
                embedVar = discord.Embed(title="You didn't even play one game")

                await message.channel.send(embed=embedVar)

        if message.content == "!rps clr":
            wins.clear()
            games.clear()
            winstreak.clear()
            embedVar = discord.Embed(title="Stats cleared")

        if message.content == "!rps Rock a":
            await arena.arenaPlay(message, games, wins, winstreak)
        elif message.content  == "!rps Scissors a":
            await arena.arenaPlay(message, games, wins, winstreak)
        elif message.content == "!rps Paper a":
            await arena.arenaPlay(message, games, wins, winstreak)
        elif message.content == "!rps pc":
            await arena.arenaPlay(message, games, wins, winstreak)
        elif message.content == "!rps join":
            await arena.join(message)

        if message.content == "!rps h":
            embedVar = discord.Embed(title="Commands")
            embedVar.add_field(name="Play", value="!rps Rock, !rps Scissors, !rps Paper", inline=False)
            embedVar.add_field(name="Winstreak", value="!rps ws", inline=False)
            embedVar.add_field(name="Winstreak leaderboard", value="!rps lbws", inline=False)
            embedVar.add_field(name="Wins", value="!rps w", inline=False)
            embedVar.add_field(name="Wins leaderboard", value="!rps lbw", inline=False)
            embedVar.add_field(name="Games", value="!rps g", inline=False)
            embedVar.add_field(name="Win chance", value="!rps %", inline=False)
            embedVar.add_field(name="Clear stats", value="!rps clr", inline=False)
            embedVar.add_field(name="Arena mode", value="!rps Rock a, !rps Scissors a, !rps Paper a", inline=False)

            await message.channel.send(embed=embedVar)



client = MyClient()
client.run("NzczOTg1MzQ5ODEzOTI3OTc4.X6RMBw.-WUeKsFTk3lb9fcY7O0wgLf2u00")
