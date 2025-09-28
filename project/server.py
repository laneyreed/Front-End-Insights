from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard/<language>")
def language_dashboard(language):
    if language == "html":
        concepts = [
            "Semantic Elements",    
            "Complex Forms",
            "Tables & Lists",
            "Media & Graphics",
            "Accessibility",
            "Best Practices"
        ]
        return render_template("dashboard/dashboard.html", title="HTML", concepts=concepts)
        
    elif language == "css":
        concepts = [
            "Flexbox & Grid",
            "Animations", 
            "Responsive Design",
            "CSS Variables",
            "Advanced Selectors",
            "Performance"
        ]
        return render_template("dashboard/dashboard.html", title="CSS", concepts=concepts)
        
    elif language == "javascript":
        concepts = [
            "ES6+ Features",
            "DOM Manipulation",
            "Async Programming", 
            "Error Handling",
            "Modules",
            "Best Practices"
        ]
        return render_template("dashboard/dashboard.html", title="JavaScript", concepts=concepts)
        
    elif language == "python":
        concepts = [
            "Variables & Data Types",
            "Functions & Classes", 
            "Loops & Conditionals",
            "File Handling",
            "Libraries & Modules",
            "Error Handling"
        ]
        return render_template("dashboard/dashboard.html", title="Python", concepts=concepts)
        
    else:
        return "Language not found", 404


if __name__ == "__main__":
    app.run(debug=True)