from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = 'sqlite:///../storage.db'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)



from .models import Paper
from .models import Author
from .models import Category

@app.route("/")
def paginapadrao():
    barra_menu = ["Início", "Blog", "Sobre", "Contato"]
    artigo = Paper.query.all()
    autor = Author.query.all()
    categoria = Category.query.all()
    tamanho = len(Paper.query.all())
    if tamanho>6:
        tamanho = 5


    return render_template("index.html",menu=barra_menu, artigo=artigo, tamanho=tamanho)

                        # artigo=artigo, autor=autor, categoria=categoria)



@app.route("/blog/<slug>")
def pagina_blog(slug):

    barra_menu = ["Início", "Blog", "Sobre", "Contato"]
    artigo = Paper.query.filter_by(slug=slug)
    tamanho = len(Paper.query.all())


    for i in range(tamanho):
        if artigo[i].slug == slug:
            return render_template("blog_unitario.html", menu=barra_menu, artigo_exibir=artigo[0])



@app.route("/blog/")
def paginapadrao_blog():
    barra_menu = ["Início", "Blog", "Sobre", "Contato"]
    artigo = Paper.query.all()
    return render_template("blog.html", menu=barra_menu, artigo=artigo)

@app.route("/contact/")
def paginapadrao_contato():
    barra_menu = ["Início", "Blog", "Sobre", "Contato"]

    return render_template("contact.html", menu=barra_menu)

@app.route("/about/")
def paginapadrao_about():
    barra_menu = ["Início", "Blog", "Sobre", "Contato"]

    return render_template("about.html", menu=barra_menu)
