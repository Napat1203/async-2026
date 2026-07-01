# Program 3: The Event Loop (asyncio.run)
# Concept: Using the Event Loop to actually execute a Coroutine Object.
import asyncio

async def greet():
    print("Hello from the Event loop!")

if __name__ == "__main__":
    asyncio.objactive = greet()  # Create a coroutine object
    asyncio.run(asyncio.objactive)  # Run the coroutine object using the event loop