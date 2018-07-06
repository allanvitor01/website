import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'fisica_aqui_e_allan_123456'

    app.config['WTF_CSRF_ENABLED'] = True
    app.config['SECRET_KEY'] = 'fisica_aqui_e_allan_123456'