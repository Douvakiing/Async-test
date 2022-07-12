from task import Task
from KB import KBHit


class Keyboard(Task):
    def __init__(self) -> None:
        super().__init__()
        super().set_tasks(self.keyboard)

        self.kb = KBHit()

        self.key = ""

    def keyboard(self) -> None:
        while not self.should_cancel:
            if self.kb.kbhit():
                self.key = self.kb.getch()

    def get_key(self):
        return self.key
