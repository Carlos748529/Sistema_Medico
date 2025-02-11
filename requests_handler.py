import requests
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    query = ""
    results = []

    if request.method == "POST":
        query = request.form["query"]
        results = get_medical_articles(query)

    return render_template("index.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)

def get_medical_articles(query):
    url = f"https://jsonplaceholder.typicode.com/posts?title_like={query}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Esto lanzará una excepción para códigos de estado HTTP 4xx/5xx
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching articles: {e}")
        return []
