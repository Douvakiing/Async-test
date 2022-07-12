from task import Task
from KB import KBHit


class Keyboard(Task):
    def __init__(self) -> None:
        super().__init__(self, self.keyboard)

        self.kb = KBHit()

        self.key = ""

    def keyboard(self) -> None:
        while True:
            if self.kb.kbhit():
                self.key = self.kb.getch()

    def get_key(self):
        return self.key
