import requests
from bs4 import BeautifulSoup

def coletar_ofertas_exemplo():
    url = "https://example.com"  # URL de teste
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    # Exemplo: extrai todos os títulos de <h2>
    ofertas = [h2.get_text().strip() for h2 in soup.find_all("h2")]
    return ofertas

if __name__ == "__main__":
    ofertas = coletar_ofertas_exemplo()
    print("Ofertas encontradas:", ofertas)

