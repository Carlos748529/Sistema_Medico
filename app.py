from flask import Flask, render_template, request
from requests_handler import get_medical_articles

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
