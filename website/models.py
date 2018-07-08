from .views import db
from datetime import datetime
class Paper(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=False, nullable=False)
    abstract = db.Column(db.Text, unique=True, nullable=False)
    text = db.Column(db.Text, unique=True, nullable=False)
    cover = db.Column(db.String(120), unique=False, nullable=False)
    published_date = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.now())
    last_modified = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.now())
    published = db.Column(db.String(6), unique=False, nullable=False)
    slug = db.Column(db.String(300), unique=False, nullable=False)

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author = db.relationship('Author', backref=db.backref('papers', lazy=True))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('papers', lazy=True))

    def __init__(self, title=None, abstract=None,text=None, cover=None, published_date=None, author=None, last_modified=None, category=None, published=None, slug=None, field=None):

        self.title = title
        self.abstract = abstract
        self.text = text
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




class Author(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    website = db.Column(db.String(120), unique=False, nullable=False)
    photo = db.Column(db.String(120), unique=False, nullable=False)
    bio = db.Column(db.String(300), unique=True, nullable=False)


    def __init__(self, name='', email='', website='', photo='', bio='', lista=[], field=None):
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


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name= '', lista=[], field=None):
        self.name = name

    def __str__(self):
        strcateg = self.name
        return strcateg

    def __repr__(self):
        reprcateg = "Nome: " + self.name
        return reprcateg



if __name__=='__main__':

    pass
