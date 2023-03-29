!pip install discord.py
!pip install nest_asyncio 
import nest_asyncio 
nest_asyncio.apply()

import discord 
from discord.ext import commands
intents = discord.Intents.all()
import random
bot = commands.Bot(command_prefix ="!",intents=intents)

@bot.event
async def on_ready():
    print("Le bot est prêt !")

@bot.command()
async def aled (ctx) :
    await ctx.channel.send("Dis hello au bot pour commencer à jouer !")

@bot.command()
async def commands (ctx) :
    await ctx.channel.send("Utilise !aled pour savoir comment utiliser le bot .")

@bot.event 
async def on_message(message) :
    message.content = str(message.content.lower())
    if message.author == bot.user:
        return
    if message.content.startswith("!") :
        await bot.process_commands(message)
    def check(m):
        return m.author == message.author and message.channel == message.author
    score = 0
    compteur = 0
    enigme1 = "Quel est le langage de programmation le plus populaire ?"
    enigme2 = "Quel est l'abrévation de la RAM ?"
    enigme3 = "Quel est le pire IDE ?"
    enigme4 = "Qui est l'inventeur d'internet ?"
    enigme5 = "La meuilleure école de la tech c'est...?"
    enigmes = [enigme1, enigme2, enigme3, enigme4, enigme5]
    indices = {enigme1 : "Pense à un serpent\nhttps://tenor.com/view/sticking-tongue-out-national-geographic-feeding-a-reticulated-python-secrets-of-the-zoo-down-under-tongue-flick-gif-25270148",
               enigme2 : "C'est en anglais\nhttps://tenor.com/view/fiert%C3%A9-franglais-bilingue-anglais-bad-english-gif-14261085", 
               enigme3 : "C'est en trois lettres\nhttps://tenor.com/view/fist-fight-ice-cube-three-gif-7746733", 
               enigme4 : "Demande à brontis !\nhttps://tenor.com/view/albob-teacher-gif-19309259", 
               enigme5 : "Un établissement ethic\nhttps://tenor.com/view/et-extra-terrestrial-party-disco-celebrate-gif-6155719"
               }
    reponses = {enigme1 : "python", 
                enigme2 : "random access memory", 
                enigme3 : "vim", 
                enigme4 : "tim berners-lee", 
                enigme5 : "hetic"
                }
    choix = {enigme1 : "\n• C\n\n• Python\n\n• JavaScript",
             enigme2 : "\n•Random Access Memory\n\n• Rien A Manger\n\n• Repas Au Mcdo", 
             enigme3 : "\n• Vim\n\n• VScode\n\n• Xcode",
             enigme4 : "\n• Moi\n\n• Toi\n\n• Tim berners-lee",
             enigme5 : "\n• Tech & code\n\n• Hetic\n\n• 42"
            }
        
    if message.content == "hello":
        await message.channel.send("Salut, ici tu peux jouer à un jeu d'énigme\nT'es partant ?\nhttps://tenor.com/view/kto-lbow-hi-hello-hi-there-gif-25347432")
        reponse = await bot.wait_for("message")
        if reponse.content.lower() == "oui" :
            await message.channel.send("Super ! Le jeu va commencer, mais avant, voici les règles :\n1- Si tu trouve la réponse du premier coup tu marque le point\n2- Si c'est trop dur, dit le mot (indice) et je t'aiderai\n3- Si tu veux repartir à zéro dit moi (restart)\n4- Réponds moi toujours en minuscule :)\nSi t'es près pour la première question dit moi go" )
            player = await bot.wait_for("message")

            if player.content.lower() == "go":
                
                while compteur < 5 :

                    question = random.choice(enigmes)
                    embed = discord.Embed(title= "Quizz bot" )
                    embed.add_field(name=question, value = choix[question] , inline = True)
                    await message.channel.send(embed=embed)
                    player = await bot.wait_for("message")

                    if player.content.lower() == "restart" :
                        await message.channel.send("Vous avez reset le jeu")
                        compteur = 0
                        enigmes=[enigme1,enigme2,enigme3,enigme4,enigme5]

                    if player.content.lower() == "indice" :
                        await message.channel.send(indices[question])
                        player = await bot.wait_for("message")

                    while player.content != reponses[question] :
                        await message.channel.send ("Mauvaise réponse, recommence !")
                        player = await bot.wait_for("message")

                        if player.content.lower() == "indice" :
                            await message.channel.send(indices[question])
                            player = await bot.wait_for("message")

                    if player.content.lower() == reponses[question]:
                        await message.channel.send("Bravo !")
                        score += 1
                    compteur += 1
                    enigmes.remove(question)

                if compteur == 5 :
                    await message.channel.send("https://tenor.com/view/bravo-clap-clapping-applause-amazed-gif-16646029\nFin du jeu\n, ton score est de "+str(score))

bot.run("**************************************************************************")


