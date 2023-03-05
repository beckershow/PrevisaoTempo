from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from controllerConsumirApiPrevisaoTempo import ControllerConsumirApiPrevisaoTempo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["http://localhost","http://127.0.0.1:3000", 'http://localhost:8080', "http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/getprevisaotempo/{cidade, pais}")
async def get_previsao_tempo(cidade, pais):
    controlerApi = ControllerConsumirApiPrevisaoTempo()
    return controlerApi.consultar_previsaotempo(cidade, pais)

@app.get("/gethistoricopesquisa")
async def get_historico_pesquisa():
    controlerApi = ControllerConsumirApiPrevisaoTempo()
    return controlerApi.consultar_historico_pesquisa()


if __name__ == "__main__":
    uvicorn.run(app, host="192.168.1.52", port=7777)