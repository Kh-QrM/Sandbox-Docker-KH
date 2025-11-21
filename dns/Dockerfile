FROM ubuntu/bind9:latest

# Copy our custom configuration files
COPY named.conf /etc/bind/named.conf
COPY named.conf.options /etc/bind/named.conf.options

# Run Bind9 in the foreground
CMD ["/usr/sbin/named", "-f", "-u", "bind"]
EXPOSE 53/udp