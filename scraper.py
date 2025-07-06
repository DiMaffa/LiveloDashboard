"""
scraper.py

Coleta títulos de promoções da Livelo:
- Usa User-Agent de navegador para evitar bloqueios
- Valida resposta HTTP (código 200)
- Remove títulos duplicados
"""

import requests
from bs4 import BeautifulSoup

def coletar_ofertas_livelo():
    """
    Busca a página de ofertas da Livelo e retorna uma lista de títulos únicos.
    """
    url = "https://www.livelo.com.br/ofertas"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        )
    }

    resp = requests.get(url, headers=headers, timeout=10)
    if resp.status_code != 200:
        raise RuntimeError(f"Erro HTTP: {resp.status_code} ao acessar {url}")

    soup = BeautifulSoup(resp.text, "html.parser")

    # Atenção: confirme a tag e classe no "Inspecionar"
    titulos = [
        tag.get_text().strip()
        for tag in soup.find_all("h3", class_="promo-title")
    ]

    # Remover duplicatas mantendo ordem
    vistos = set()
    unicos = []
    for t in titulos:
        if t and t not in vistos:
            vistos.add(t)
            unicos.append(t)

    return unicos

if __name__ == "__main__":
    try:
        ofertas = coletar_ofertas_livelo()
        print("Ofertas encontradas:", ofertas)
    except Exception as e:
        print("Erro ao coletar ofertas:", e)
