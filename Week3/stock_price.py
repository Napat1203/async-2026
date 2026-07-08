# นักเรียนต้องเลือกใช้ asyncio.wait() พร้อมออปชัน return_when=asyncio.FIRST_COMPLETED เท่านั้น (หากใครใช้ gather หรือ wait_for จะไม่ตรงสเปกเงื่อนไขการแข่งส่งข้อมูล)
import asyncio
from time import ctime, time 

async def fetch_stock_price(server_name, delay):
    await asyncio.sleep(delay)  
    return f"[{server_name}] Price: 150 USD" 

async def main():
    tasks = {
        asyncio.create_task(fetch_stock_price("Alpha", 3.0), name="Alpha"),
        asyncio.create_task(fetch_stock_price("Beta", 0.8), name="Beta"),
        asyncio.create_task(fetch_stock_price("Gamma", 1.5), name="Gamma")
        }
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for finished_task in done:
        print(f"{ctime()} Winner Task Result: {finished_task.result()}") 
    
    if pending:
        print(f"{ctime()} Cleaning up {len(pending)} pending tasks...")
        for t in pending:
            t.cancel()
            
asyncio.run(main())