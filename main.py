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


def main():
    while True:
        time.sleep(1)
        print(Kb.get_key(), Server.get_msg())


if __name__ == "__main__":
    try:
        Executor.run(KB, SERV, main)

    except KeyboardInterrupt:
        print("closed")
        sys.exit()
