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
# Perform input/output
import io

# Set the path to the Tesseract executable, this is the default
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

load_dotenv()
# Insert token
TOKEN = "{insert your token here}"
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
    # Check if images are attached
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please attach an image.")
        return

    ocr_results = []  # List to store OCR results for each image

    for attachment in ctx.message.attachments:
        image_url = attachment.url

        # Get image. don't worry, it does not save the images it's for tesseract to process them
        image_bytes = await attachment.read()
        image = Image.open(io.BytesIO(image_bytes))

        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(image)
        ocr_results.append(text)

    # Combine OCR results into a single message
    combined_text = "\n\n".join(f"OCR Result for Image {i + 1}:\n{text}" for i, text in enumerate(ocr_results))

    # Send the OCR results
    await ctx.send(combined_text)

bot.run(TOKEN)
