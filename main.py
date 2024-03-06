# Check if Prisma.fi has Playstation 5 is in stock and send an email if this is so
import telegram
import time
import urllib.request
from bs4 import BeautifulSoup
import requests
import asyncio

log = ""
TOKEN = "7137854022:AAHDvqVRCP6KsTtYgslvaCjpBOEYOELB1PY"
bot = telegram.Bot(TOKEN)
class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def check_availability():
    
    global log
    try:
        page = requests.get('https://www.dzrt.com/en/icy-rush.html').content
        target_phrase = 'Back In Stock Soon'
        soup = BeautifulSoup(page)
        if target_phrase in soup.text:
            print("no dzrt sadlly")
            time.sleep(60)
            return check_availability()
        return asyncio.run(success())
    except:
        log += "Error parsing website "
async def success():
    await bot.send_message(chat_id=-1002141381439, text='توفر دزرتتتت !!!')
def main():
    global log
    check_availability()



if __name__ == '__main__':
    check_availability()