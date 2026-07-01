# Program 1: The First Coroutine Function
# Concept: Understanding async def and how it differs from a normal function.
import asyncio 

async def greet():
    print("Hello from coroutine!")

print(type(greet))  # This will show that greet is a coroutine function, not a normal function.