class LogHandler:
    def __init__(self, filename):  # Fixed __init__
        self.filename = filename

    def save(self, log_data):
        with open(self.filename, "a") as file:
            for entry in log_data:
                file.write(entry + " ")
            file.write("\n--- End of Session ---\n")
