# stock_price_httpx.py (เวอร์ชันสำหรับแจกเป็นโจทย์หรือแนวทางให้นักเรียนเขียน)
import asyncio
import httpx  
from time import ctime

async def fetch_stock_price(server_name: str):

    url = f"http://127.0.0.1:8088/price/{server_name}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=5.0)
        data = response.json()
        return f"[{data['server']}] Price: {data['price_usd']} USD"

async def main():
    tasks = [
        asyncio.create_task(fetch_stock_price("Alpha")),
        asyncio.create_task(fetch_stock_price("Beta")),
        asyncio.create_task(fetch_stock_price("Gamma"))
    ]
    
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    for tasks in done:
        print(f"{ctime()} Winner Result: {tasks.result()}") 
    
    if pending:
        print(f"{ctime()} Cleaning up {len(pending)} pending tasks...")
        for tasks in pending:
            tasks.cancel() 
            try:
                await tasks 
            except asyncio.CancelledError:
                pass
        
if __name__ == "__main__":
    asyncio.run(main())