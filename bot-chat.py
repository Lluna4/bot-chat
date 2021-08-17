import socket
import discord
from discord import embeds 
from discord.utils import get
from discord.ext import commands
import threading
import time
import asyncio

intents = discord.Intents.default()
intents.members = True  
bot = commands.Bot(command_prefix='/', intents=intents)
HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!desconectar"
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER, PORT)
corriendo = True
autor = False

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(ADDR)
connectado = True
t = ""
a = ""
mensaje1 = False

@bot.event
async def on_ready():
    global t
    global mensaje1
    global a
    print("Listo para tus servicios encanto")
    await bot.change_presence(activity=discord.Game(name="Follandome a tu puta madre"))
    x1 = threading.Thread(target=mensaje)
    x1.start()
    guild = bot.get_guild(792826492102377504)
    
    canal = get(guild.text_channels, id=876954699541147649)
    while True:
        if mensaje1 == True:
            
            t2 = discord.Embed(description=t)

            #try:
            print(a)
            b = a[17:-1]
            t2.set_author(name=a, icon_url=f"https://minotar.net/helm/{a}/100.png")

            await canal.send(embed=t2)
            mensaje1 = False
        else:
            pass




def mensaje():
    global t
    global mensaje1
    global autor
    global a
    time.sleep(1)

    
        
    while True:
        if autor == False:
            t1 = cliente.recv(2048).decode()
            t = t1
            autor = True
            
        if autor == True:
            t1 = cliente.recv(2048).decode()
            a = t1
            mensaje1 = True
            autor = False

        


        
        

    




bot.run("NzkyNzQ3ODQ3NzYxMDAyNTM2.X-iN9w.s4mprx-0p5SZdNvwXLinCg420_4")
mensaje()
