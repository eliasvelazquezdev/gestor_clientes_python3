from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
import database as db

headers = {"content-type":"charset=utf-8"}
app = FastAPI()

@app.get("/")
async def index():
    content = {"mensaje":"¡Hola mundo!"}

    return JSONResponse(content=content, headers=headers)

@app.get("/html")
async def html():
    content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>¡Hola mundo!</title>
    </head>
    <body>
        <h1>¡Hola mundo!</h1>
    </body>
    </html>
    """
    return Response(content=content, media_type="text/html")

@app.get("/clientes")
async def clientes():
    content = [cliente.cast_dict() for cliente in db.Clientes.lista]

    return JSONResponse(content=content, headers=headers) 

@app.get("/clientes/buscar/{dni}")
async def clientes_buscar(dni: str):
    cliente = db.Clientes.buscar(dni=dni)

    if not cliente:
        raise HTTPException(status_code=500, detail="Cliente no encontrado")

    return JSONResponse(content=cliente.cast_dict(), headers=headers)


print("Servidor de la API...")