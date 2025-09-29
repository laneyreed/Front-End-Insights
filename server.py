from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard/<language>")
def language_dashboard(language):
    if language == "html":
        language= "HTML"
        resources = ["HTML Tutorial", "https://www.w3schools.com/html"]
        concepts = [
            "Semantic Elements",    
            "Complex Forms",
            "Tables & Lists",
            "Media & Graphics",
            "Accessibility",
            "Best Practices"
        ]
        return render_template("dashboard/dashboard.html", lang=language, concepts=concepts, resources=resources)
        
    elif language == "css":
        language= "CSS"
        resources = ["CSS Tutorial", "https://www.w3schools.com/css"]
        concepts = [
            "Flexbox & Grid",
            "Animations", 
            "Responsive Design",
            "CSS Variables",
            "Advanced Selectors",
            "Performance"
        ]
        return render_template("dashboard/dashboard.html", lang=language, concepts=concepts, resources=resources)
        
    elif language == "javascript":
        language= "JavaScript"
        resources = ["JavaScript Tutorial", "https://www.w3schools.com/js"]
        concepts = [
            "ES6+ Features",
            "DOM Manipulation",
            "Async Programming", 
            "Error Handling",
            "Modules",
            "Best Practices"
        ]
        return render_template("dashboard/dashboard.html", lang=language, concepts=concepts, resources=resources)
        
    elif language == "python":
        language= "Python"
        concepts = [
            "Variables & Data Types",
            "Functions & Classes", 
            "Loops & Conditionals",
            "File Handling",
            "Libraries & Modules",
            "Error Handling"
        ]
        resources = ["Python For Beginners", "https://www.python.org/about/gettingstarted"]
        # resources = [
        #     {"beginner": "https://www.learnpython.org/"},
            # {"intermediate": "https://realpython.com/"},
            # {"name": "Official Python Documentation", "url": "https://docs.python.org/3/"},
            # {"name": "Real Python Tutorials", "url": "https://realpython.com/"},
            # {"name": "Automate the Boring Stuff with Python", "url": "https://automatetheboringstuff.com/"}
        #]
        return render_template("dashboard/dashboard.html", lang=language, concepts=concepts, resources=resources)
        
    else:
        return "Language not found", 404


if __name__ == "__main__":
    app.run(debug=True)