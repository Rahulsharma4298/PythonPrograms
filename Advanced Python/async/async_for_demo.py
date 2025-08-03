import asyncio
import random

# 1. An asynchronous generator
async def delayed_generator(count):
    for i in range(count):
        print(f"Generator is about to yield {i}...")
        await asyncio.sleep(1)
        yield i
    print("Generator has finished.")

# 2. An async function using async for
async def main():
    print("Starting the async for loop...")
    async for number in delayed_generator(5):
        print(f"Consumed number: {number}")
    print("Async for loop has finished.")

# 3. Running the asyncio program
if __name__ == "__main__":
    asyncio.run(main())