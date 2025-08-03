import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading
from keylogger import KeyLogger

class KeyloggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Keylogger GUI - Live Viewer")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.kl = KeyLogger(live_callback=self.display_keystroke)

        self.label = tk.Label(root, text="Live Keylog Viewer", font=("Arial", 14))
        self.label.pack(pady=10)

        self.textbox = scrolledtext.ScrolledText(root, width=45, height=15, font=("Consolas", 10))
        self.textbox.pack(pady=10)
        self.textbox.config(state=tk.DISABLED)

        self.start_btn = tk.Button(root, text="Start Logging", command=self.start_logging, bg="#4CAF50", fg="white", width=20)
        self.start_btn.pack(pady=5)

        self.exit_btn = tk.Button(root, text="Exit", command=self.root.quit, bg="#f44336", fg="white", width=20)
        self.exit_btn.pack(pady=5)

    def display_keystroke(self, key):
        self.textbox.config(state=tk.NORMAL)
        self.textbox.insert(tk.END, key + ' ')
        self.textbox.see(tk.END)
        self.textbox.config(state=tk.DISABLED)

    def start_logging(self):
        messagebox.showinfo("Logging Started", "Press ESC to stop logging.")
        t = threading.Thread(target=self.kl.start_logging)
        t.daemon = True
        t.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyloggerGUI(root)
    root.mainloop()
