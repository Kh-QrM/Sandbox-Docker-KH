FROM mitmproxy/mitmproxy:latest

# 1. Switch to Root
USER root

# 2. DISABLE the built-in script that forces us back to non-root
ENTRYPOINT []

# 3. Run the command as absolute Root
CMD ["mitmdump", "--flow-detail", "3", "-w", "/data/traffic.log", "--set", "block_global=false"]

EXPOSE 8080