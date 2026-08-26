import asyncio 

async def producer(queue: asyncio.Queue, total_coupons: int):
    """
    Producer: สร้าง Coupon จำนวน 20 ใบแล้วดันลง asyncio.Queue
    """
    print(f"[Producer] เริ่มสร้างคูปองจำนวน {total_coupons} ใบ...")
    for i in range(1, total_coupons + 1):
        coupon = f"COUPON-{i:02d}"
        await queue.put(coupon)
        print(f" --[Producer] สร้างและใส่คิวสำเร็จ: {coupon}")
        await asyncio.sleep(0.01)

    print("[Producer] สร้างคูปองเสร็จสิ้นเรียบร้อยแล้ว!\n") 

async def consumer(queue: asyncio.Queue, consumer_name: str):
    """
    Consumer: ทำหน้าที่ดึงคูปองออกจาก asyncio.Queue มาเก็บไว้
    """
    claimed_coupons = []
    print(f"[{consumer_name}] เริ่มต้นรอรับคูปอง...")

    while True:
        # ดึงคูปองจากคิว (Consumer ตัวไหนว่างก่อน จะแย่งกันดึงได้ก่อน)
        coupon = await queue.get() 

        # ตรวจสอบ Sentinel value (สัญญาณสั่งหยุดทำงาน)
        if coupon is None:
            queue.task_done() 
            break 

        claimed_coupons.append(coupon)
        print(f" -> [{consumer_name}] ได้รับคูปอง: {coupon} (รวมสะสม: {len(claimed_coupons)}) ใบ")

        # แจ้ง Queue ว่าประมวลผลคูปองชิ้นนี้เสร็จเรียบร้อย
        queue.task_done() 
        await asyncio.sleep(0.04) # จำลองระยะเวลาการประมวลผล

    print(f"\n[{consumer_name}] ทำงานเสร็จสิ้น! รวมคูปองที่เก็บได้ทั้งหมด: {len(claimed_coupons)} ใบ")
    return claimed_coupons

async def main():
    TOTAL_COUPONS = 20 
    NUM_CONSUMERS = 2
    queue = asyncio.Queue()

    prod_task = asyncio.create_task(producer(queue, TOTAL_COUPONS))
    # สร้าง Task สำหรับ Consumer 2 ตัวรันขนานกัน
    consumers = [
        asyncio.create_task(consumer(queue, f"Consumer_{i:02d}"))
        for i in range(1, NUM_CONSUMERS + 1)
    ]

    await prod_task 

    # รอให้ Consumer ทั้ง 2 ตัวช่วยกันรุมเคลียร์คูปองใน Queue จนหมด
    await queue.join() 

    # ส่ง Semtinel Value (None) เท่ากับจำนวน Consumer (2 อัน) เพื่อสั่งหยุด Consumer ทุกตัว
    for _ in range (NUM_CONSUMERS):
        await queue.put(None)

    # รอให้ Consumer ทุกตัวปิดการทำงานสมบูรณ์
    await asyncio.gather(*consumers) 
    print("\n=== ระบบประมวลผลคูปองแบบ Multi-Consumer ทำงานเสร็จสิ้นทั้งหมด ===")

if __name__=="__main__":
    asyncio.run(main())