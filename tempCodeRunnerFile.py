@client.command(name='join', help='Tells the bot to join the voice channel')
# async def join(ctx):
#     if not ctx.message.author.voice:
#         await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
#         return
#     else:
#         channel = ctx.message.author.voice.channel
#     await channel.connect()