import asyncio 

async def link_scaper(queue: asyncio.Queue, page_urls: list):
    print("[Producer] เริ่มสแกนหาลิงก์รูปภาพ...")

    for page in page_urls:
        print(f" -- [Producer] สแกนหน้าเว็บ: {page}")
        await asyncio.sleep(0.3)

        img_url_1 = f"https://example.com/images/{page}_imag_"
        img_url_2 = f"https://example.com/images/{page}_imag_"

        await queue.put(img_url_1)
        await queue.put(img_url_2)

    print("[Producer] สแกนหาลิงก์รูปภาพเสร็จสิ้น\n")

async def image_downloader(queue: asyncio.Queue, worker_name: str):
    downloaded_count = 0
    print(f"[{worker_name}] สตาร์ทเตรียมพร้อมโหลดรูป...")

    while True:
        img_url = await queue.get()

        if img_url is None:
            queue.task_done() 
            break 

        downloaded_count += 1 
        print(f" -> [{worker_name}] (รูปที่ {downloaded_count}) กำลังโหลด: {img_url}")
        await asyncio.sleep(0.5)

        queue.task_done() 

    print(f"[{worker_name}] ทำงานเสร็จสิ้น! ดาวน์โหลดรวมทั้งหมด {downloaded_count} รูป")

async def main():
    pages = ["page_1", "page_2", "page_3"]
    queue = asyncio.Queue() 

    producer_task = asyncio.create_task(link_scaper(queue, pages))
    downloader_task = asyncio.create_task(image_downloader(queue, "Downloader_01")) 

    await producer_task 

    await queue.join() 

    await queue.put(None)
    await downloader_task 

if __name__ == "__main__":
    asyncio.run(main())