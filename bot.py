import discord
import sys, traceback
import socket
import urllib3
from datetime import datetime
from dateutil.relativedelta import relativedelta
from discord.ext.commands import Bot
from discord.ext import commands

bot = commands.Bot(command_prefix='!', description='UGA CS Bot')

client = discord.Client()

#TODO - CHANGE ON_MESSAGE INTO 2 DIFFERENT FUNCTIONS
#LEARN COMMANDS.COMMAND AND STARTUP_EXTENSIONS
#startup_extensions = ['roles']

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    elif(message.content == "!helpm"):
        await bot.send_message(message.channel, "Sorry, no one can help cure your autism")
        
    elif(message.content == "!help"):
        await bot.send_message(message.channel, "Help is on the way")
    
    if(message.content == "!marriage" and message.channel.name == "nomatt"):
        await nut(message)
                
    if(message.channel.name == 'roles'):
        await role(message)
    
    if(message.content.startswith("!ip")):
        await bot.send_message(message.channel, str(getIP(message.content[4:])))
    
    if(message.content.startswith("!get")):
        await bot.send_message(message.channel, str(req(message.content[5:])))

async def role(message):
    roleDict = {"1301":"482666002925223946",
                "1302":"482666038757163039",
                "1730":"485118772697366542",
                "2610":"482666084638654467",
                "2670":"482666112723714052",
                "2720":"482665821844275200",
                "3030":"485118897167794176",
                "3360":"485118944248856620",
                "4050":"485118967090905104",
                "4060":"485119039660883969",
                "4070":"485119062545006592",
                "4080":"485119111282819073",
                "4130":"485119135504662528",
                "4140":"485119249124425738",
                "4150":"485119185534451732",
                "4210":"485119371350376449",
                "4250":"485119286906585113",
                "4260":"485119310122188801",
                "4270":"485119460911611920",
                "4300":"485119525503893504",
                "4720":"497474963482083328",
                "4835":"485119547469332482",


                #Plane Project roles
                "electronics":"493186797031915520",
                "manufacturing":"493186941974741013"
                }

    if(message.content.startswith("!add")):
        
        if(message.content[5:] == ":^)" or message.content[5:] == "Mod"  ):
            await bot.send_message(message.channel, "No")
            return
        
        roleId = roleDict[message.content[5:]]
        role = discord.utils.get(message.server.roles, id=roleId)
        if message.content[5:] in roleDict:                
            
            try:
                await client.add_roles(message.author, role)
                await bot.send_message(message.channel, "You have been added to: " + str(role) )
                    
            except Exception as e:
                await bot.send_message(message.channel, e)
                    
    elif(message.content.startswith("!rm")):        
            roleId = roleDict[message.content[4:]]
            role = discord.utils.get(message.server.roles, id=roleId)

            if message.content[4:] in roleDict:   
                
                try:
                    await client.remove_roles(message.author, role)
                    await bot.send_message(message.channel, "You have been removed from: " + str(role))
                    
                except Exception as e:
                    await bot.send_message(message.channel, e)
                    
    else:
        await bot.send_message(message.channel, "Invalid operation. Try: !add [class] or !rm[class]")


def getIP(host):
    name = socket.gethostbyname(host)
    return name

def getAddr(host, port, protocol):
    if protocol.lower() == "tcp":
        tup = socket.getaddrinfo(host, port, type = socket.SOCK_STREAM)
    elif protocol.lower() == "udp":
        tup = socket.getaddrinfo(host, port, type = socket.SOCK_DGRAM)
    else:
        tup = "incorrect protocol, tcp or udp"
    return tup

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return

def req(host):
    http = urllib3.PoolManager()
    r = http.request('GET', host)
    return r.headers

async def nut(message):
    tillNut = datetime(2024, 7, 25, 0, 0, 0)
    today = datetime.today()
    rd = relativedelta(tillNut, today)
    mes = "%(years)d years, %(months)d months, %(days)d days, %(hours)d hours, %(minutes)d minutes, and %(seconds)d seconds until Nitin turns a beef sandwich into a chick sandwich " % rd.__dict__
    await bot.send_message(message.channel, mes)
    
@bot.event
async def on_ready():
    print('\nLogged in as: ' + bot.user.name + '\nVersion: ' + discord.__version__ + '\n')
    await bot.change_presence(game=discord.Game(name='PYTHON', type=1))
    await client.login('NDEyNzI5MTE0NjU1NTg4MzYy.DmnKvg.vTKGxkAY_AXCxt2SuyS04QpDybM')
    print('Successfully logged in and booted!')



if __name__ == '__main__':
#for extension in startup_extensions:
#        try:
 #           bot.load_extension(extension)
  #      except Exception:
   #         print('Failed to load extension ' + extension + '.', file=sys.stderr)
    #        traceback.print_exc()

    bot.run('NDEyNzI5MTE0NjU1NTg4MzYy.DmnKvg.vTKGxkAY_AXCxt2SuyS04QpDybM', bot=True, reconnect=True)

