import concurrent.futures
import asyncio


class Executor:
    def __init__(self) -> None:
        self.loop = asyncio.get_event_loop()
        self.executor = None

    async def __list_executors__(self, loop, executor, tasks=[]) -> None:
        await asyncio.wait(
            {
                *[
                    j
                    for sub in [
                        [loop.run_in_executor(executor, task)]
                        if callable(task)
                        else task.get_executor(loop, executor)
                        for task in tasks
                    ]  # unpack the list of executers in each class or from raw function
                    for j in sub
                ]
            },
            return_when=asyncio.ALL_COMPLETED,
        )

    def run(self, *executables) -> None:
        self.executor = concurrent.futures.ThreadPoolExecutor(
            max_workers=len(executables) + 1
        )

        self.loop.run_until_complete(
            self.__list_executors__(
                self.loop,
                self.executor,
                executables,
            )
        )

    def close(self):
        self.executor.shutdown(wait=False)
        self.loop.stop()
        print("closed")
