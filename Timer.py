import pygame
import threading
import time
import DrawingFunctions


class Timer:
    def __init__(self, screen):
        self.screen = screen
        self.seconds = 1    # Seconds elapsed from the start of the countdown
        self.thread = threading.Thread(target=self._start_clock)    # Starting our clock
        self.thread.daemon = True   # Making our thread kill itself when the application exists
        self.thread.start()         # Starting our thread

    def _start_clock(self):
        while True:
            # self._display_time()
            self.seconds += 1
            time.sleep(1)

    # Displaying the time on our screen`
    def _display_time(self):
        text = DrawingFunctions.create_text(str(self.seconds), 'comic sans', 48, (250, 250, 250))
        self.screen.blit(text, (950, 950))

