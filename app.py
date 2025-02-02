from flask import Flask, render_template, request
import requests_handler
from config import API_URL

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    results = []

    if request.method == "POST":
        query = request.form["query"]
        params = {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": 10  # Número de resultados
        }

        response = request.get(API_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            if "esearchresult" in data and "idlist" in data["esearchresult"]:
                pubmed_ids = data["esearchresult"]["idlist"]
                results = [{"id": pid, "link": f"https://pubmed.ncbi.nlm.nih.gov/{pid}"} for pid in pubmed_ids]

    return render_template("index.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
