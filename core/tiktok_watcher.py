from random import randint

from playwright.async_api import Page, ElementHandle

from config.config import SKIP_PERCENT

async def watch_videos(page: Page, video: ElementHandle, index:int):
    link = await video.query_selector("a")

    if not link:
        print(f"[WARNING] No link found in video item {index+1}. Skipping.")
        return

    url = await link.get_attribute("href")

    await link.click()
    await page.wait_for_load_state("load")

    if randint(1, 100) <= int(SKIP_PERCENT):
        status = "Skipped"
        await page.go_back()
    else:
        try:
            duration_el = await page.wait_for_selector("div[class*='DivSeekBarTimeContainer']", timeout=1000)
            duration = await duration_el.inner_text()

            total_duration = duration.split('/')[1]

            time_parts = list(map(int, total_duration.split(':')))

            seconds = time_parts[0] * 60 + time_parts[1]
        except Exception:
            print("[WARNING] Unable to find duration of the video (set to 5 sec by default)")
            seconds = 5

        await page.wait_for_timeout(seconds * 1000)
        status = f"Watched for {seconds} seconds"
        await page.go_back()

    print(f"Video {index+1}. Link:{url} - {status}")
    await page.wait_for_timeout(2000)