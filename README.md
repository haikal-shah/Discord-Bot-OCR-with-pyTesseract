# Python Discord Bot with Tesseract OCR

## Overview

This Discord bot leverages Tesseract OCR to perform optical character recognition.

**Tesseract OCR:**  
[Learn more about Tesseract OCR](https://github.com/tesseract-ocr/tesseract)

## How to Use the Bot

1. **Install Tesseract:**
   Follow the [Tesseract installation guide](https://tesseract-ocr.github.io/tessdoc/Installation.html).

2. **Install Required Packages:**
   Run the following command to install necessary Python packages:

   ```bash
   pip install discord.py python-dotenv pillow pytesseract requests
   ```

   - **discord.py:** Discord API wrapper for Python.
   - **python-dotenv:** Module for managing environment variables.
   - **pillow:** Image processing library.
   - **pytesseract:** Python wrapper for Tesseract OCR.
   - **requests:** Library for making HTTP requests.

3. **Configuration:**
   - Insert your Discord bot token.
   - Optionally, edit the prefix if you want to customize it.

4. **Run the Bot:**
   Execute the following command to start the bot:

   ```bash
   python ocr_bot.py
   ```

## Contribution

Contributions are welcome, feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
