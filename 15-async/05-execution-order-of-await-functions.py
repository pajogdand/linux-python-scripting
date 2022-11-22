import asyncio

async def print_now(arg):
    print(arg)

# async def async_main():
#     await  asyncio.gather(
#     print_now("first") ,
#     print_now("second") ,
#     print_now("thrid")
#     )

async def async_main() -> None:
    try:
        await asyncio.wait_for(
        asyncio.gather(
            print_now("first") ,
            print_now("second") ,
            print_now("thrid")
        ) , 20 )
    except asyncio.TimeoutError:
        print("oppss timeout")

asyncio.run(async_main())