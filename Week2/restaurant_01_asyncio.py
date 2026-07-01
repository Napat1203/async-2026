import asyncio
from time import time, ctime 

async def greet_diners(customer):
    print(f"{ctime()} Greeting for Customer-{customer} ...")
    await asyncio.sleep(1)
    print(f"{ctime()} Greeting for Customer-{customer} ...Done!") 

async def customer_private_workflow(customer):
    print(f"{ctime()} Taking order for Customer-{customer} ...")
    await asyncio.sleep(1)
    print(f"{ctime()} Taking order for Customer-{customer} ...Done!") 

    print(f"{ctime()} Cooking for Customer-{customer} ...")
    await asyncio. sleep(1)
    print(f"{ctime()} Cooking for Customer-{customer} ...Done!") 

    print(f"{ctime()} Mini Bar for Customer-{customer} ...")
    await asyncio.sleep(1)
    print(f"{ctime()} Mini Bar for Customer-{customer} ...Done!")      

    print(f"\n{ctime()} [Task - {customer}] All served!\n")
async def main():
    customers = ["A", "B", "C"]

    start_time = time()
    for customer in customers:
        await greet_diners(customer)
         
    print(f"{ctime()} ---All customers greeted. FORKING into indepentent Tasks (Brendon)---\n")

    tasks = []
    for customer in customers:
        task = asyncio.create_task(customer_private_workflow(customer))
        tasks.append(task)

    for task in tasks:
        await task
    
    duration = time() - start_time
    print(f"Finished Entire Restaurant Operation in {duration:.2f} seconds ") 

if __name__ == "__main__":
    asyncio.run(main())