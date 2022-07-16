import threading
from typing import Callable, List


class Task:
    def __init__(self):
        self.tasks: List[Callable] = []
        self.should_cancel: bool = False
        self.event = threading.Event()

    def set_tasks(self, *tasks):
        self.tasks += list(tasks)

    def set_looping_tasks(self, *tasks):
        for task in tasks:
            global x

            def x():
                while not self.event.is_set():
                    task()

            self.tasks.append(x)

    def precancel(self):
        pass

    def cancel(self):
        self.precancel()
        self.event.set()

    def get_executor(self, loop, executor):
        return [
            loop.run_in_executor(executor, task, i) for i, task in enumerate(self.tasks)
        ]


if __name__ == "__main__":
    print(dir(Task()))
