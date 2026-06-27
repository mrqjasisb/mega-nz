from flask import Flask, redirect, render_template_string
import requests

app = Flask(__name__)

links = {
    "folder/SwJw1LzQRp_SlviJg8oBY0I7Ql8eAw": "https://youtube.com/shorts/0tAa8YktpOg?is=d2Apv0wWQh6WNnT9"
}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta property="og:title" content="{{ title }}">
    <meta property="og:description" content="{{ description }}">
    <meta property="og:image" content="{{ image }}">
    <meta http-equiv="refresh" content="0;url={{ url }}">
</head>
<body>Redirecionando...</body>
</html>
"""

@app.route("/<path:slug>")
def redirecionar(slug):
    url = links.get(slug)
    if not url:
        return "Link não encontrado", 404
    try:
        r = requests.get(url, timeout=5)
        title = slug
        description = "Clique para acessar"
        image = ""
    except:
        title = slug
        description = "Clique para acessar"
        image = ""
    return render_template_string(HTML, title=title, description=description, image=image, url=url)

if __name__ == "__main__":
    app.run(debug=False)
