from flask import Flask
from flask import render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask import request
from .forms import Authorforms, Categoryforms
SQLALCHEMY_DATABASE_URI = 'sqlite:///../storage.db'


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
app.config['WTF_CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = 'fisica_aqui_e_allan_123456'


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

@app.route("/forms/", methods=['GET', 'POST'])
def paginapadrao_forms():
    barra_menu = ["Início", "Blog", "Sobre", "Contato"]
    author_form = Authorforms()

    if author_form.validate_on_submit():
        name = author_form.name.data
        email = author_form.email.data
        website = author_form.website.data
        photo = author_form.photo.data
        bio = author_form.bio.data
        db.session.add(Author(name=name, email=email, website=website, photo=photo, bio=bio))
        db.session.commit()

        return redirect(url_for('paginapadrao_authorall'))


    return render_template("formulario_autor.html", form=author_form, menu=barra_menu)


@app.route("/author_all")
def paginapadrao_authorall():
    barra_menu = ["Início", "Blog", "Sobre", "Contato"]

    autor = Author.query.all()

    return render_template("lista_author.html", menu=barra_menu, author=autor)


@app.route("/forms_category/", methods=['GET', 'POST'])
def paginapadrao_formscate():

    category_form = Categoryforms()

    barra_menu = ["Início", "Blog", "Sobre", "Contato"]
    #categoria = Category.query.all()

    if category_form.validate_on_submit():
        name = category_form.name.data
        db.session.add(Category(name=name))
        db.session.commit()

        return redirect(url_for('paginapadrao'))

    return render_template("formulario_categoria.html", form=category_form, menu=barra_menu)