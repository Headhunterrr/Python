import asyncio


async def sleep1(i):
    await asyncio.sleep(i)
    print(f"Sleep1 {i}")


async def sleep2(i):
    await asyncio.sleep(i/3)
    print(f"  Sleep2 {i}")


async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(1, 11):
            tg.create_task(sleep1(i))
            tg.create_task(sleep2(i))

asyncio.run(main())


