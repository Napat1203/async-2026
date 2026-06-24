from time import sleep, ctime, time

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
    print(f"{ctime()} | === Synchronous Coffee Machine ===")
    star_t = time()
    for customer in queue:
        make_coffee(customer)
        update_cup_number(customer)
    duration = time() - star_t
    print(f"{ctime()} | Total time: {duration:.2f} seconds")
if __name__ == "__main__":
    main()