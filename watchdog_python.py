import logging, sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

log_path = sys.argv[2]
path = sys.argv[1]

class MyEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return None
        else:
            if event.event_type == 'created':
                print(f"File {event.src_path} was created.")
                logging.info(f"File {event.src_path} was created.")
            elif event.event_type == 'modified':
                print(f"File {event.src_path} was modified.")
                logging.info(f"File {event.src_path} was modified.")
            elif event.event_type == 'deleted':
                print(event)
                print(f"File {event.src_path} was deleted.")
                logging.info(f"File {event.src_path} was deleted.")
            elif event.event_type == 'moved':
                print(f"File {event.src_path} was moved to {event.dest_path}.")
                logging.info(f"File {event.src_path} was moved to {event.dest_path}.")

logging.basicConfig(filename=log_path, filemode='a', level=logging.INFO)
event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, path=path, recursive=True)
observer.start()

try:
    while True:
        observer.join(timeout=1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

print("\nExiting program")