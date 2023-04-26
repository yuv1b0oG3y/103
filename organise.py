import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/ninenine/Downloads"
to_dir = "/Users/ninenine/Desktop"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"{event.src_path} has been created")
    def on_deleted(self, event):
        print(f"{event.src_path} has been deleted")
    def on_modified(self, event):
        print(f"{event.src_event} has been modified")
    def on_moved(self, event):
        print(f"{event.src_path} has been moved")
for filename in list_of_files:
    name, extension = os.path.splitext(filename)
    #print(name)
    #print(extension)
    if extension == "":
        continue
    if extension in [".pdf"]:
        path1 = from_dir + "/" + filename
        path2 = to_dir + "/" + "pdf_files"
        path3 = to_dir + "/" + "pdf_files" + "/" + filename
        #print("path1", path1)
        #print("path3", path3)
        if os.path.exists(path2):
            print("MOVING" + filename + "...")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("MOVING" + filename + "...")
            shutil.move(path1, path3)

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("Running!")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()