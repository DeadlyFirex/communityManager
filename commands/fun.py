from interactions import (slash_command, SlashContext, Extension,
                          OptionType, SlashCommandOption)

from random import choice, randint


class FunCommands(Extension):
    # Choose command
    @slash_command("choose", description="Chooses between two options", options=[
        SlashCommandOption("options",  OptionType.STRING, "List of options", required=True)
    ])
    async def choose_command(self, ctx: SlashContext, **kwargs):
        await ctx.send(f"I choose `{choice(ctx.kwargs["options"].split(", "))}`!")

    # Add command
    @slash_command("add", description="Adds two integers together", options=[
        SlashCommandOption("n1", OptionType.INTEGER, "First integer", required=True),
        SlashCommandOption("n2", OptionType.INTEGER, "Second integer", required=True)
    ])
    async def add_command(self, ctx: SlashContext, **kwargs):
        await ctx.send(f":ok_hand: `{ctx.kwargs["n1"]}` and `{ctx.kwargs["n2"]}` is "
                       f"`{ctx.kwargs["n1"] + ctx.kwargs["n2"]}`.")

    # Cool command
    @slash_command("cool", description="Check if someone is cool", options=[
        SlashCommandOption("target", OptionType.USER, "Target user", required=True)
    ])
    async def cool_command(self, ctx: SlashContext, **kwargs):
        if randint(0, 10) <= 3:
            await ctx.send(f":sunglasses: `{ctx.kwargs["target"].mention}` is very cool!")
        else:
            await ctx.send(f":clown: {ctx.kwargs['target'].mention} is not cool, but a clown.")

    # Joined command
    @slash_command("joined", description="Check a person's join date", options=[
        SlashCommandOption("target", OptionType.USER, "Target user", required=True)
    ])
    async def joined_command(self, ctx: SlashContext, **kwargs):
        await ctx.send(f"{ctx.kwargs["target"].mention} joined at {ctx.kwargs["target"].joined_at}.")

    # Repeat command
    @slash_command("repeat", description="Repeat a message", options=[
        SlashCommandOption("amount", OptionType.INTEGER, "Amount of repeats", required=True),
        SlashCommandOption("message", OptionType.STRING, "Message to repeat", required=True)
    ])
    async def repeat_command(self, ctx: SlashContext, **kwargs):
        for _ in range(ctx.kwargs["amount"]):
            await ctx.send(ctx.kwargs["message"])


def setup(bot):
    FunCommands(bot)
