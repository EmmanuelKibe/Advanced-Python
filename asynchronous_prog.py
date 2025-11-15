""" #A normal synchronous function
import time

def fetch_data():
    time.sleep(3)  # Pretend to fetch something
    return "Data loaded"

#print("Start")
data = fetch_data()   # Everything stops here for 3 seconds
#print(data)
#print("End") """

#An asynchronous version
import asyncio

async def fetch_data():
    await asyncio.sleep(3)  # Non-blocking wait
    return "Data loaded"

async def main():
    print("Start")
    task = asyncio.create_task(fetch_data())  # Start task in background
    print("Doing other work...")
    data = await task  # Come back when ready
    print(data)
    print("End")

asyncio.run(main())
