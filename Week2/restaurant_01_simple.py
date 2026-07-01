from time import sleep, ctime, time

def greet_diners(customer):
    print(f"{ctime()} -> Greeting for customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} -> Greeting for customer-{customer} ...Done!")

def take_order(customer):
    print(f"{ctime()} -> Taking Oder for customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} -> Taking Oder for customer-{customer} ...Done!")

def do_cooking(customer):
    print(f"{ctime()} -> Cooking for customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} -> Cooking for customer-{customer} ...Done!")

def mini_bar(customer):
    print(f"{ctime()} -> Mini bar for customer-{customer} ...")
    sleep(1)
    print(f"{ctime()} -> Mini bar for customer-{customer} ...Done!")

if __name__ == "__main__":
    customers = ["A", "B", "C"]

    start_time = time()

    for customer in customers:
        greet_diners(customer)
        take_order(customer)
        do_cooking(customer)
        mini_bar(customer)

    print(f"Total Operation time: {time() - start_time:.2f} seconds")