import importlib
import time
import os  # 'os' is imported to handle file paths more safely and flexibly
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class CodeChangeHandler(FileSystemEventHandler):
    def __init__(self, input_folder, script_folder):
        self.input_folder = input_folder
        self.script_folder = script_folder

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            day = event.src_path.split(os.path.sep)[-1].replace(".py", "")  # Use os.path.sep to handle the path safely
            print(f"\nDetected changes in {day}.py. Executing...\n")

            try:
                # Ensure the module path is correct for the operating system
                module_name = f"scripts.{day}"  # Do not manually add backslashes
                input_file = f"{self.input_folder}/{day}.txt"  # Path for the input file

                # Import and reload the module
                module = importlib.import_module(module_name)
                importlib.reload(module)

                # Read the input file
                with open(input_file) as f:
                    input_data = f.read()

                # Execute the module functions
                print(f"Results of {day}.py:")
                print("Part 1:")
                print(module.part1(input_data))
                print("\nPart 2:")
                print(module.part2(input_data))
            except Exception as e:
                print(f"Error executing {day}.py: {e}")

if __name__ == "__main__":
    input_folder = "inputs"  # Folder where the input files (.txt) are located
    script_folder = "scripts"  # Folder where the Python scripts (.py) are located
    
    event_handler = CodeChangeHandler(input_folder, script_folder)
    observer = Observer()
    
    # Monitor changes in the script folder
    observer.schedule(event_handler, path=script_folder, recursive=False)
    
    print("Monitoring changes in scripts. Press Ctrl+C to stop.")
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
