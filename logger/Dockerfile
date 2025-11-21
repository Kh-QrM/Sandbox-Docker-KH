FROM alpine:latest


RUN apk add --no-cache bash


WORKDIR /data



CMD ["sh", "-c", "touch /data/traffic.log && tail -f /data/traffic.log"]