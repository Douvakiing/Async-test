from keyboard import Keyboard
from server import TCP_Server
from executor import Executor
from task import Task
import logging
import time
import sys

KB = Keyboard()
SERV = TCP_Server()
EXEC = Executor()


def main():
    while True:
        time.sleep(1)
        print(KB.get_key(), SERV.get_msg())


if __name__ == "__main__":
    try:
        EXEC.run(KB, SERV, main)

    except KeyboardInterrupt:
        print("closed")
        sys.exit()
