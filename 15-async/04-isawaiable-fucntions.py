import asyncio
import inspect


async def keep_printing():
    print("printing")

async def async_function() -> None:
        await keep_printing()


coroutine = async_function()

print(type(async_function))
print(type(coroutine))

print(inspect.isawaitable(async_function))
print(inspect.isawaitable(coroutine))

asyncio.run(async_function())