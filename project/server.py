from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard/<language>")
def language_dashboard(language):
    # Main Navigation Setup

    if language not in ["html", "css", "javascript", "python"]:
        return "Language not supported", 404
    if language == "python":
        mainNavItems = {# Python Main Navigation Setup
            "dashboard_title": "Python",
            "nav_item1": "HTML",
            "nav_item2": "CSS",
            "nav_item3": "JavaScript",
            }
        return render_template("dashboard/python/python-home.html",
                                **mainNavItems)
    if language == "javascript":
        mainNavItems = {# Javascript Main Navigation Setup
            "dashboard_title": "JavaScript",
            "nav_item1": "HTML",
            "nav_item2": "CSS",
            "nav_item3": "Python",
            }
        return render_template("dashboard/javascript/js-home.html",
                                **mainNavItems)
    if language == "css":
        mainNavItems = {# CSS Main Navigation Setup
            "dashboard_title": "CSS",
            "nav_item1": "HTML",
            "nav_item2": "JavaScript",
            "nav_item3": "Python",
            }
        return render_template("dashboard/css/css-home.html",
                                **mainNavItems)
    if language == "html":
        mainNavItems = {# HTML Main Navigation Setup
            "dashboard_title": "HTML",
            "nav_item1": "CSS",
            "nav_item2": "JavaScript",
            "nav_item3": "Python",
            }
        return render_template("dashboard/html/html-home.html",
                                **mainNavItems)

if __name__ == "__main__":
    app.run(debug=True)