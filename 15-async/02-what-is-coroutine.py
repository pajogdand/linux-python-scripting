import asyncio
import datetime

def print_now():
    print(datetime.datetime.now())

async def keep_printing(name: str = " ") -> None:
    while True:
        print(name , end=" ")
        print_now()
        await asyncio.sleep(0.50)

async def async_main():
    kp = keep_printing()
    waiter = asyncio.wait_for(kp,3)
    try:
        await waiter
    except Exception as e:
        print("timeout with :" , e)

asyncio.run(async_main())
