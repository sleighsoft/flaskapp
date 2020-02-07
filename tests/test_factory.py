import pytest

from flaskapp import create_app


def test_create_app():
    dev_app = create_app("development")
    assert dev_app.debug == True
    assert dev_app.testing == False

    dev_app = create_app("testing")
    assert dev_app.debug == False
    assert dev_app.testing == True

    with pytest.raises(ValueError) as e:
        dev_app = create_app()

    app = create_app("development", {"DEBUG": False})
    assert app.debug == False
