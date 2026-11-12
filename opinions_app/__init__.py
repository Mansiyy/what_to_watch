from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config


BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    instance_path=str(BASE_DIR / 'instance'),
    template_folder=str(BASE_DIR / 'templates'),
    static_folder=str(BASE_DIR / 'static')
)
app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)


from .models import Opinion
from .forms import OpinionForm

from .views import (
    internal_error,
    page_not_found,
    opinion_view,
    add_opinion_view,
    index_view
)

from .commands import load_opinions_command