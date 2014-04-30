import logging
from flask import Flask
from flaskboiler.data import db


def create_app():
    """
    Factory that creates the :class:`Flask` application:
        - Registers interfaces
        - Setup configuration

    :return: :class:`Flask` application that was created.
    """
    # Create the :class:`Flask` application and setup the configuration (points to instance/boilerpy.cfg)
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('flaskboiler.cfg')

    # Turn off strict slashes, which tells Werkzeug to not care about trailing slashes. Thus,
    # hitting /some/url and /some/url/ have the same behavior.
    app.url_map.strict_slashes = False

    app.logger.setLevel(logging.DEBUG)

    # Register interfaces from blueprint
    from .interfaces import api
    app.register_blueprint(api)

    # Configure database
    db.init_app(app)

    return app
