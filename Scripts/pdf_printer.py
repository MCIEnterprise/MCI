import sys
import win32api
#import win32printing
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

GHOSTSCRIPT_PATH = "C:\\MCI\\GHOSTSCRIPT\\bin\\gswin32.exe"
GSPRINT_PATH = "C:\\MCI\\GSPRINT\\gsprint.exe"


class Handler(FileSystemEventHandler):

    toggle = False

    def on_modified(self, event):
        self.toggle = not self.toggle
        printer = event.src_path.split(".\\")[1].split(".pdf")[0]
        if printer in sys.argv and self.toggle:
            print(printer)
            # currentprinter = win32printing.win32print.GetDefaultPrinter()
            win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "' +
                                  GHOSTSCRIPT_PATH+'" -printer "'+printer+'" +printer+".pdf"', '.', 0)


observer = Observer()
observer.schedule(Handler(), ".")  # watch the local directory
observer.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    observer.stop()
