import time
import sys
import signal
LOG_FILE_PATH = "C:\Users\aAdmin\AppData\Local\Programs\Python\Python312"
KEYWORDS = ["ERROR", "WARNING", "INFO"]

def signal_handler(sig, frame):
    print("\nStopping log monitoring...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def monitor_log():
    with open(LOG_FILE_PATH, "r") as log_file:
        log_file.seek(0, 2)  # Move the cursor to the end of the file
        while True:
            line = log_file.readline()
            if not line:
                time.sleep(0.1)  # Sleep briefly to avoid high CPU usage
                continue
            for keyword in KEYWORDS:
                if keyword in line:
                    print(f"Found '{keyword}' in log: {line.strip()}")
if __name__ == "__main__":
    print(f"Monitoring log file: {LOG_FILE_PATH}")
    monitor_log()
