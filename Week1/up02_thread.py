from time import sleep, ctime, time
import threading

def update_cup_number(customer_name):

    print(f"{ctime()} | LCD: Processing for customer {customer_name}...")
    sleep(1)
    print(f"{ctime()} | LCD: Done for customer {customer_name}.")



def make_coffee(customer_name):

    print(f"{ctime()} | Making coffee for {customer_name}...")
    sleep(1)
    print(f"{ctime()} | Coffee ready for {customer_name}!")



def main():

    queue = ['A', 'B', 'C']
    print(f"{ctime()} | === Multi-threading Coffee Machine ===")
    start = time()
    threads = []

    for customer in queue:

        t = threading.Thread(target=lambda c=customer: (make_coffee(c), update_cup_number(c)), name=f"Thread-{customer}")
        threads.append(t)
        t.start()



    for t in threads:
        t.join()

    duration = time() - start
    print(f"{ctime()} | Total time: {duration:.2f} seconds")

if __name__ == "__main__":
    main() 

