import hikari
import lightbulb
import math
from ai import llm, duckduckgo_agent

with open("token.key") as token:
    bot = lightbulb.BotApp(token=token.read())

def response_generator(input, response) -> [hikari.Embed]:
    response_length = len(response)
    num_embeds = math.floor(response_length/4096)
    content = ""
    embeds = []
    prompt = input
    
    if len(prompt) > 256:
        prompt = prompt[:256]
    
    if num_embeds == 10:
        for i in range(10):
            embeds.append(hikari.Embed(title=f"Prompt: {prompt} ({i+1}/10)", description=response[response_length*i:response_length*(i+1)]))
        content = "The generated response was too long for Discord, sorry about that!"
        
    elif (0 < num_embeds < 10):
        for i in range(num_embeds):
            embeds.append(hikari.Embed(title=f"Prompt: {prompt} ({i+1}/{num_embeds})", description=response[response_length*i:response_length*(i+1)]))
    else:
        embeds.append(hikari.Embed(title=f"Prompt: {prompt}", description=response))
        
    return content, embeds


@bot.command
@lightbulb.option("text", "What you want to ask NdyAI")
@lightbulb.command("ask", "Ask NdyAI a question", auto_defer = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx: lightbulb.Context) -> None:
    try:
        response = llm(ctx.options.text)
    except:
        await ctx.respond(embed=hikari.Embed(title="Failed to generate response", description="Something went wrong. Please try agian!"))
        return
    
    content, embeds = response_generator(ctx.options.text, response)
    
    await ctx.respond(content=content, embeds=embeds)
    
@bot.command
@lightbulb.option("text", "What you want to ask NdyAI")
@lightbulb.command("search", "Takes much longer but has access to the internet", auto_defer = True)
@lightbulb.implements(lightbulb.SlashCommand)
async def echo(ctx: lightbulb.Context) -> None:
    try:
        response = duckduckgo_agent.run(ctx.options.text)
    except:
        await ctx.respond(embed=hikari.Embed(title="Failed to generate response", description="Something went wrong. Please try agian!"))
        return
    
    content, embeds = response_generator(ctx.options.text, response)
    
    await ctx.respond(content=content, embeds=embeds)
    
bot.run()