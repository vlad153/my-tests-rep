#!/usr/bin/env sh

docker compose --env-file="$(dirname $0)"/../.env \
    -f "$(dirname $0)"/../docker/docker-compose.prod-image.yml \
    up -d
    
