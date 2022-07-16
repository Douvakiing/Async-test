import asyncio

if __name__ == "__main__":
    from task import Task
else:
    from .task import Task
import concurrent.futures
from typing import Callable, List


class Executor:
    def __init__(self) -> None:
        self.loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
        self.executor: concurrent.futures.ThreadPoolExecutor = None
        self.tasks = []

    def __list_executors__(self, loop, executor, tasks=[]) -> None:
        return [
            j
            for sub in [task.get_executor(loop, executor) for task in tasks]
            for j in sub
        ]

    async def run(self, *executables) -> None:
        self.tasks = executables
        # self.executor =

        with concurrent.futures.ProcessPoolExecutor(max_workers=32) as process_pool:
            results = await asyncio.gather(
                *self.__list_executors__(self.loop, process_pool, executables)
            )

            print(results)
        # self.loop.run_until_complete(
        #     self.__list_executors__(
        #         self.loop,
        #         self.executor,
        #         executables,
        #     )
        # )

    def close(self):
        self.loop.close()
        for task in self.tasks:
            task.cancel()


if __name__ == "__main__":
    import time

    Exec = Executor()

    class TestTask(Task):
        def __init__(self):
            super().__init__()
            # super().set_tasks(self.task, self.looping_task1, self.looping_task2)
            super().set_looping_tasks(self.looping_task1, self.looping_task2)
            self.i1 = 0
            self.i2 = 0

        def task(self):
            print("Starting")
            time.sleep(1000)

        def looping_task1(self):
            self.i1 += 1
            print("Task: 1,", self.i1)
            time.sleep(1)
            return "sex"

        def looping_task2(self):
            self.i2 -= 1
            print("Task: 2", self.i2)
            time.sleep(1)

    tt = TestTask()

    try:
        Exec.run(tt)
    except KeyboardInterrupt:
        Exec.close()
