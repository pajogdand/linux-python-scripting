import asyncio
async def find_divisialbe(inrange, dev_by):
    print("finding nums in range {} , divisiable by".format(inrange,dev_by))
    located=[]
    for i in range(inrange):
        if i % dev_by == 0:
            located.append(i)
        if i % 50000 == 0:
            await asyncio.sleep(0.00001)
    print("done with nums in range {} , divisiable by".format(inrange, dev_by))
    print("============================================")

async def main():
    divs1 = loop.create_task(find_divisialbe(50000000,100))
    divs2 = loop.create_task(find_divisialbe(600000, 100))
    divs3 = loop.create_task(find_divisialbe(700000, 100))
    await asyncio.wait([divs1,divs2,divs3])
    return divs1,divs2,divs3
    
if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.set_debug(1)
        d1, d2,d3 = loop.run_until_complete(main())
    except Exception as e:
        print(e)
    finally:
        loop.close()