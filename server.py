from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html.jinja2")

@app.route("/dashboard/<language>")
def language_dashboard(language):
    # print(f"Requested language dashboard: {language}")
    print(request.args.get('concept'))
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
        return render_template("dashboard/dashboard.html.jinja2", lang=language, concepts=concepts, resources=resources)
    
    elif language == "css":
        language= "CSS"
        resources = ["CSS Tutorial", "https://www.w3schools.com/css"]
        concepts = [
            "Grid Layout",
            "Flexbox",
            "Animations", 
            "Responsive Design",
            "CSS Variables",
            "Advanced Selectors",
            "Performance"
        ]
        return render_template("dashboard/dashboard.html.jinja2", lang=language, concepts=concepts, resources=resources)
        
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
        return render_template("dashboard/dashboard.html.jinja2", lang=language, concepts=concepts, resources=resources)
        
    elif language == "python":
        language= "Python"
        resources = ["Python For Beginners", "https://www.python.org/about/gettingstarted"]
        concepts = [
            "Templating Engines",
            "Data Processing for Frontend", 
            "File Handling & Media",
            "Frontend Asset Management",
            "PyScript",
            "Python-based UI Frameworks"
        ]
        return render_template("dashboard/dashboard.html.jinja2", lang=language, concepts=concepts, resources=resources)
        
    else:
        return "Language not found", 404





if __name__ == "__main__":
    app.run(debug=True)