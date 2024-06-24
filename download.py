#!/usr/bin/env python

# Spawn multiple threads and run an HTTP request on each of them indefinitely.
# This is to simulate a large number of egress requests from a VM instance.
#
# Usage:
#   python download.py <url> <num_threads>
#
# Example:
#   python download.py https://www.google.com 10

import requests
import threading
import sys
import time

def download(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Downloaded {len(response.content)} bytes from {url}")
        except Exception as e:
            print(f"Error downloading from {url}: {e}")
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python download.py <url> <num_threads>")
        sys.exit(1)

    url = sys.argv[1]
    num_threads = int(sys.argv[2])

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=download, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
