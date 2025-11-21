FROM ubuntu/bind9:latest


COPY named.conf /etc/bind/named.conf
COPY named.conf.options /etc/bind/named.conf.options


CMD ["/usr/sbin/named", "-f", "-u", "bind"]
EXPOSE 53/udp