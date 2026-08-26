import asyncio 

async def producer(queue: asyncio.Queue, total_coupons: int):
    print(f"[Producer] เริ่มสร้างคูปองจำนวน {total_coupons} ใบ...")
    for i in range(1, total_coupons + 1):
        coupon = f"COUPON-{i:02d}"
        await queue.put(coupon)
        print(f" --[Producer] สร้างและใส่คิวสำเร็จ: {coupon}")
        await asyncio.sleep(0.02)

    print("[Producer] สร้างคูปองเสร็จสิ้นเรียบร้อยแล้ว!\n") 

async def consumer(queue: asyncio.Queue, consumer_name: str):
    claimed_coupons = []
    print(f"[{consumer_name}] เริ่มต้นรอรับคูปอง...")

    while True:
        coupon = await queue.get() 

        if coupon is None:
            queue.task_done() 
            break 

        claimed_coupons.append(coupon)
        print(f" -> [{consumer_name}] ได้รับคูปอง: {coupon} (รวมสะสม: {len(claimed_coupons)}) ใบ")

        queue.task_done() 
        await asyncio.sleep(0.05)

    print(f"\n[{consumer_name}] ทำงานเสร็จสิ้น! รวมคูปองที่เก็บได้ทั้งหมด: {len(claimed_coupons)} ใบ")
    print(f"รายการคูปอง: {claimed_coupons}")

async def main():

    TOTAL_COUPONS = 20 
    queue = asyncio.Queue()

    prod_task = asyncio.create_task(producer(queue, TOTAL_COUPONS))
    cons_task = asyncio.create_task(consumer(queue, "Consumer_01"))

    await prod_task 

    await queue.join() 

    await queue.put(None)
    await cons_task 

if __name__=="__main__":
    asyncio.run(main())