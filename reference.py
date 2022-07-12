import concurrent.futures
import asyncio
import msvcrt
import time

key = ""


def keyboard():
    global key

    while True:
        key = ord(msvcrt.getch())


def printing():
    while True:
        print(key)


async def main(loop, executor):
    await asyncio.wait(
        {
            loop.run_in_executor(executor, keyboard),
            loop.run_in_executor(executor, printing),
        },
        return_when=asyncio.ALL_COMPLETED,
    )


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)
        loop.run_until_complete(main(loop, executor))

    except KeyboardInterrupt:
        pass
