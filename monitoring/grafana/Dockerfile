FROM grafana/grafana:8.2.6
COPY ssl/server.pem /var/lib/grafana/ssl/grafana.key
COPY ssl/server.csr /var/lib/grafana/ssl/grafana.csr
COPY ssl/server.crt /var/lib/grafana/ssl/grafana.crt