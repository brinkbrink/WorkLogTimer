import time
import csv
import os

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        self.project_name = self.get_project_name()

    def get_project_name(self):
        project_name = input("Enter the project name: ").strip()
        return project_name.replace(" ", "_") + ".csv"

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            print("Timer started.")

    def stop(self):
        if self.running:
            self.elapsed_time += time.time() - self.start_time
            self.running = False
            print(f"Timer stopped. Total elapsed time: {self.elapsed_time:.2f} seconds.")
            tasks_completed = input("Enter the tasks completed during this period: ").strip()
            self.write_to_csv(tasks_completed)
            self.reset()

    def pause(self):
        if self.running:
            self.elapsed_time += time.time() - self.start_time
            self.running = False
            print(f"Timer paused. Elapsed time: {self.elapsed_time:.2f} seconds.")

    def resume(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True
            print("Timer resumed.")

    def write_to_csv(self, tasks_completed):
        file_path = self.project_name
        formatted_time = self.format_time(self.elapsed_time)
        file_exists = os.path.isfile(file_path)
        try:
            with open(file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                if not file_exists:
                    writer.writerow(["Date", "Duration", "Task"])
                    file.write("\n")  # Write a new line after the header
                writer.writerow([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), formatted_time, tasks_completed])
            print(f"Elapsed time and tasks written to {file_path}.")
        except Exception as e:
            print(f"Failed to write to {file_path}: {e}")

    def format_time(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        print("Timer reset.")

def main():
    timer = Timer()
    while True:
        command = input("Enter command (start, stop, pause, resume, exit): ").strip().lower()
        if command == "start":
            timer.start()
        elif command == "stop":
            timer.stop()
        elif command == "pause":
            timer.pause()
        elif command == "resume":
            timer.resume()
        elif command == "exit":
            if timer.running:
                timer.stop()
            break
        else:
            print("Invalid command. Please enter 'start', 'stop', 'pause', 'resume', or 'exit'.")

if __name__ == "__main__":
    main()