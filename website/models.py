from .views import db
from datetime import datetime
class Paper(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=False, nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    abstract = db.Column(db.Text, unique=True, nullable=False)
    cover = db.Column(db.String(120), unique=False, nullable=False)
    published_date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, unique=False, nullable=False)
    published = db.Column(db.String(6), unique=False, nullable=False)
    slug = db.Column(db.String(300), unique=False, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author = db.relationship('Author', backref=db.backref('papers', lazy=True))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('papers', lazy=True))

    def __init__(self, title, text, abstract, cover, published_date, author, last_modified, category, published, slug):
        self.title = title
        self.text = text
        self.abstract = abstract
        self.cover = cover
        self.published_date = published_date
        self.author = author
        self.last_modified = last_modified
        self.category = category
        self.published = published
        self.slug = slug

    def __str__(self):
        strpaper = "Título: "+self.title+"\n"+"Resumo: "+self.text
        return strpaper


    def __repr__(self):
        reprpaper = "Título: " +self.title
        return reprpaper

    def examples():
        lista_artigos = [Paper("Python é uma linguagem", "Python é uma linguagem de programação de alto nível, "
                         "interpretada, de script, imperativa, orientada a objetos, funcional, "
                          "de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.",
                        "Aqui é um resumo sobre python", "imagem.png", "10/10/2017", "Allan Vitor",
                        "07/06/2018", "Estudo", "Sim", "python_e_uma_linguagem"),
                         Paper("C++ é uma linguagem","C++ é uma linguagem de programação compilada multi-paradigma"
                          " e de uso geral. Desde os anos 1990 é uma das linguagens comerciais mais populares, "
                          "sendo bastante usada também na academia por seu grande desempenho e base de "
                          "utilizadores.","Resumo sobre +CC","imagem2.png","15/10/2017","João Carlos",
                          "15/10/2018","Estudo","Sim","c++_e_uma_linguagem")]

        return lista_artigos


class Author(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    website = db.Column(db.String(120), unique=False, nullable=False)
    photo = db.Column(db.String(120), unique=False, nullable=False)
    bio = db.Column(db.String(300), unique=True, nullable=False)


    def __init__(self, name, email, website, photo, bio):
        self.name = name
        self.email = email
        self.website = website
        self.photo = photo
        self.bio = bio

    def __str__(self):
        strautor = self.name
        return strautor


    def __repr__(self):
        reprautor = "Nome: " +self.name
        return reprautor

    def examples():

        lista_autor = [Author("Allan Carneiro", "allanvitor.carneiro@gmail.com",
                    "allancarneiro.webbly.com", "fotoperfil.jpeg",
                    "Sou estudante de Física na UFRJ, e participo do Programa de Ensino Python Café"),
                       Author("Joao Vitor", "joao.vitor@yahoo.com.br", "facebook.com/joao.vitor",
                        "foto_joao.jpeg", "Sou um exemplo de pessoa, estudo e trabalho e ainda tenho "
                        "tempo para jogar futebol")]

        return lista_autor



class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self,name):
        self.name = name

    def __str__(self):
        strcateg = "Nome: " + self.nome
        return strcateg

    def __repr__(self):
        reprcateg = "Nome: " + self.nome
        return reprcateg

    def examples():
        lista_categ = [Category("Ciências"), Category("Programação"), Category("Física")]

        return lista_categ

if __name__=='__main__':

    pass
