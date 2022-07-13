from .task import Task
from .KB import KBHit


class Keyboard(Task):
    def __init__(self) -> None:
        super().__init__()
        super().set_looping_tasks(self.keyboard)

        self.kb = KBHit()

        self.key = ""

    def keyboard(self) -> None:
        if self.kb.kbhit():
            self.key = self.kb.getch()

    def get_key(self):
        key = self.key
        self.key = ""
        return key


if __name__ == "__main__":
    pass
