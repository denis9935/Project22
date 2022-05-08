import time
import certifi
import asyncio
import  aiohttp
import ssl
import bs4 import BeatifulSoup


start_time = time.time()
all_info = []
items = []
cashes = []
urls = []
years = []


async def load_site_info()
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)

    async with aiohttp.ClientSession(connector=conn) as session:
        tasks = []
        for page in range(1, 5):
            task_1 = asyncio.create_task(get_page_info(session, page))
            tasks.append(task_1)

        await asyncio.gather(*tasks)


async def run_tasks
    global items,cashes, urls, years
    await load_site_info()
    all_info = list(zip(items))
