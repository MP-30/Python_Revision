import multiprocessing
import os

def worker():
    # Infinite loop to keep CPU busy
    while True:
        pass

def main():
    # Get the number of CPU cores
    num_cores = multiprocessing.cpu_count()

    # Create a process for each CPU core
    processes = []
    for _ in range(num_cores):
        process = multiprocessing.Process(target=worker)
        process.start()
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.join()

if __name__ == "__main__":
    main()
