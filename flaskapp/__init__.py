import os

from flask import Flask


def create_app(env=None, additional_config=None):
    """Creates a Flask application.
    
    Args:
        env: Specifies the used config. One of "development", "testing",
            everything else for production.
        additional_config: Additional config that can override settings from
            `env` in the form of a python dict.
    
    Returns:
        A Flask app.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",  # Change for deployment
        DATABASE=os.path.join(app.instance_path, "flaskapp.sqlite"),
    )

    env = env if env else app.config["ENV"]

    if env == "development":
        app.config.from_object("config.DevelopmentConfig")
    elif env == "testing":
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object("config.ProductionConfig")
        if app.secret_key is None:
            raise ValueError(
                "Please specify a ProductionConfig.SECRET_KEY in config.py! "
                "Use `python -c 'import os; print(os.urandom(16))'` to generate one!"
            )

    if additional_config:
        app.config.update(additional_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db

    db.init_app(app)

    from flaskapp import reports

    app.register_blueprint(reports.bp)

    app.add_url_rule("/", endpoint="index")

    return app
