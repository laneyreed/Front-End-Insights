from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard/<language>")#route for language-specific dashboards
# endpoint name comes from your Flask function name, not the URL parameter
def language_dashboard(language):  # endpoint for language-specific dashboards: request.endpoint = language_dashboard
    if language not in ["html", "css", "javascript", "python"]: # Validate language
        return "Language not supported", 404
        # or  language = 'html'  # Fallback to default
    # return render_template(f"dashboard/{language}.html")
    if language == "python":
        # {% if request.view_args and request.view_args.get('language') == 'python' %}active{% endif %}
            # request.view_args and prevents errors if view_args is None
        # request.args contains query parameters
        # request.form contains form data
        # request.cookies contains cookies
        # request.headers contains request headers
        # request.remote_addr contains the client's IP address
        # request.user_agent contains the user agent string
        # request.is_secure indicates if the request was made over HTTPS
        # request.content_type contains the content type of the request
        # request.content_length contains the content length of the request
        return render_template("dashboard/python/python-home.html", title="Python")
    if language == "javascript":
        return render_template("dashboard/javascript/js-home.html", title="JavaScript")
    if language == "css":
        return render_template("dashboard/css/css-home.html", title="CSS")
    if language == "html":
        return render_template("dashboard/html/html-home.html", title="HTML")

if __name__ == "__main__":
    app.run(debug=True)