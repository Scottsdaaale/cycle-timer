import tkinter as tk
import time
from datetime import datetime


class StopwatchApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Stopwatch")
        self.master.geometry("300x150")

        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0

        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00.00")

        self.time_label = tk.Label(
            master, textvariable=self.time_var, font=("Arial", 30))
        self.time_label.pack(pady=20)

        self.toggle_button = tk.Button(
            master, text="Start", command=self.toggle_stopwatch, bg="red", fg="white", font=("Arial", 16))
        self.toggle_button.pack()

        self.update_time()

    def toggle_stopwatch(self):
        if self.is_running:
            self.stop()
        else:
            self.start()

    def start(self):
        self.is_running = True
        self.start_time = time.time() - self.elapsed_time
        self.toggle_button.config(text="Stop")

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.elapsed_time = time.time() - self.start_time
            self.toggle_button.config(text="Start")
            self.log_time()

    def update_time(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time

        hours, rem = divmod(self.elapsed_time, 3600)
        minutes, rem = divmod(rem, 60)
        seconds = int(rem)
        milliseconds = int((rem - seconds) * 100)

        time_str = f"{int(hours):02d}:{int(minutes):02d}:{seconds:02d}.{milliseconds:02d}"
        self.time_var.set(time_str)

        self.master.after(50, self.update_time)

    def log_time(self):
        with open("stopwatch_log.txt", "a") as log_file:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{current_time} - Elapsed time: {self.time_var.get()}\n"
            log_file.write(log_entry)


if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
