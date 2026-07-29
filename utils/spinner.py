import itertools
import threading
import time
import sys


class Spinner:

    def __init__(self, message="Scanning"):

        self.spinner = itertools.cycle(
            ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
        )

        self.running = False

        self.thread = None

        self.message = message

    def start(self):

        self.running = True

        self.thread = threading.Thread(
            target=self.animate,
            daemon=True
        )

        self.thread.start()

    def animate(self):

        while self.running:

            sys.stdout.write(
                "\r"
                + next(self.spinner)
                + " "
                + self.message
            )

            sys.stdout.flush()

            time.sleep(0.1)

    def stop(self):

        self.running = False

        if self.thread:

            self.thread.join()

        sys.stdout.write("\r" + " " * 80 + "\r")

        sys.stdout.flush()