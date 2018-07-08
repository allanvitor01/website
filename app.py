from website.views import app,db
from website.models import Category, Author, Paper
from datetime import datetime
from website.admin import admin

app.run()
# autor_exemplo = Author.query.filter_by(name="Allan Carneiro").first()
# categoria_exemplo = Category.query.filter_by(name="Educacao").first()
# data = datetime.strptime("10-10-2017", "%d-%m-%Y")
#
# db.session.edit   (Paper(title="Educação", text="Aqui é sobre educação. C++ é uma linguagem de programação compilada multi-paradigma"
#                            " e de uso geral. Desde os anos 1990 é uma das linguagens comerciais mais populares, "
#                            "sendo bastante usada também na academia por seu grande desempenho e base de "
#                            "utilizadores.",
#                        abstract="Sobre educacao Resumo sobre +CC", cover="imagem3.png", published_date=data,
#                        author=autor_exemplo,
#                        last_modified=data, category=categoria_exemplo, published="Sim",
#                        slug="educacao"))
#admin = (Author.query.filter_by(name='Allan Carneiro').update(dict(website='allancarneiro.weebly.com')))
#db.session.commit()

#print(admin)




#db.session.add(Author(name="Allan Carneiro", email="allanvitor.carneiro@gmail.com", website="allan.carneiro.weebly.com", photo="image.png", bio="Essa é minha história"))
#db.session.add(Category(name="Programacao"))
#db.session.add(Category(name="Fisica"))
#db.session.add(Category(name="Educacao"))

#autor_exemplo = Author.query.filter_by(name="Allan Carneiro").first()
#categoria_exemplo = Category.query.filter_by(name="Fisica").first()
#data = datetime.strptime("10-10-2017", "%d-%m-%Y")

#db.session.add(Paper(title="C++ é uma linguagem", text="C++ é uma linguagem de programação compilada multi-paradigma"
#                           " e de uso geral. Desde os anos 1990 é uma das linguagens comerciais mais populares, "
#                           "sendo bastante usada também na academia por seu grande desempenho e base de "
#                           "utilizadores.",
#                       abstract="Resumo sobre +CC", cover="imagem2.png", published_date=data,
#                       author=autor_exemplo,
#                       last_modified=data, category=categoria_exemplo, published="Sim",
#                       slug="c++_e_uma_linguagem"))

#db.session.commit()