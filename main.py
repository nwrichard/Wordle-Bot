import discord, os, random
from replit import db
from keep_alive import keep_alive
from datetime import datetime, timedelta
from threading import Timer
from discord import Webhook, RequestsWebhookAdapter

#casually_heroic_webhook = os.environ['Casually_Heroic_Webhook']
#beans_webhook = os.environ['Beans_Webhook']

webhook = Webhook.from_url(str(casually_heroic_webhook), adapter=RequestsWebhookAdapter())

client = discord.Client()

keep_alive()
client.run(os.getenv('TOKEN'))