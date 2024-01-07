# Discord
import discord
from discord.ext import commands
# Managing environment variables
from dotenv import load_dotenv
# Image processing library
from PIL import Image
# Python wrapper for Tesseract OCR
import pytesseract
# HTTP/1.1 requests
import requests

# Set the path to the Tesseract executable, this is the default
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

load_dotenv()
# Insert token
TOKEN = "DISCORD_TOKEN"
# Change to whatever prefix you want
PREFIX = "!"

# Create an intents object for Discord
intents = discord.Intents.default()
intents.messages = True  # Enable the messages intent
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
# Print out connected message
async def on_ready():
    print(f'Connected to {bot.user.name}')

# Change the command here
@bot.command(name='ocr')
async def ocr_command(ctx):
    # Check if an image is attached
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please attach an image.")
        return

    # Get the first attached image
    image_url = ctx.message.attachments[0].url

    # Download the image, don't worry, it does not save the images it's for tesseract to process them
    image = Image.open(requests.get(image_url, stream=True).raw)

    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(image)

    # Send the OCR result
    await ctx.send(f"OCR Result:\n```{text}```")

bot.run(TOKEN)
