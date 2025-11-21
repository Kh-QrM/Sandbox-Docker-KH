FROM alpine:latest

# Install basic tools
RUN apk add --no-cache bash

# Create the data directory
WORKDIR /data

# Command: Watch the log file created by the proxy
# We use 'touch' to ensure the file exists before tailing it
CMD ["sh", "-c", "touch /data/traffic.log && tail -f /data/traffic.log"]