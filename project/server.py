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
        #Main navigation setup by defining the dashboard title and nav items in a dictionary
        # and then passing them to the template using ** unpacking.
        mainNavItems = {# Python Main Navigation Setup
            "dashboard_title": "Python",
            "dashboard_title_icon": "fa-brands fa-python",
            "nav_item1": "HTML",
            "nav_item2": "CSS",
            "nav_item3": "JavaScript",
            "main_nav_icon1": "fa-brands fa-html5",
            "main_nav_icon2": "fa-brands fa-css3",
            "main_nav_icon3": "fa-brands fa-js",
            }
        return render_template("dashboard/python/python-home.html",
                                **mainNavItems)
    if language == "javascript":
        mainNavItems = {# Javascript Main Navigation Setup
            "dashboard_title": "JavaScript",
            "dashboard_title_icon": "fa-brands fa-js",
            "nav_item1": "HTML",
            "nav_item2": "CSS",
            "nav_item3": "Python",
            "main_nav_icon1": "fa-brands fa-html5",
            "main_nav_icon2": "fa-brands fa-css3",
            "main_nav_icon3": "fa-brands fa-python",
            }
        return render_template("dashboard/javascript/js-home.html",
                                **mainNavItems)
    if language == "css":
        mainNavItems = {# CSS Main Navigation Setup
            "dashboard_title": "CSS",
            "dashboard_title_icon": "fa-brands fa-css3",
            "nav_item1": "HTML",
            "nav_item2": "JavaScript",
            "nav_item3": "Python",
            "main_nav_icon1": "fa-brands fa-html5",
            "main_nav_icon2": "fa-brands fa-js",
            "main_nav_icon3": "fa-brands fa-python",
            }
        return render_template("dashboard/css/css-home.html",
                                **mainNavItems)
    if language == "html":
        mainNavItems = {# HTML Main Navigation Setup
            "dashboard_title": "HTML",
            "dashboard_title_icon": "fa-brands fa-html5",
            "nav_item1": "CSS",
            "nav_item2": "JavaScript",
            "nav_item3": "Python",
            "main_nav_icon1": "fa-brands fa-css3",
            "main_nav_icon2": "fa-brands fa-js",
            "main_nav_icon3": "fa-brands fa-python",
            }
        return render_template("dashboard/html/html-home.html",
                                **mainNavItems)

if __name__ == "__main__":
    app.run(debug=True)