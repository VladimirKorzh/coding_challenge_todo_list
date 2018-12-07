import pytest
from src.services.redis import redis_init


@pytest.fixture
def flask_app():
    from src.run import create_app
    application = create_app()
    redis_init(application)

    return application


@pytest.fixture
def client(flask_app):
    return flask_app.test_client()
