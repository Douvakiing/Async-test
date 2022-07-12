import threading


class Task:
    def __init__(self):
        self.tasks: List[callable] = []
        self.should_cancel: bool = False

    def set_tasks(self, *tasks):
        self.tasks = tasks

    def cancel(self):
        self.should_cancel = True

    def get_executor(self, loop, executor):
        return [loop.run_in_executor(executor, task) for task in self.tasks]


if __name__ == "__main__":
    print(dir(Task()))
