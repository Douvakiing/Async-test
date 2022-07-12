from keyboard import Keyboard
from server import TCP_Server
from executor import Executor
from task import Task
import logging
import time
import sys

Kb = Keyboard()
Server = TCP_Server()
Executor = Executor()


class MainTask(Task):
    def __init__(self):
        super().__init__()
        super().set_tasks(self.main_task)

    def main_task(self):
        while not self.should_cancel:
            # time.sleep(1)
            print(Kb.get_key(), Server.get_msg())


if __name__ == "__main__":
    try:
        Executor.run(Kb, Server, MainTask())

    except KeyboardInterrupt:
        Executor.close()
