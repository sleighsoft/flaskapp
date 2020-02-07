import pytest
from werkzeug.exceptions import HTTPException

from flaskapp.db import get_db
from flaskapp.reports import get_report_by_id


def test_index(client):
    response = client.get("/")
    assert b"Reports" in response.data
    assert b"State" in response.data


@pytest.mark.parametrize("id", (25, 16))
def test_block(client, app, id):
    path = f"/block/{id}"
    response = client.post(path)
    assert response.status == "302 FOUND"
    with app.app_context():
        db = get_db()
        row = db.execute("SELECT * FROM reports WHERE id = ?", (id,)).fetchone()
        assert row["state"] == "BLOCKED"


@pytest.mark.parametrize("id", (25, 16))
def test_resolve(client, app, id):
    path = f"/resolve/{id}"
    response = client.put(path)
    assert response.status == "200 OK"
    with app.app_context():
        db = get_db()
        row = db.execute("SELECT * FROM reports WHERE id = ?", (id,)).fetchone()
        assert row["state"] == "RESOLVED"


@pytest.mark.parametrize("id", (25, 16))
def test_hidden_resolved(client, app, id):
    path = f"/resolve/{id}"
    client.put(path)
    response = client.get("/")
    assert str.encode(f"post-{id}") not in response.data


def test_get_report_by_id(app):
    with app.app_context():
        row = get_report_by_id(25)
        assert row["id"] == 25

        with pytest.raises(HTTPException) as e:
            get_report_by_id(-1)

