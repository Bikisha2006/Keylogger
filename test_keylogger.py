import unittest
from log_handler import LogHandler

class TestLogHandler(unittest.TestCase):
    def test_save_log(self):
        log_data = ["h", "e", "l", "l", "o"]
        handler = LogHandler("test_output.txt")
        handler.save(log_data)

        with open("test_output.txt", "r") as f:
            content = f.read()
        self.assertIn("h e l l o", content)

if __name__ == '__main__':  # Fixed __name__ check
    unittest.main()
