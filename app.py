#! /usr/bin/python
from interactions import Client, Intents, listen, Status
from interactions.ext import prefixed_commands

from services.configuration import Config

config: Config = Config()
client: Client = Client(intents=Intents.ALL, sync_interactions=True)
prefixed_commands.setup(client)


@listen()
async def on_ready():
    print(f"Finished up loading, logged in as <{client.user}>")
    print(f"Application owner is <{config.application.owner}>")
    await client.change_presence(status=Status.DO_NOT_DISTURB)

client.load_extension("commands.fun")
client.start(config.application.credentials.token)
