from fastapi import FastAPI, Request
import uvicorn
from middleware import metrics_middleware
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
 


app = FastAPI()

app.middleware("http")(metrics_middleware)

vendas = {
    1: {"produto": "Camiseta", "preco": 50.0},
    2: {"produto": "Calça", "preco": 100.0},
    3: {"produto": "Tênis", "preco": 200.0},
    4: {"produto": "Boné", "preco": 30.0}
}

print("ARQUIVO MAIN CARREGADO")

@app.get("/vendas/{venda_id}")
def get_venda(venda_id: int):  
    venda = vendas.get(venda_id)
    if venda:
        return venda
    return {"error": "Venda não encontrada"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",   # importante usar string
        host="127.0.0.1",
        port=8000,
        reload=True   # habilita auto reload
    )


    