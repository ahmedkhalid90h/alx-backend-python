#!/usr/bin/env python3
""" Measure the runtime """

import asyncio
import random
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure the runtime """
    start = time.perf_counter()
    await asyncio.gather(*([async_comprehension() for i in range(4)]))
    end = time.perf_counter()
    return end - start
