import discord
from discord.ext import tasks
import os
from keep_alive import keep_alive

#conexion a discord
#creamos un cliente
estado = discord.Activity(name='nopor de Neblina', type=discord.ActivityType.watching)
client = discord.Client(activity = estado)

#variable con el id del canal
canalNotificaciones = os.environ['notificacionesId']
canalNot = client.get_channel(canalNotificaciones)

#para registrar un evento
@client.event
#dolo se ejecutara cuando el bot esta preparado para ser usado
async def on_ready():
  print(' Nos hemos conectado como {0.user}'.format(client))

  @client.event
  async def on_message(message):
    #message es el mensaje que escribimos nosotros
    if message.author == client.user:
      return
    if message.content.startswith('.thello'):
      await message.channel.send('Holita! :D')
    if message.content.startswith('.tseba'):
      await message.channel.send('Hola amiwito del canal')
    if message.content.startswith('.tines'):
      await message.channel.send('Alabada sea mi creadora :O')
    if message.content.startswith('.tprog'):
      await message.channel.send('Es hora de programar vagos!')
    if message.content.startswith('.tsexy'):
      await message.channel.send('Ahora es cuando voy a buscar como mandar imagenes para filtrar los nudes de Thea')
    if message.content.startswith('.troll'):
      await message.channel.send('Tehee :P')
    
    if message.content.startswith('.t'):
      await canalNot.send('Enviando a notificaciones')

      
  @tasks.loop(minutes = 5.0)
  async def aviso():
    await canalNot.send('cliente.getchannel envia')



keep_alive()

token = os.environ['pass']
client.run(token)


