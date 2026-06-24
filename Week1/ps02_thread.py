import queue
from time import sleep, ctime, time, process_time
import threading
import os
import psutil

# ฟังก์ชันจำลองการทำกาแฟให้ลูกค้า 1 คน
def make_coffee(customer_name):
    pid = os.getpid()
    thread_id = threading.current_thread().native_id
    thread_name = threading.current_thread().name

    print(f"[time1] | PID: {pid} | TID: {thread_id} | Thread Name: {thread_name} | กำลังชงกาแฟให้ {customer_name}...")
    sum(i*i for i in range(1000000)) # งานคำนวณ CPU-bound ใช้เวลา 5 วินาที
    sleep(5) # งานหน่วงเวลา Thread นี้ 5 วินาที
    print(f"[time1] | PID: {pid} | TID: {thread_id} | Thread Name: {thread_name} | ชงกาแฟให้ {customer_name} ได้เรียบร้อยแล้ว!")

def main():
    queue = ['A', 'B', 'C']
    main_pid = os.getpid()
    main_tid = threading.current_thread().native_id

    print(f"[time1] | Main PID: {main_pid} | Main TID: {main_tid} === เริ่มกระบวนการทำงานแบบ Multi-Thread ===")
    start_time = time()
    start_cpu = process_time() # เริ่มจับเวลา CPU

    threads = []
    # สร้างงานในแต่ละ Thread
    for customer in queue:
        t = threading.Thread(target=make_coffee, args=(customer,), name=f"Thread-{customer}")
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    duration = time() - start_time
    cpu_duration = process_time() - start_cpu

    # ใช้ psutil ตรวจสอบ RAM
    process = psutil.Process(os.getpid())
    mem_mb = process.memory_info().rss / (1024 * 1024)

    print(f"[*สรุปผล Multi-Thread*]")
    print(f"รวมเวลาทั้งหมด (Wall Time): {duration:0.2f} วินาที")
    print(f"รวมเวลาการใช้ CPU (CPU-bound): {cpu_duration:0.4f} วินาที")
    print(f"การใช้หน่วยความจำ (RAM) ทั้งหมด: {mem_mb:0.2f} MB")

if __name__ == "__main__":
    main()