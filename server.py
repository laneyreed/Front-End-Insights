from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gap-test")
def gap_test():
    return render_template("gap-test.html")


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
        # Convert the display format (with spaces/symbols) to concept URL parameter (with hyphens)
        concepts_url_format ={
            "Semantic Elements": "semantic-elements",
            "Complex Forms": "complex-forms",
            "Tables & Lists": "tables-lists",
            "Media & Graphics": "media-graphics",
            "Accessibility": "accessibility",
            "Best Practices": "best-practices"
        }
        #return render_template("dashboard/dashboard.html", lang=language, concepts=concepts, concepts_url_format=concepts_url_format, resources=resources)
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
            "Templating Engines",
            "Data Processing for Frontend", 
            "File Handling & Media",
            "Frontend Asset Management",
            "PyScript",
            "Python-based UI Frameworks"
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


# @app.route("/dashboard/<language>/<concept_url_format>")
# def language_concept(language, concept_url_format):
#     print(language)# html
#     print(concept_url_format)# semantic-elements
#     # Define concepts for each language
#     language_concepts = {
#         "html": {
#             "concepts": [
#                 "Semantic Elements",    
#                 "Complex Forms",
#                 "Tables & Lists",
#                 "Media & Graphics",
#                 "Accessibility",
#                 "Best Practices"
#             ],
#             "resources": ["HTML Tutorial", "https://www.w3schools.com/html"]
#         },
#         "css": {
#             "concepts": [
#                 "Flexbox & Grid",
#                 "Animations", 
#                 "Responsive Design",
#                 "CSS Variables",
#                 "Advanced Selectors",
#                 "Performance"
#             ],
#             "resources": ["CSS Tutorial", "https://www.w3schools.com/css"]
#         },
#         "javascript": {
#             "concepts": [
#                 "ES6+ Features",
#                 "DOM Manipulation",
#                 "Async Programming", 
#                 "Error Handling",
#                 "Modules",
#                 "Best Practices"
#             ],
#             "resources": ["JavaScript Tutorial", "https://www.w3schools.com/js"]
#         },
#         "python": {
#             "concepts": [
#                 "Templating Engines",
#                 "Data Processing for Frontend", 
#                 "File Handling & Media",
#                 "Frontend Asset Management",
#                 "PyScript",
#                 "Python-based UI Frameworks"
#             ],
#             "resources": ["Python For Beginners", "https://www.python.org/about/gettingstarted"]
#         }
#     }
    
#     # Check if language exists
#     if language not in language_concepts:
#         return "Language not found", 404
    
#     # Get language data
#     lang_data = language_concepts[language]
#     print(lang_data['concepts'])
#     # Convert concept URL parameter (with hyphens) to display format (with spaces/symbols)
#     concept_mapping = {
#         # HTML concepts
#         "semantic-elements": "Semantic Elements",
#         "complex-forms": "Complex Forms", 
#         "tables-lists": "Tables & Lists",
#         "media-graphics": "Media & Graphics",
#         "accessibility": "Accessibility",
#         "best-practices": "Best Practices",
        
#         # CSS concepts
#         "flexbox-grid": "Flexbox & Grid",
#         "animations": "Animations",
#         "responsive-design": "Responsive Design", 
#         "css-variables": "CSS Variables",
#         "advanced-selectors": "Advanced Selectors",
#         "performance": "Performance",
        
#         # JavaScript concepts
#         "es6-features": "ES6+ Features",
#         "dom-manipulation": "DOM Manipulation",
#         "async-programming": "Async Programming",
#         "error-handling": "Error Handling",
#         "modules": "Modules",
        
#         # Python concepts
#         "templating-engines": "Templating Engines",
#         "data-processing-frontend": "Data Processing for Frontend",
#         "file-handling-media": "File Handling & Media", 
#         "frontend-asset-management": "Frontend Asset Management",
#         "pyscript": "PyScript",
#         "python-ui-frameworks": "Python-based UI Frameworks"
#     }
    
#     # Check if concept exists
#     if concept_url_format not in concept_mapping:
#         return "Concept not found", 404
    
#     # Get the display name for the concept
#     concept_display = concept_mapping[concept_url_format]
#     print(f"Concept display name: {concept_display}")# Semantic Elements
#     # Check if concept belongs to this language
#     if concept_display not in lang_data["concepts"]:
#         return "Concept not available for this language", 404
    
#     # Render the concept-specific template
#     try:
#         return render_template(
#             f"dashboard/{language}/{language}-dashboard.html",
#             lang=language.upper(),
#             concept=concept_display,
#             concepts=lang_data["concepts"],
#             resources=lang_data["resources"]
#         )
#     except:
#         # Fallback to a generic concept template
#         return render_template(
#             "dashboard/concept.html",
#             lang=language.upper(),
#             # concept=concept_display,
#             concepts=lang_data["concepts"],
#             resources=lang_data["resources"]
#         )


if __name__ == "__main__":
    app.run(debug=True)