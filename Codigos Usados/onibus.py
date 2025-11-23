import os
import requests
import folium
import json
from dotenv import load_dotenv

load_dotenv(".env")
token = os.getenv("SPTRANS_TOKEN")

if not token:
    print("❌ ERRO: variável SPTRANS_TOKEN não encontrada no .env")
    exit()

s = requests.Session()
auth_url = f"http://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={token}"
auth = s.post(auth_url)

if auth.text.lower() == "true":
    print("✅ Autenticado com sucesso!")
else:
    print("❌ Falha na autenticação. Verifique seu token.")
    exit()
codigo_linha = input("Digite o código da linha: ")

paradas = s.get(f"http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha={codigo_linha}")
dados_paradas = paradas.json()

print(f"Total de paradas: {len(dados_paradas)}")
print("Exemplo:", dados_paradas[1])
posicoes = s.get(f"http://api.olhovivo.sptrans.com.br/v2.1/Posicao?codigoLinha={codigo_linha}")
dados_posicoes = posicoes.json()
linhas_lapa = s.get(
    "http://api.olhovivo.sptrans.com.br/v2.1/Linha/Buscar?termosBusca=Lapa"
)
linhas_lapa = linhas_lapa.json()
linhas_lapa[:1]
res = s.get(
    f"http://api.olhovivo.sptrans.com.br/v2.1/Parada/BuscarParadasPorLinha?codigoLinha={codigo_linha}"
)
paradas = res.json()
paradas[:1]
from folium import Map, Marker

m = Map(location=[paradas[1]["py"], paradas[1]["px"]], zoom_start=14)
for i in paradas:
    Marker(location=[i["py"], i["px"]], popup=i["np"]).add_to(m)
m.show_in_browser()