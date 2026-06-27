from flask import Flask, redirect, render_template_string

app = Flask(__name__)

links = {
    "folder/SwJw1LzQRp_SlviJg8oBY0I7Ql8eAw": "https://urlto.me/27Dm8"
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
    title = slug
    description = "Clique para acessar"
    image = ""
    return render_template_string(HTML, title=title, description=description, image=image, url=url)
