from flask import Flask
from app import config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(config)

# Login管理登録
lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'auth.login'
lm.init_app(app)

from app.views import dailyManager
from app.views import authviews

app.register_blueprint(authviews.auth, url_prefix='/auth')
