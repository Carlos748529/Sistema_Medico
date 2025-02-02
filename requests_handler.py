import requests_handler
from config import API_URL

def get_medical_articles(query, max_results=10):
    """
    Consulta la API de PubMed para obtener artículos médicos relacionados con la búsqueda.

    Parámetros:
    - query (str): Término de búsqueda médica.
    - max_results (int): Número máximo de resultados a obtener.

    Retorna:
    - Lista de diccionarios con ID y enlace de los artículos.
    """
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }

    try:
        response = requests_handler.get(API_URL, params=params)
        response.raise_for_status()  # Lanza un error si la respuesta no es exitosa

        data = response.json()
        articles = []

        if "esearchresult" in data and "idlist" in data["esearchresult"]:
            pubmed_ids = data["esearchresult"]["idlist"]
            articles = [{"id": pid, "link": f"https://pubmed.ncbi.nlm.nih.gov/{pid}"} for pid in pubmed_ids]

        return articles

    except requests_handler.exceptions.RequestException as e:
        print(f"Error al consultar la API: {e}")
        return []
