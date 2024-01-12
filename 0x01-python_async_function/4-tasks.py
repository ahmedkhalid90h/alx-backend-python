#!/usr/bin/env python3

""" Async basics in Python task 4 """
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times.
    '''
    while n > 0:
        task = task_wait_random(max_delay)
        await task
        delay = task.result()
        n -= 1
        while idx < len(delays) and delay > delays[idx]:
            idx += 1

        delays.insert(idx, delay)

    return delays
