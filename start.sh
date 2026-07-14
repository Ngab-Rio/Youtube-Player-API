#!/usr/bin/env bash

set -e

IMAGE_NAME="karaoke-player"
CONTAINER_NAME="karaoke-player"
PORT=8000

echo "==> Building image..."
docker build -t $IMAGE_NAME .

echo "==> Removing old container (if exists)..."
docker rm -f $CONTAINER_NAME 2>/dev/null || true

echo "==> Starting container..."
docker run -d \
  --name $CONTAINER_NAME \
  -p $PORT:$PORT \
  --restart unless-stopped \
  $IMAGE_NAME

echo ""
echo "Container started!"
echo "API: http://localhost:$PORT"
