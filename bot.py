import random
import discord
from discord.ext import commands
from discord.utils import find
from datetime import datetime
import sys

#invite bot link just in case
#https://discord.com/api/oauth2/authorize?client_id=736665323159289897&permissions=2048&scope=bot

bot = commands.Bot(command_prefix = 'sc!', help_command=None)
TOKEN = ''

@bot.event
async def on_ready():
    #show python version and servers the bot is in
	print(f'Bot is running at Python {sys.version.split()[0]} on {len(bot.guilds)} servers')
	print('=-=-=-=-=-=-=-=-=-=-=-=')
    #display custom listening status
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.guilds)} servers | HALFWAY TO 10 SERVERS!!! thank you all!❤"))

@bot.event
async def on_guild_join(guild):
    #when the bot joins a new guild, update the status
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.guilds)} servers | HALFWAY TO 10 SERVERS!!! thank you all!❤"))

@bot.command(pass_context=True)
async def scenario(ctx, argpersona, argpersonb):
    #open the text file with scenarios
	scenariof = open("scenarios.txt", "r")
    #read it in a string
	scenariostr = scenariof.read()
    #make an array with every variable being a scenario
	scenarios = scenariostr.split('\n')
    #close the file
	scenariof.close()
    
    #mix the scenarios up
	random.shuffle(scenarios)
    #select a certain scenario
	scennumb = random.randint(0, 97)
    #the code to mix up the inputs
	persona = random.randint(0, 1)

	if persona == 0:
		personb = 1
	elif persona == 1:
		personb = 0

	persons = ([argpersona], [argpersonb])

	X = '**' + ''.join(persons[persona]) + '**'
	Y = '**' + ''.join(persons[personb]) + '**'
    
    #finally the output part, its super messed up, sorry for that
	embed=discord.Embed(title=f"Scenario #{scennumb+1}", description=str(scenarios[scennumb]).replace('{X}', str(X).replace("['", "").replace("']", "")).replace('{Y}', str(Y).replace("['", "").replace("']", "")), color=random.randint(0, 0xFFFFFF))
	embed.set_footer(text="Bot by yourordinaryred#2736 | Scenarios from https://creativichee.tumblr.com/miniscenario")
	await ctx.send(embed=embed)

#invite command
@bot.command()
async def invite(ctx):
	embed=discord.Embed(title="Invite bot", url='https://discord.com/api/oauth2/authorize?client_id=736665323159289897&permissions=2048&scope=bot', color=random.randint(0, 0xFFFFFF))
	embed.set_footer(text="Bot by yourordinaryred#2736 | Scenarios from https://creativichee.tumblr.com/miniscenario")
	await ctx.send(embed=embed)
	
@bot.command()
async def ping(ctx):
	msgs = {
	['Pong!'],
	[f"{ctx.message.author.mention}. You asked for it, so don't complain!"],
	['Someone except the owner actually uses it?'],
	['I, EvaX, humbly subm- Wait, wrong user!!'],
	['Mi pan, zum zum zum, zum zum zum. Mi pan, yakasus, nan nan nan'],
	['mkk'],
	['haha ping go brr']}
	
	msgnumb = random.randint(0, len(msgs))
	
	print(f'{msgs[msgnumb]}: {bot.latency}ms')

@bot.command()
async def help(ctx):
	embed=discord.Embed(title="Help command", color=random.randint(0, 0xFFFFFF))
	embed.add_field(name="sc!scenario <A> <B>", value='Generates a scenario with two persons you input. (If the persons name contains spaces, just surround it with "" brackets, example: sc!scenario "Person A" "Person B")', inline=False)
	embed.add_field(name="sc!help", value="Sends this embed.", inline=False)
	embed.add_field(name="sc!invite", value="Sends an invite for this bot.", inline=False)
	embed.add_field(name="sc!ping", value="Shows the latency of the bot (The only command with humor).", inline=False)
	embed.set_footer(text="Bot by yourordinaryred#2736 | Scenarios from https://creativichee.tumblr.com/miniscenario")
	await ctx.send(embed=embed)


bot.run(TOKEN)
