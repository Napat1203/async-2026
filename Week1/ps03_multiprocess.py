from time import sleep, ctime, time, process_time
import multiprocessing
import threading
import os
import psutil

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name, result_queue):
    # ดึง PID ของแต่ละโปรเซส (ซึ่งจะไม่ซ้ำกันเด็ดขาด)
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"{ctime()} | [PID: {pid}] | [TID: {thread_id}] [Thread Name: {thread_name}] กำลังทำงานให้ ลูกค้า {customer_name}...")
    start_cpu = process_time()
    sum(i * i for i in range(10000000)) # จำลองงานที่กิน CPU-bound เยอะ และรอ 5 วินาที
    sleep(5) # พักการทำงานของ Thread นี้ 5 วินาที
    cpu_duration = process_time() - start_cpu
    print(f"{ctime()} | [PID: {pid}] | [TID: {thread_id}] [Thread Name: {thread_name}] ลูกค้า {customer_name}: ได้รับกาแฟแล้ว!")

    # หลังจากทำงานเสร็จ RAM และ CPU ของโปรเซสนี้จะถูกนำไปเก็บใน Queue
    process = psutil.Process(pid)
    mem_mb = process.memory_info().rss / (1024 * 1024)
    result_queue.put((mem_mb, cpu_duration))

def main():
    queue = ['A', 'B', 'C']
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"[time()] [Main PID: {main_pid}] [Main TID: {main_tid}] === เริ่มระบบหลายผู้ทำงาน Multi-processing ===")
    start_time = time()
    main_start_cpu = process_time()

    result_queue = multiprocessing.Queue()
    processes = []
    # สร้างหลายๆ process
    for customer in queue:
        # สร้าง Process ใหม่จากฟังก์ชัน make_coffee
        p = multiprocessing.Process(target=make_coffee, args=(customer, result_queue))
        processes.append(p)
        p.start()

    # รวบรวมข้อมูลจากหลายๆ Process เข้ามา
    child_memories = []
    child_cpu_times = []
    for _ in queue:
        mem, cpu_t = result_queue.get()
        child_memories.append(mem)
        child_cpu_times.append(cpu_t)

    for p in processes:
        p.join()

    duration = time() - start_time

    # คำนวณหน่วยความจำ Main Process และรวมทั้งหมด
    main_process = psutil.Process(os.getpid())
    main_mem = main_process.memory_info().rss / (1024 * 1024)

    total_memory = main_mem + sum(child_memories)
    total_cpu_time = (process_time() - main_start_cpu) + sum(child_cpu_times)

    print(f"[*สรุปผล Multi-processing*]")
    print(f"เวลาที่ใช้ทั้งหมด (Wall Time): {duration:.2f} วินาที")
    print(f"เวลาที่ใช้ CPU ทั้งหมด (Total CPU Time): {total_cpu_time:.4f} วินาที")
    print(f"หน่วยความจำ (Memory RAM) Process: {total_memory:.2f} MB (Main: {main_mem:.2f} MB + ย่อย: {sum(child_memories):.2f} MB)")

if __name__ == "__main__":
    main()
