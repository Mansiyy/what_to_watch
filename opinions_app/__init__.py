from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config


BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(
    __name__,
    instance_path=str(BASE_DIR / "instance")
)

app.config.from_object(Config)

db = SQLAlchemy(app)

migrate = Migrate(app, db)


from .models import Opinion
from .forms import OpinionForm

from .views import (
    opinion_view,
    add_opinion_view,
    index_view
)

from .error_handlers import (
    internal_error,
    page_not_found
)

from .cli_commands import load_opinions_command
