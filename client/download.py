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

def download(url, num_chunks_per_thread):
    for i in range(num_chunks_per_thread):
        try:
            response = requests.get(url)
            print(f"Downloaded {len(response.content)} bytes from {url}")
        except Exception as e:
            print(f"Error downloading from {url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python download.py <total_size_mb> <chunk_size_mb> <url> <num_threads>")
        sys.exit(1)

    total_size_mb = int(sys.argv[1])
    chunk_size_mb = int(sys.argv[2])
    url = sys.argv[3]
    num_threads = int(sys.argv[4])

    num_chunks = total_size_mb // chunk_size_mb
    num_chunks_per_thread = num_chunks // num_threads

    print("Will download {} chunks, {} per thread".format(num_chunks, num_chunks_per_thread))

    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=download, args=(url, num_chunks_per_thread))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
