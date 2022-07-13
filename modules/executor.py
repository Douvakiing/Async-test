import concurrent.futures
import asyncio
from typing import Callable, List


class Executor:
    def __init__(self) -> None:
        self.loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()
        self.executor: concurrent.futures.ThreadPoolExecutor = None
        self.tasks: List[self.__class__.__bases__[0]] = []

    async def __list_executors__(self, loop, executor, tasks=[]) -> None:
        await asyncio.wait(
            {
                *[
                    j
                    for sub in [task.get_executor(loop, executor) for task in tasks]
                    for j in sub
                ]
            },
            return_when=asyncio.ALL_COMPLETED,
        )

    def run(self, *executables) -> None:
        self.tasks = executables
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
        for task in self.tasks:
            task.cancel()


if __name__ == "__main__":
    import time
    from task import Task

    Exec = Executor()

    class TestTask(Task):
        def __init__(self):
            super().__init__()
            super().set_tasks(self.task)
            super().set_looping_tasks(self.looping_task1, self.looping_task2)
            self.i1 = 0
            self.i2 = 0

        def task(self):
            print("Starting")

        def looping_task1(self):
            self.i1 += 1
            print("Task: 1,", self.i1)
            time.sleep(1)

        def looping_task2(self):
            self.i2 -= 1
            print("Task: 2", self.i2)
            time.sleep(1)

    tt = TestTask()

    try:
        Exec.run(tt)
    except KeyboardInterrupt:
        Exec.close()
