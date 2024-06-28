#!/bin/bash

TOTAL_SIZE_MB=$1
TARGET_URL=$2
CHUNK_SIZE_MB=100

usage() {
    echo "Usage: $0 <total_size_in_mb> <target_url>"
}

if [ $# -ne 2 ]; then
    usage
    exit 1
fi

N_CHUNKS=$(expr $TOTAL_SIZE_MB / $CHUNK_SIZE_MB)
echo "Uploading $N_CHUNKS chunks"

echo "Creating data file..."
head -c "${CHUNK_SIZE_MB}M" /dev/urandom > /tmp/data.bin

# Run curl for each chunk
for i in $(seq 1 $N_CHUNKS); do
    echo "Uploading chunk $i"
    curl -s -X POST -w "%{http_code}\n" --data-binary "@/tmp/data.bin" "$TARGET_URL"
done

echo "Upload complete!"
