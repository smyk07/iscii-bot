from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import subprocess
import sys
from rich import print


class RestartOnChangeHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.start_script()

    def start_script(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen([sys.executable, self.script])

    def on_modified(self, event):
        if event.src_path.endswith(self.script):
            print(f"[light_green]{self.script} changed, restarting...[/]")
            self.start_script()


if __name__ == "__main__":
    script = "main.py"
    event_handler = RestartOnChangeHandler(script)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
