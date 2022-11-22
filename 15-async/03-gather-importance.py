import asyncio
import datetime


def print_now():
    print(datetime.datetime.now())

async def keep_printing(name: str="") -> None:
    while True:
        print(name,end=" ")
        print_now()
        await asyncio.sleep(0.5)

# async def async_main():
#     await  asyncio.gather(
#     print_now("first") ,
#     print_now("second") ,
#     print_now("thrid")
#     )

async def async_main() -> None:
    await asyncio.wait_for(
    asyncio.gather(
        keep_printing("first") ,
        keep_printing("second") ,
        keep_printing("thrid")
    ) , 1000 )

asyncio.run(async_main())