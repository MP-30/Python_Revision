import os
import time

def measure_bandwidth(interval=1):
    while True:
        # Perform a speed test using speedtest-cli
        os.system("speedtest")

        # Wait for the specified interval before the next test
        time.sleep(interval)

if __name__ == "__main__":
    measure_bandwidth()
