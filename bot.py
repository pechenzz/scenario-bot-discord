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
owner_id = 435750383491481602

@bot.event
async def on_ready():
	print(f'Bot is running at Python {sys.version.split()[0]} on {len(bot.guilds)} servers')
	print('=-=-=-=-=-=-=-=-=-=-=-=')
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.guilds)} servers | what if we were next to eachother on the userlist 😳😳😳 | prefix is sc!"), status=discord.Status.idle)

@bot.event
async def on_guild_join(guild):
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.guilds)} servers | what if we were next to eachother on the userlist 😳😳😳 | prefix is sc!"), status=discord.Status.idle)
	await bot.get_user(owner_id).send(f"Joined {guild.name} with {len(guild.members)} members")
	
@bot.event
async def on_guild_remove(guild):
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{len(bot.guilds)} servers | what if we were next to eachother on the userlist 😳😳😳 | prefix is sc!"), status=discord.Status.idle)
	await bot.get_user(owner_id).send(f"Left {guild.name} with {len(guild.members)} members")

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
    
    #finally the output part, now a bit more fixed
	scop = str(scenarios[scennumb]).replace('1', str(X)).replace('2', str(Y))
	embed=discord.Embed(title=f"Scenario #{scennumb+1}", description=scop, color=random.randint(0, 0xFFFFFF))
	embed.set_footer(text=f"Bot by {bot.get_user(owner_id).name}#{bot.get_user(owner_id).discriminator} | Scenarios from https://creativichee.tumblr.com/miniscenario")
	await ctx.send(embed=embed)
	await bot.get_user(owner_id).send(f"{ctx.author.name} used **{ctx.message.content}** in **{ctx.guild.name}** and got [{scop}]")

#invite command
@bot.command()
async def invite(ctx):
	embed=discord.Embed(title="Invite bot", url='https://discord.com/api/oauth2/authorize?client_id=736665323159289897&permissions=2048&scope=bot', color=random.randint(0, 0xFFFFFF))
	embed.set_footer(text=f"Bot by {bot.get_user(owner_id).name}#{bot.get_user(owner_id).discriminator} | Scenarios from https://creativichee.tumblr.com/miniscenario")
	await ctx.send(embed=embed)
	
@bot.command()
async def ping(ctx):
	user = random.choice(ctx.message.channel.guild.members)
	msgs = ['Pong!'], [f"{ctx.message.author.mention}. You asked for it, so don't complain!"], ['Someone except the owner actually uses it?'], ['I, EvaX, humbly subm- Wait, wrong user!!'], ['mkk'], ['haha ping go brr'], ['YOU HAVE WON NITRO! CLICK THI- wait wrong dm'], ['REEEEEEEEEEEEEEEEEEEEEEEEE'], [f'You want fun? {user.name} show you fun!'], ['get stickbugged lol'], ["""
Mario: Time to take a piss.
Goomba: What the hell are you doing?
Mario: I'm taking a piss.
Goomba: Okay, but why aren't you jumping on me? That's what you're supposed to do.
Mario: I might do it frucking later.
Goomba: No, I'm a motherfrucking enemy, you're supposed to jump on me.
Mario: Okie dokie then, let me pull up my pants again first, and then maybe I'll jump on you.
Goomba: Maybe? Maybe?! Are you out of your frocking mind?! No! Jump on me now, motherfrucker!
Mario: Let me get my pants first!
Goomba: Ugh, fine..."""], ['maybe you could eat blades of grass'], ['but ummm, look, guys, look, its one of my greatest achivements, wario land 4 on gameboy advance, **HAHA**']
	
	msgnumb = random.randint(0, len(msgs))
	
	print(f'{msgs[msgnumb]}: {bot.latency}ms')

@bot.command()
async def help(ctx):
	embed=discord.Embed(title="Help command", color=random.randint(0, 0xFFFFFF))
	embed.add_field(name="sc!scenario <A> <B>", value='Generates a scenario with two persons you input. (If the persons name contains spaces, just surround it with "" brackets, example: sc!scenario "Person A" "Person B")', inline=False)
	embed.add_field(name="sc!help", value="Sends this embed.", inline=False)
	embed.add_field(name="sc!invite", value="Sends an invite for this bot.", inline=False)
	embed.add_field(name="sc!ping", value="Shows the latency of the bot (The only command with humor).", inline=False)
	embed.set_footer(text=f"Bot by {bot.get_user(owner_id).name}#{bot.get_user(owner_id).discriminator} | Scenarios from https://creativichee.tumblr.com/miniscenario")
	await ctx.send(embed=embed)


bot.run(TOKEN)
