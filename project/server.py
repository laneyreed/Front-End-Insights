from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard/<language>")
def language_dashboard(language):
    if language not in ["html", "css", "javascript", "python"]:
        return "Language not supported", 404
    if language == "python":
        return render_template("dashboard/python/python-home.html")
    if language == "javascript":
        return render_template("dashboard/javascript/js-home.html")
    if language == "css":
        return render_template("dashboard/css/css-home.html")
    if language == "html":
        return render_template("dashboard/html/html-home.html")

if __name__ == "__main__":
    app.run(debug=True)