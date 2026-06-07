import asyncio
import time

async def f():
    await asyncio.sleep(30) # Explained in next slide
    print('fello')


async def g():
    await asyncio.sleep(1) # Explained in next slide
    print('gello')


async def h():
    await asyncio.sleep(2) # Explained in next slide
    print('hello')


async def main():
    await asyncio.gather(*[f(), g(), h()])
    print('Done')

asyncio.run(main())

for i in range(100):
    print(f'count {i}')
    time.sleep(1)