from modules.keyboard import Keyboard
from modules.server import TCP_Server
from modules.executor import Executor
from modules.task import Task
import logging
import time

Kb = Keyboard()
Server = TCP_Server()
Exec = Executor()


class MainTask(Task):
    def __init__(self):
        super().__init__()
        super().set_looping_tasks(self.main_task)

    def main_task(self):
        # time.sleep(1)
        print(Kb.get_key(), Server.get_msg())

        if Kb.get_key() == "q":
            Exec.close()


if __name__ == "__main__":
    try:
        Exec.run(Kb, MainTask(), Server)

    except KeyboardInterrupt:
        print("Closing")
        Exec.close()
