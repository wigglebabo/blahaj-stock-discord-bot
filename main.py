import ikea_api,os,discord, random

from dotenv import load_dotenv

def get_availibility(item_number):
    
    # store codes: https://github.com/Ephigenia/ikea-availability-checker/blob/main/src/data/stores.json
    store_gent = 169

    # Constants like country, language, base url
    constants = ikea_api.Constants(country="be", language="en")
    # Search API
    search = ikea_api.Search(constants)
    # Search endpoint with prepared data
    endpoint = search.search("Billy")

    ikea_api.run(endpoint)
    stock = ikea_api.Stock(constants)
    item = stock.get_stock(item_number)


    result = ikea_api.run(item)

    for item in result["availabilities"]:
        if item["classUnitKey"]["classUnitCode"] == "169":
            
            quantity = item["buyingOption"]["cashCarry"]["availability"]["quantity"]
            
            return quantity
            break


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


intents=discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')



@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    
    
    if "blahaj" in message.content.lower():
        if random.randint(0,10) == 10:
            response = f"er staat 1 heel erg grote blahaj achter je"
            await message.channel.send(response)
        else:
            quantity_big = get_availibility("30373588")
            response = f"Er zijn nog {quantity_big} grote blahaj in Gent!"
            await message.channel.send(response)
            quantity_smal = get_availibility("20540663")
            response = f"Er zijn nog {quantity_smal} kleine blahaj in Gent!"
            await message.channel.send(response)

client.run(TOKEN)


