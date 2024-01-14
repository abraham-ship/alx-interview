#!/usr/bin/python3
import sys


def parse_line(line):
    '''parsing line'''
    try:
        parts = line.split()
        ip_address = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return ip_address, status_code, file_size
    except (ValueError, IndexError):
        return None, None, None


def print_statistics(total_size, status_counts):
    '''print value'''
    print(f'File size: {total_size}')
    for code in sorted(status_counts.keys()):
        print(f'{code}: {status_counts[code]}')


def main():
    '''main function'''
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}
    lines_processed = 0

    try:
        for line in sys.stdin:
            ip_address, status_code, file_size = parse_line(line.strip())
            if ip_address is not None:
                total_size += file_size
                status_counts[status_code] += 1
                lines_processed += 1

            if lines_processed % 10 == 0:
                print_statistics(total_size, status_counts)
                total_size = 0
                status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                                 403: 0, 404: 0, 405: 0, 500: 0}

    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
