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
    try:
        await asyncio.wait_for(keep_printing() , 10)
    except Exception as e:
        print("timeout with :" , e)

asyncio.run(async_main())





