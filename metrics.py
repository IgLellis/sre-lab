import prometheus_client
from prometheus_client import Counter, Gauge, Histogram


# Métricas para contagem de vendas

http_requests_total = Counter(
    'http_requests_total', 'Total de requisições HTTP', ['method', 'endpoint', "status_code"],
)

http_error_total = Counter(
    "http_error_total","Total de erros HTTP", ['endpoint'],)

http_request_duration_seconds = Histogram(
    'http_request_duration_seconds', 'Duração das requisições HTTP em segundos', ['endpoint'])

def track_request(method: str, endpoint: str, status_code: int, duration: float):
    http_requests_total.labels(method=method, endpoint=endpoint, status_code=status_code).inc()
    http_request_duration_seconds.labels(endpoint=endpoint).observe(duration)
    if status_code >= 400:
        http_error_total.labels(endpoint=endpoint).inc()

    if status_code >= 400:
        http_error_total.labels(endpoint=endpoint).inc()

    http_request_duration_seconds.labels(endpoint=endpoint).observe(duration)

    