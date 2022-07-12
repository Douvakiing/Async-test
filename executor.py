import concurrent.futures
import asyncio


class Executor:
    def __init__(self) -> None:
        self.loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
        self.executor: concurrent.futures.ThreadPoolExecutor = None
        self.tasks = []

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
            super().set_tasks(self.task1, self.task2)

        def task1(self):
            i = 0
            while not self.should_cancel:
                i += 1
                print("Task: 1,", i)
                time.sleep(1)

        def task2(self):
            i = 0
            while not self.should_cancel:
                i -= 1
                print("Task: 2", i)
                time.sleep(1)

    tt = TestTask()

    try:
        Exec.run(tt)
    except KeyboardInterrupt:
        Exec.close()
