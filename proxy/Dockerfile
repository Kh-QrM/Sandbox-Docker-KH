FROM mitmproxy/mitmproxy:latest


USER root


ENTRYPOINT []


CMD ["mitmdump", "--flow-detail", "3", "-w", "/data/traffic.log", "--set", "block_global=false"]

EXPOSE 8080