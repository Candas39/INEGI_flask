import os
import json
import requests
#from dotenv import load_dotenv

#load_dotenv()
inegi_token = os.getenv("inegi_token")


def get_info_inegi(tipo_establecimiento, coordenadas, radio):
    base_url = f"https://www.inegi.org.mx/app/api/denue/v1/consulta/Buscar/{tipo_establecimiento}/{coordenadas}/{radio}/{inegi_token}"
    url_completa = base_url.format(tipo_establecimiento, coordenadas, radio)
    payload = ""
    headers = {
        'Cookie': 'BIGipServerLB_apis=3590494474.20480.0000'
    }
    response = requests.request("GET", url_completa, headers=headers, data=payload)
    if response.status_code == 200:
        try:
            return response.json()
        except ValueError:
            return {"error": ValueError}
    else:
        return {"error": f"Error en la solicitud, código de estado: {response.status_code}"}
    