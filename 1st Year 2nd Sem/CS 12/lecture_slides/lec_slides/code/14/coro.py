from collections import deque

def f(id: str):
    for i in range(5):
        print(f'{id}: Iteration {i}')
        yield


def main():
    task_queue = [f('A'), f('B'), f('C')]
    while task_queue:
        coro = task_queue.pop(0)
        try:
            next(coro)
        except StopIteration:
            continue
        task_queue.append(coro)

main()


async def f():
    print('hello')