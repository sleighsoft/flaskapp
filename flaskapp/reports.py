from flask import Blueprint
from flask import redirect
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort

from flaskapp.db import get_db

from .sql import (
    GET_UNRESOVLED_ENTRIES,
    SET_ENTRY_TO_BLOCKED,
    SET_ENTRY_TO_RESOLVED,
    GET_ENTRY_BY_ID,
)

bp = Blueprint("reports", __name__)


@bp.route("/")
def index():
    """Show all the reports, most recent first."""
    reports = get_unresolved_reports()
    return render_template("reports/index.html", reports=reports)


@bp.route("/block/<int:id>", methods=("POST",))
def block(id):
    """Marks a report as blocked."""
    report = get_report_by_id(id)

    if request.method == "POST":
        db = get_db()
        db.execute(SET_ENTRY_TO_BLOCKED, (id,))
        db.commit()

    reports = get_unresolved_reports()
    return redirect("/")


@bp.route("/resolve/<int:id>", methods=("PUT",))
def resolve(id):
    """Marks a report as resolved."""
    report = get_report_by_id(id)
    if request.method == "PUT":
        db = get_db()
        db.execute(SET_ENTRY_TO_RESOLVED, (id,))
        db.commit()

    reports = get_unresolved_reports()
    return "200"


def get_report_by_id(id):
    """Get a report from the database matching `id`.

    abort(404) if `id` is not found.
    """
    report = get_db().execute(GET_ENTRY_BY_ID, (id,)).fetchone()

    if report is None:
        abort(404, f"Report with {id} does not exist")

    return report


def get_unresolved_reports():
    """Returns all reports from the database."""
    return get_db().execute(GET_UNRESOVLED_ENTRIES).fetchall()
