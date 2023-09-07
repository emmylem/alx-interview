#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics"""


import sys
from collections import defaultdict
import signal


def print_statistics(total_size, status_counts):
    print(f"Total file size: {total_size}")
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")


def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    def signal_handler(signal, frame):
        print_statistics(total_size, status_counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 9:
                try:
                    status_code = int(parts[-3])
                    total_size += int(parts[-2])
                    status_counts[status_code] += 1
                except ValueError:
                    pass

            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
