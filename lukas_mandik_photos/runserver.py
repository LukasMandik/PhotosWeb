#!/usr/bin/.env python
import os
import sys
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        subprocess.call(['touch', os.path.join(BASE_DIR, 'reload')])

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    subprocess.Popen(['python', 'manage.py', 'runserver'])
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, BASE_DIR, recursive=True)
    observer.start()
    try:
        while True:
            observer.join(1)
            with open(os.path.join(BASE_DIR, 'reload'), 'r') as f:
                f.read()
            os.remove(os.path.join(BASE_DIR, 'reload'))
            observer.stop()
            subprocess.call(['killall', '-HUP', 'python'])
            observer.start()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
