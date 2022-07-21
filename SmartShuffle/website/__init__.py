from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from . import creds
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
DB_NAME = "smartshuffle.db"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=creds.CLIENT_ID, client_secret=creds.CLIENT_SECRET))

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='ofwgkta'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    migrate.init_app(app, db)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    from .models import User

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    # if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created database!')

