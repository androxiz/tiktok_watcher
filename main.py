import os
import asyncio

from playwright.async_api import async_playwright

from core.tiktok_watcher import watch_videos
from config.config import SEARCH_QUERY

async def main():
    async with async_playwright() as p:
        try:
            browser = await p.chromium.launch(
                executable_path="C:/Program Files/Google/Chrome/Application/chrome.exe", 
                headless=False, 
                args=["--disable-blink-features=AutomationControlled"]
            )
        except Exception as e:
            print(f"[ERROR] Failed to launch browser: {e}")
            return

        if os.path.exists("state.json"):
            context = await browser.new_context(storage_state="state.json")
        else:
            context = await browser.new_context()

        page = await context.new_page()

        if not os.path.exists("state.json"):
            try:
                await page.goto("https://www.tiktok.com/login")
                print("Authorize in your browser (or skip this)")
                input("After this hit Enter")
                await context.storage_state(path="state.json")
            except Exception as e:
                print(f"[ERROR] Failed during login step: {e}")
                await browser.close()


        await page.goto("https://www.tiktok.com")
        
        try:
            await page.wait_for_selector("button[data-e2e='nav-search']")
            await page.click("button[data-e2e='nav-search']")

            await page.wait_for_selector("input[data-e2e='search-user-input']:visible")
            await page.click("input[data-e2e='search-user-input']:visible")
            await page.fill(selector="input[data-e2e='search-user-input']:visible", value=SEARCH_QUERY)
            await page.keyboard.press("Enter")
        except Exception as e:
            print(f"[ERROR] Error during search input: {e}")
            await browser.close()
        
        await page.wait_for_timeout(5000)

        videos = await page.query_selector_all("div[data-e2e='search_top-item']")

        for i, video in enumerate(videos):
            await watch_videos(page=page, video=video, index=i)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
