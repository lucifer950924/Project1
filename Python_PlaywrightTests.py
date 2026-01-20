from playwright.sync_api import Playwright
from playwright.async_api import async_playwright
import os,time,pathlib,asyncio,csv,tracemalloc

async def RunPlaywright(URL:str):
    tracemalloc.start()
    currDir  = os.getcwd()
    runTimeDataPath = os.path.join(currDir,'Data','RunTimeData.csv')
    with open(runTimeDataPath,'r',encoding='utf-8') as file:
        lines = csv.reader(file)
        lines = dict(lines)

    
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(
            channel = lines['PlaywrightChannel'],
            headless = False,
            args = ['--start-maximized']
        )
        context = await browser.new_context(viewport=None)
        page = await context.new_page()
        await page.goto(URL)
        title = await page.title()
        print(title)
        print(page.viewport_size)
        

        



asyncio.run(RunPlaywright('https://testautomationpractice.blogspot.com/'))