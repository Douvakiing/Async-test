class Task:
    def __init__(self, *tasks):
        self.tasks = tasks

    def get_executor(self, loop, executor):
        return [loop.run_in_executor(executor, task) for task in self.tasks]
