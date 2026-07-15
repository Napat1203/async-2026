# foodcourt_04_wait_for.py
import asyncio
from time import ctime, time 
from food_utils import send_order_to_kitchen 

async def main():
        MY_STUDENT_ID = "6710301034"
        print(f"{ctime} | --- [Task4] Pratice using wait_for to handle timeouts ---")
        
        try:
            print(f"{ctime} | [System] Order sent. Monitoring 2.0s timeout limit...")
            result = await asyncio.wait_for(
                 send_order_to_kitchen(MY_STUDENT_ID,"staek", "T-Bone Steak"),
                 timeout=2.0
            )
            print(f"{ctime()} | Success: {result}")

        except asyncio.TimeoutError:
             print(f"{ctime()} | Timeout occurred: Steak took too long! Leaving the food court now.")

if __name__ == "__main__":
    asyncio.run(main())
