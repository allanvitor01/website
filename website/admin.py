from .views import app, db
from flask_admin import Admin
from .models import Paper, Author, Category
from flask_admin.contrib.sqla import ModelView


admin = Admin(app, name="sitepessoal", template_mode="bootstrap3")


admin.add_view(ModelView(Paper, db.session))
admin.add_view(ModelView(Author, db.session))
admin.add_view(ModelView(Category, db.session))
