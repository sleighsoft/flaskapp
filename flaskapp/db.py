import sqlite3

import json
import click
from flask import current_app, g
from flask.cli import with_appcontext

from .sql import INSERT_INTO_REPORTS


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    create_tables()
    import_into_db("data/reports.json")


def create_tables():
    db = get_db()

    with current_app.open_resource("schema.sql") as f:
        db.executescript(f.read().decode("utf8"))


def import_into_db(json_file):
    """Inserts data from data/reports.json into the database"""
    db = get_db()

    with current_app.open_resource(json_file) as f:
        reports = json.load(f)

    for element in reports["elements"]:
        entry = (
            element["id"],
            element["source"],
            element["sourceIdentityId"],
            element["state"],
            element["created"],
            element["reference"]["referenceId"],
            element["reference"]["referenceType"],
            element["payload"]["reportType"],
            element["payload"]["reportId"],
            element["payload"]["referenceResourceId"],
            element["payload"]["referenceResourceType"],
            element["payload"]["message"],
        )
        db.execute(INSERT_INTO_REPORTS, entry)

    db.commit()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


# NOTE: Instead of writing the SQL statements a ORM such as SQL-Alchemy could be used.
#       I chose not due to the simple nature of the application.
