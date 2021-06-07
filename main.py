from flask import Flask
from api.datab import db


from api.blueprints.base_blueprint import BaseBluePrint


app = Flask(__name__)


app.url_map.strict_slashes = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# register views
blue_prints = BaseBluePrint(app)
blue_prints.register()

# register ORM
import api.models

db.init_app(app)

app.run()
